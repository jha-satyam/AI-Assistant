############################## README ##############################
############################## README ##############################

#1. Once run this script will take 2 types of recording, i.e.,
#   the wakeword - "Hey Alan" and the ambient noise

#2. Please try to take at least 2 batches of 100 recordings

#3. Record the first batch using a dedicated mic, i.e., an 
#   earphone's mic, a bluetooth mic, etc. held close to your
#   mouth in a noise free silent room/environment

#4. Record the second batch using your device's inbuilt mic 
#   in a slightly/moderately noisy environment

#Please install the package "sounddevice" before running this script
#enter the following command in your python code runner or command line to install the package:
#pip install sounddevice


import sounddevice as sd
from scipy.io.wavfile import write
import os

def wakeword_record(to_path, n_times=100):
    for i in range(n_times):
        fs = 44100
        seconds = 2
        wakeword = sd.rec(seconds * fs, samplerate=fs, channels=2)
        sd.wait()
        write(f"{to_path}/wakeword{i+1}.wav", fs, wakeword)
        input(f"Press Enter to record next or press q to exit...{i+1}/{n_times}")

def ambient_sound_record(to_path, n_times=100):
    for i in range(n_times):
        fs = 44100
        seconds = 2
        ambient_sound = sd.rec(seconds * fs, samplerate=fs, channels=2)
        sd.wait()
        write(f"{to_path}/ambient{i}.wav", fs, ambient_sound)
        print(f"Press Ctrl+C to exit. Recording...{i+1}/{n_times}")

input_user = input("Please Enter your name before recording your voice: ")
cwd = os.getcwd()
user_dir = f"{cwd}/{input_user}"
os.makedirs(user_dir, exist_ok=True)
wakeword_dir = f"{user_dir}/wakeword"
os.makedirs(wakeword_dir, exist_ok=True)

input("Press Enter to start recording the wakeword \"Hey Alan\" or press Ctrl+C to exit:")
wakeword_record(wakeword_dir, 2)

input_env = input("Please enter a 1-3 words description of your current environment for recording your ambient noise: ")    
non_wakeword_dir = f"{user_dir}/{input_env}"
os.makedirs(non_wakeword_dir, exist_ok=True)

input("Press Enter to start recording ambient audio or press Ctrl+C to exit:")
ambient_sound_record(non_wakeword_dir)