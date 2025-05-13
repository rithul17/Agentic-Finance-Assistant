from TTS.api import TTS

# Download and load a lightweight TTS model
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)

# Synthesize speech and save to file
tts.tts_to_file(text="Hello, this is a test!", file_path="output.wav")


