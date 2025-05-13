import whisper

model = whisper.load_model("base")  # or "tiny" if system is slow
result = model.transcribe("/home/rithul/Desktop/Main/Projects/test/output.wav")
print(result["text"])


