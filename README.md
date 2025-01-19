# Calyx: Your AI Video Summarizer (Powered by Gemini)
## Live: https://calyx-ai.streamlit.app/

Calyx is an AI-powered tool that analyzes and summarizes video content. With the help of Google Gemini, Calyx provides detailed insights into your videos, answering questions and extracting meaningful context from them. Simply upload your video, ask a question, and let Calyx provide you with a summary or analysis based on its content and context.

## Features

- **AI-powered video summarization**: Powered by Google's Gemini model, Calyx generates insightful summaries based on your video content.
- **Video content analysis**: Ask specific questions and receive detailed answers based on the video's context.
- **Web integration**: Get additional insights through web research to complement video analysis.
- **Easy video uploading**: Upload MP4, MOV, and AVI video files directly through the interface.

## Technologies

- **Streamlit**: For the web interface, allowing an easy-to-use application for video uploading and analysis.
- **Google Gemini**: A powerful generative AI model used for video analysis and summarization.
- **Python**: Backend code for managing video uploads, processing, and generating responses.
- **DuckDuckGo**: For web-based tools that provide additional research capabilities to enhance video analysis.

## Installation

### Prerequisites

Before using Calyx, you need to have the following:

- **Python 3.7+**: Make sure Python is installed on your machine.
- **Streamlit**: This application uses Streamlit for building the UI.
- **Google Gemini API Key**: You'll need an API key for Google's Gemini model to authenticate and interact with it.

### Steps to Install

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/calyx.git
   cd calyx
   ```
   
2. Install the Necessary Python Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3.  Set Up Your Environment Variables:
  ```bash
  GEMINI_API_KEY=your-gemini-api-key
  ```

4. Run the Streamlit App:
   ```bash
   streamlit run app.py
   ```
## Usage

### Upload a Video

- Click the "Upload a video file" button to upload a video in MP4, MOV, or AVI format.
- The video will be processed, and you will be able to interact with the AI for insights.

### Ask Questions

- Once the video is uploaded, use the text area to enter a question about the video.
- Click the "🔍 Analyze video" button to receive a detailed analysis based on the video content and context.

### Results

- The AI will generate a summary and answer your query with the help of the video content.
- Additional web-based research might be included in the response to provide a more complete answer.

### Example Queries

Here are some example questions you can ask Calyx to analyze the video:

- "What is the main topic discussed in this video?"
- "Summarize the key points from the meeting in this video."
- "What insights can you provide from the lecture video?"

## Contributing

If you'd like to contribute to Calyx, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- **Streamlit**: For providing an easy-to-use interface for building data-driven applications.
- **Google Gemini**: For enabling powerful generative AI models to process and analyze videos.
- **DuckDuckGo**: For enhancing the tool with web-based research capabilities.
