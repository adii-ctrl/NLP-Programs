
# Program 5: Parsing and Chunking using RegEx and spaCy

import nltk
import spacy

# Download required NLTK data
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")

from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.chunk import RegexpParser


# Sample sentence
sentence = "The intelligent student is studying Natural Language Processing."


# ==========================================================
# REGEX CHUNKING USING NLTK
# ==========================================================

print("========== REGEX CHUNKING USING NLTK ==========")

# Tokenize the sentence
words = word_tokenize(sentence)

# Perform POS tagging
pos_tags = pos_tag(words)

print("\nPOS Tags:")
print(pos_tags)

# Define a noun phrase chunking grammar
grammar = """
    NP: {<DT>?<JJ>*<NN.*>+}
"""

# Create a RegEx parser
chunk_parser = RegexpParser(grammar)

# Parse the POS-tagged sentence
tree = chunk_parser.parse(pos_tags)

print("\nChunk Tree:")
print(tree)


# ==========================================================
# DEPENDENCY PARSING USING SPACY
# ==========================================================

print("\n========== DEPENDENCY PARSING USING SPACY ==========")

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Process the sentence
doc = nlp(sentence)

# Display dependency information
print("\nWord -> Dependency -> Head")

for token in doc:
    print(f"{token.text} -> {token.dep_} -> {token.head.text}")
