import sounddevice as sd
import numpy as np
import whisper

# Load Whisper model
model = whisper.load_model("base")

def record_audio(duration=5, fs=16000):
    """
    Record audio for a given duration and sample rate.
    """
    print(f"Recording for {duration} seconds...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    return np.squeeze(recording)  # Remove channel dimension and ensure float32 format

def transcribe(audio):
    """
    Transcribe the recorded audio to text using Whisper.
    """
    result = model.transcribe(audio)
    return result['text']

def main():
    try:
        # Record audio
        duration = 5  # Duration in seconds
        sample_rate = 16000
        audio = record_audio(duration, sample_rate)

        # Transcribe audio
        transcription = transcribe(audio)
        print("Transcription:\n", transcription)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
