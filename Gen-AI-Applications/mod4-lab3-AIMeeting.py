'''
import requests
# URL of the audio file to be downloaded
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX04C6EN/Testing%20speech%20to%20text.mp3"
# Send a GET request to the URL to download the file
response = requests.get(url)
# Define the local file path where the audio file will be saved
audio_file_path = "downloaded_audio.mp3"
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # If successful, write the content to the specified local file path
    with open(audio_file_path, "wb") as file:
        file.write(response.content)
    print("File downloaded successfully")
else:
    # If the request failed, print an error message
    print("Failed to download the file")
'''

import torch
from transformers import pipeline
import gradio as gr


def transcript_audio(audio_file):
    # Initialize the speech-to-text pipeline from Hugging Face Transformers
    # This uses the "openai/whisper-tiny.en" model for automatic speech recognition (ASR)
    # The `chunk_length_s` parameter specifies the chunk length in seconds for processing
    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-tiny.en",
        chunk_length_s=30,
        )
    # Define the path to the audio file that needs to be transcribed
    sample = 'sample2.mp3'
    # Perform speech recognition on the audio file
    # The `batch_size=8` parameter indicates how many chunks are processed at a time
    # The result is stored in `prediction` with the key "text" containing the transcribed text
    prediction = pipe(sample, batch_size=8)["text"]
    # Print the transcribed text to the console
    return prediction

# Set up Gradio interface
audio_input = gr.Audio(sources="upload", type="filepath")  # Audio input
output_text = gr.Textbox()  # Text output
# Create the Gradio interface with the function, inputs, and outputs
iface = gr.Interface(fn=transcript_audio, 
                     inputs=audio_input, outputs=output_text, 
                     title="Audio Transcription App",
                     description="Upload the audio file")
# Launch the Gradio app
iface.launch(server_name="0.0.0.0", server_port=7860)