import streamlit as st
from phi.agent import Agent
from phi.llm.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
import google.generativeai as genai
from pytube import YouTube
import time
from pathlib import Path
import tempfile
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)
else:
    st.error("GOOGLE_API_KEY environment variable not set. Please add it to your .env file.")
    st.stop()

st.set_page_config(
    page_title="Calyx AI",
    page_icon="🤖",
    layout="wide",
)
st.title("Calyx: AI Video Analyzer")
st.header("Analyze Videos from Upload or YouTube Link")
st.markdown("---")

@st.cache_resource
def initialize_agent():
    return Agent(
        name="Video AI Summarizer",
        llm=Gemini(model="models/gemini-1.5-flash"),
        tools=[DuckDuckGo()],
        markdown=True,
        description="You are a world-class AI agent for analyzing video content. You will be provided a video and a user query. Your goal is to answer the user's query based on the video's content, and you can use the DuckDuckGo search tool to find additional information if needed.",
    )

def analyze_video_content(video_path: str, user_query: str, agent: Agent):
    if not Path(video_path).exists():
        st.error("Video file not found at the specified path.")
        return

    try:
        with st.spinner("Uploading and processing video... This may take a moment."):
            processed_file = genai.upload_file(path=video_path)

            while processed_file.state.name == "PROCESSING":
                time.sleep(5)
                processed_file = genai.get_file(processed_file.name)

            if processed_file.state.name == "FAILED":
                st.error("Video processing failed. Please try a different video.")
                return

        with st.spinner("Analyzing content and generating insights..."):
            analysis_prompt = f"""
            You are an expert video analyst. Analyze the provided video thoroughly.
            Based on the video's content and context, answer the following user query:

            **User Query:** "{user_query}"

            Provide a detailed, well-structured, and user-friendly response in Markdown format.
            If necessary, use your search tool to gather supplementary information for a more comprehensive answer.
            """
            response = agent.run(analysis_prompt, files=[processed_file])

        st.subheader("💡 Analysis Result")
        st.markdown(response)

    except Exception as e:
        st.error(f"An error occurred during analysis: {e}")
    finally:
        Path(video_path).unlink(missing_ok=True)

multimodal_agent = initialize_agent()

input_method = st.radio(
    "Choose your video source:",
    ("Upload a video", "Provide a YouTube link"),
    horizontal=True,
)

st.markdown("---")

user_query = st.text_area(
    "What insights are you seeking from the video?",
    placeholder="e.g., 'Summarize the key points of this lecture.' or 'What is the main product being advertised?'",
    height=100,
    help="Provide specific questions or insights you want from the video."
)

if input_method == "Upload a video":
    video_file = st.file_uploader(
        "Upload a video file", type=['mp4', 'mov', 'avi', 'mkv'], help="Upload a video for AI analysis"
    )

    if st.button("🔍 Analyze Uploaded Video", key="analyze_upload_button"):
        if video_file and user_query:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
                temp_video.write(video_file.read())
                video_path = temp_video.name
            
            st.video(video_path)
            analyze_video_content(video_path, user_query, multimodal_agent)
        else:
            st.warning("Please upload a video and enter a query before analyzing.")

elif input_method == "Provide a YouTube link":
    yt_url = st.text_input("Enter the YouTube video URL:", placeholder="https://www.youtube.com/watch?v=...")

    if st.button("🔍 Analyze YouTube Video", key="analyze_yt_button"):
        if yt_url and user_query:
            video_path = None
            try:
                with st.spinner("Downloading video from YouTube..."):
                    yt = YouTube(yt_url)
                    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
                    
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
                        stream.download(filename=temp_video.name)
                        video_path = temp_video.name
                
                st.video(video_path)
                analyze_video_content(video_path, user_query, multimodal_agent)

            except Exception as e:
                st.error(f"Failed to download or process YouTube video: {e}")
                if video_path:
                    Path(video_path).unlink(missing_ok=True)
        else:
            st.warning("Please provide a YouTube URL and enter a query before analyzing.")

st.markdown("---")
st.info("Upload a video file or provide a YouTube link and ask a question to begin analysis.")
