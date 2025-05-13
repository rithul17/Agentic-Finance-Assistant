import streamlit as st
import requests

st.title("Audio Recorder")

# Prompt the user to record audio
audio_data = st.audio_input("Record your message")

if audio_data:
    # Playback the recorded audio
    st.audio(audio_data)

    # Save the audio to a file
    with open("recorded_audio.wav", "wb") as f:
        f.write(audio_data.getbuffer())
#    st.success("Audio recorded and saved successfully!")

    # Prepare the file for upload
    files = {"file": ("recorded_audio.wav", audio_data.getbuffer(), "audio/wav")}

    # Send the file to the FastAPI backend
    try:
        response = requests.post("http://localhost:8000/upload-audio/", files=files)
        if response.status_code == 200:
            st.success("Audio file sent to backend successfully!")
            st.json(response.json())
        else:
            st.error(f"Failed to send audio file. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

