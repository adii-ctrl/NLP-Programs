
# Program 2: Stemming and Lemmatization using NLTK

import nltk

# Download required NLTK data
nltk.download("wordnet")
nltk.download("omw-1.4")

from nltk.stem import PorterStemmer, WordNetLemmatizer

# Sample words
words = [
    "playing",
    "played",
    "plays",
    "studies",
    "studying",
    "running",
    "runner",
    "easily",
    "fairly"
]

# Create objects
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# ---------------- Stemming ----------------

print("========== STEMMING ==========")

for word in words:
    stemmed_word = stemmer.stem(word)
    print(f"{word} -> {stemmed_word}")


# ---------------- Lemmatization ----------------

print("\n========== LEMMATIZATION ==========")

for word in words:
    lemmatized_word = lemmatizer.lemmatize(word)
    print(f"{word} -> {lemmatized_word}")

