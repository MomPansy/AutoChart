from transformers import pipeline
import gradio as gr

pipe = pipeline(model="Mompansy/whisperfinetune_modelcheckpoints")  # change to "your-username/the-name-you-picked"

def transcribe(audio):
    text = pipe(audio)["text"]
    return text

iface = gr.Interface(
    fn=transcribe, 
    inputs=gr.Audio(source="microphone", type="filepath"), 
    outputs="text",
    title="Whisper Small Singapore",
    description="Realtime demo for Singaporean English speech recognition using a fine-tuned Whisper small model.",
)

iface.launch()
