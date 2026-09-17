# Program 1: Tokenization using NLTK and spaCy

import nltk
import spacy

# Download required NLTK data
nltk.download("punkt")
nltk.download("punkt_tab")

from nltk.tokenize import sent_tokenize, word_tokenize

# Sample text
text = "Natural Language Processing is a field of Artificial Intelligence. It helps computers understand human language."

# ---------------- NLTK Tokenization ----------------

print("========== NLTK TOKENIZATION ==========")

# Sentence Tokenization
nltk_sentences = sent_tokenize(text)

print("\nSentence Tokens:")
for sentence in nltk_sentences:
    print(sentence)

# Word Tokenization
nltk_words = word_tokenize(text)

print("\nWord Tokens:")
print(nltk_words)


# ---------------- spaCy Tokenization ----------------

print("\n========== SPACY TOKENIZATION ==========")

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Process the text
doc = nlp(text)

# Sentence Tokenization
print("\nSentence Tokens:")
for sentence in doc.sents:
    print(sentence.text)

# Word Tokenization
print("\nWord Tokens:")
for token in doc:
    print(token.text)