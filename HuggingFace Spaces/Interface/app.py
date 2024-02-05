from transformers import pipeline
import gradio as gr
from utils import agents
import librosa

asr = pipeline(
        "automatic-speech-recognition", 
        model="Mompansy/whisperfinetune_modelcheckpointsv2", 
        device_map= 'auto',
    )

    # setting model config parameters
asr.model.config.forced_decoder_ids = (
    asr.tokenizer.get_decoder_prompt_ids(
        language="en", 
        task="transcribe"
    )
)

def transcribe(audio):
    # Gradio passes audio as a tuple (file_path, sample_rate)

    try:
        audio_data, samplerate = librosa.load(audio, sr = 16000)
    except Exception as e:
        print(f"Failed to load audio: {e}")
        return 
        # Handle the error or log it

    # Initialize conversationFormattingAgent
    transcipt_organiser = agents.conversationFormattingAgent()
    # Initialize medicalScribeAgent
    scribe = agents.MedicalScribeAgent()
    # Get transcription from tuned whisper model
    temp = asr(audio_data,chunk_length_s=20)
    text = temp['text']

    transcipt_organiser.step(text)
    formatted_transcription = transcipt_organiser.get_response()

    # Get medical document
    scribe.step(formatted_transcription)
    response = scribe.get_response()
    return (formatted_transcription, response)

with gr.Blocks() as demo:
    with gr.Row():
        audio_input = gr.Audio(sources="upload", type="filepath")
    with gr.Row():
        formatted_conversation = gr.Text(label="Formatted Conversation")
        formatted_medical_chart = gr.Text(label="Formatted Medical Chart")

    gr.Button("Transcribe").click(
        transcribe, 
        inputs=audio_input, 
        outputs=[formatted_conversation, formatted_medical_chart]
    )

demo.launch()
