import gradio as gr
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
from transformers import pipeline
import textwrap

# Extract video ID from YouTube URL
def extract_video_id(url):
    parsed_url = urlparse(url)
    if 'youtube' in parsed_url.netloc:
        return parse_qs(parsed_url.query).get('v', [None])[0]
    elif 'youtu.be' in parsed_url.netloc:
        return parsed_url.path[1:]
    return None

# Get transcript
def get_youtube_transcript(video_id):
    language_options = ['en-IN', 'en']
    for lang in language_options:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
            text = ' '.join([item['text'] for item in transcript])
            return text
        except:
            continue
    return None

# Summarize using Hugging Face
def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    wrapped = textwrap.wrap(text, 1000)
    summary = ''
    for chunk in wrapped:
        summary_piece = summarizer(chunk, max_length=150, min_length=60, do_sample=False)[0]['summary_text']
        summary += summary_piece + ' '
    return summary.strip()

# Gradio Function
def summarize_youtube_video(url):
    video_id = extract_video_id(url)
    if not video_id:
        return "❌ Invalid YouTube URL.", ""

    transcript = get_youtube_transcript(video_id)
    if not transcript:
        return "❌ Transcript not available for this video.", ""

    summary = summarize_text(transcript)
    return transcript, summary

# Gradio UI
demo = gr.Interface(
    fn=summarize_youtube_video,
    inputs=gr.Textbox(label="🔗 Enter YouTube video URL"),
    outputs=[
        gr.Textbox(label="📃 Full Transcript", lines=5),
        gr.Textbox(label="📝 Video Summary", lines=7)
    ],
    title="🎥 YouTube Video Transcript Summarizer",
    description="Paste a YouTube URL to get the transcript and a concise summary powered by Hugging Face models! 💡",
)

if __name__ == "__main__":
    demo.launch()
