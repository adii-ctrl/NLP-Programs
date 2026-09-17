id="j6q3gk"
# Program 3: Stop-word Removal using NLTK

import nltk

# Download required NLTK data
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("punkt_tab")

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Sample document
text = """
Natural Language Processing is a branch of Artificial Intelligence.
It helps computers understand and process human language.
"""

# Convert text into words
words = word_tokenize(text)

# Get English stop words
stop_words = set(stopwords.words("english"))

# Remove stop words
filtered_words = [
    word for word in words
    if word.lower() not in stop_words
]

# Display results
print("========== ORIGINAL DOCUMENT ==========")
print(text)

print("========== WORDS BEFORE STOP-WORD REMOVAL ==========")
print(words)

print("\n========== STOP WORDS ==========")
print(sorted(stop_words))

print("\n========== WORDS AFTER STOP-WORD REMOVAL ==========")
print(filtered_words)
