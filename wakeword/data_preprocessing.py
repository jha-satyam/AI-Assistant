import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

##### FOR SINGLE DATA #####
#### LOADING THE VOICE DATA FOR VISUALIZATION ###
'''
sample = "wakeword/wakeword_audio/renu/wakeword8.wav"
data, sample_rate = librosa.load(sample)

##### VISUALIZING WAVE FORM ##
plt.title("Wave Form")
librosa.display.waveshow(data, sr=sample_rate)
plt.show()

##### VISUALIZING MFCC #######
mfccs = librosa.feature.mfcc(y=data, sr=sample_rate, n_mfcc=40)
print("Shape of mfcc:", mfccs.shape)

plt.title("MFCC")
librosa.display.specshow(mfccs, sr=sample_rate, x_axis='time')
plt.show()
'''

##### FOR ALL DATA #####
all_data = []

data_path_dict = {
    0: [[f"wakeword/ambient_audio/{environment}/{file_path}" for file_path in os.listdir(f"wakeword/ambient_audio/{environment}")] for environment in os.listdir("wakeword/ambient_audio/")],
    1: [[f"wakeword/wakeword_audio/{speaker}/{file_path}" for file_path in os.listdir(f"wakeword/wakeword_audio/{speaker}")] for speaker in os.listdir("wakeword/wakeword_audio/")]
}

# the wakeword/ambient_audio/ directory has all sounds which DOES NOT CONTAIN wake word
# the wakeword/wakeword_audio/ directory has all sound WHICH HAS Wake word

for class_label, label_sounds in data_path_dict.items():
    for sound_samples in label_sounds:
        for sound in sound_samples:
            data, sampling_rate = librosa.load(sound)
            mfccs = librosa.feature.mfcc(y=data, sr=sampling_rate, n_mfcc=40)
            mfccs_mean = np.mean(mfccs.T, axis=0)
            all_data.append([mfccs_mean, class_label])
    print(f"INFO: Processed all data for the class: {class_label}")


df = pd.DataFrame(all_data, columns=['feature', 'class_label'])
df.to_pickle("wakeword/final_preprocessed_data_csv/preprocessed_labelled_audio_data.csv")