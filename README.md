 🎥 YouTube Video Transcript Summarizer 📝

This project extracts transcripts from YouTube videos and provides a concise, AI-generated summary using Hugging Face's `facebook/bart-large-cnn` model. The app is built with **Gradio** for a simple and interactive UI.

 🚀 Features

- ✅ Extracts video transcript from YouTube URL (supports `youtube.com` and `youtu.be`)
- ✅ Uses multiple language fallback (`en-IN`, `en`) for better transcript availability
- ✅ Summarizes long video transcripts into readable summaries
- ✅ Clean and modern Gradio UI

🧠 Tech Stack

- [Gradio](https://www.gradio.app/) - For UI
- [Hugging Face Transformers](https://huggingface.co/transformers/) - For text summarization
- [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/) - For fetching YouTube video transcripts

 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/youtube-transcript-summarizer.git
   cd youtube-transcript-summarizer
