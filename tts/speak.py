import os

def speak(speech_str):
    tts = f"mimic3 {speech_str} | aplay"
    os.system(tts)

if __name__ == "__main__":
    speak("Goodbye Nana")