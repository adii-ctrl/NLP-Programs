import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

texts = [
    "great movie", "excellent acting", "loved this film", "wonderful story",
    "bad movie", "awful acting", "hated this film", "boring story",
    "really great film", "very bad story", "excellent movie", "awful film"
]
labels = np.array([1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0])

tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)
X = pad_sequences(tokenizer.texts_to_sequences(texts), maxlen=6, padding="post")

model = Sequential([
    Embedding(1000, 16, input_length=6),
    LSTM(16),
    Dense(1, activation="sigmoid")
])
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
model.fit(X, labels, epochs=10, verbose=1)

sample = ["great and wonderful movie"]
sample_X = pad_sequences(tokenizer.texts_to_sequences(sample), maxlen=6, padding="post")
score = float(model.predict(sample_X, verbose=0)[0][0])
print("Prediction:", "Positive" if score >= 0.5 else "Negative", "score:", round(score, 3))
