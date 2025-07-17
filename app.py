import whisper
import gradio as gr
import tempfile

# Load Whisper model
model = whisper.load_model("base")

def transcribe(audio):
    if audio is None:
        return "No audio provided.", None
    
    with tempfile.NamedTemporaryFile(suffix=".webm", delete=False) as tmp:
        tmp.write(audio.read())
        tmp_path = tmp.name
    
    result = model.transcribe(tmp_path, language="yi")
    text = result["text"]
    
    transcript_path = tmp_path + ".txt"
    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(text)
    
    return text, transcript_path

iface = gr.Interface(
    fn=transcribe,
    inputs=gr.Audio(source="microphone", type="file", label="🎤 Record in Yiddish"),
    outputs=[
        gr.Textbox(label="📝 Transcription (Yiddish)"),
        gr.File(label="⬇️ Download Text File")
    ],
    title="Yiddish Voice-to-Text (Whisper)",
    description="Speak in Yiddish and get a transcription. Powered by Whisper."
)

iface.launch()
