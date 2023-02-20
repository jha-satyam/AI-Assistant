import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras import Sequential
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Dense, Activation, Dropout
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

df = pd.read_pickle("wakeword/final_preprocessed_data_csv/preprocessed_labelled_audio_data.csv")

X = df["feature"].values
X = np.concatenate(X, axis=0).reshape(len(X), 40)

Y = np.array(df["class_label"].to_list())
Y = to_categorical(Y)

##### TRAIN AND TEST DATA SPLIT #####
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

##### TRAINING MODEL ARCHITECTURE #####
model = Sequential([
    Dense(256, input_shape=X_train[0].shape),
    Activation('relu'),
    Dropout(0.5),
    Dense(256),
    Activation('relu'),
    Dropout(0.5),
    Dense(2, activation='softmax')
])

print(model.summary())

model.compile(
    loss="categorical_crossentropy",
    optimizer='adam',
    metrics=['accuracy']
)

print("Model Score: \n")
history = model.fit(X_train, Y_train, epochs=1000)
model.save("wakeword/saved_model/WWD_1000ep.h5")
score = model.evaluate(X_test, Y_test)
print(score)

##### EVALUATING THE MODEL USING A CONFUSION MATRIX #####
print("Model Classification Report: \n")
y_pred = np.argmax(model.predict(X_test), axis=1)
cm = confusion_matrix(np.argmax(Y_test, axis=1), y_pred)
print(classification_report(np.argmax(Y_test, axis=1), y_pred))
ConfusionMatrixDisplay(cm, display_labels=["Non-Wakeword", "Wakeword"]).plot()
plt.show()