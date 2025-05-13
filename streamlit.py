import streamlit as st
import requests

st.title("🎙️ Audio Recorder + TTS Response")

# Record user's voice
audio_data = st.audio_input("Record your message")

if audio_data:
    # Playback user recording
    st.audio(audio_data, format="audio/wav")

    # Save locally (optional)
    with open("recorded_audio.wav", "wb") as f:
        f.write(audio_data.getbuffer())

    # Prepare the file to send
    files = {"file": ("recorded_audio.wav", audio_data.getbuffer(), "audio/wav")}

    # Send to FastAPI backend
    try:
        response = requests.post("http://localhost:8000/upload-audio/", files=files)
        if response.status_code == 200:
            st.success("✅ Audio file sent to backend successfully.")
            st.json(response.json())
        else:
            st.error(f"❌ Failed to send audio. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"⚠️ Error sending audio: {e}")

    # Fetch the TTS-generated audio response from backend
    st.write("⏳ Waiting for TTS response...")

    try:
        tts_response = requests.get("http://localhost:8000/get-tts-audio/")
        if tts_response.status_code == 200:
            with open("tts_output.wav", "wb") as f:
                f.write(tts_response.content)
            st.audio("tts_output.wav", format="audio/wav")
            st.success("🔊 TTS response received and played.")
        else:
            st.error("❌ Failed to fetch TTS audio from backend.")
    except Exception as e:
        st.error(f"⚠️ Error fetching TTS audio: {e}")

