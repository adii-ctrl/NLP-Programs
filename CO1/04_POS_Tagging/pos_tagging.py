
# Program 4: Part-of-Speech (POS) Tagging using NLTK

import nltk

# Download required NLTK data
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")

from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Given sentence
sentence = "The intelligent student is studying Natural Language Processing."

# Tokenize the sentence
words = word_tokenize(sentence)

# Perform POS tagging
pos_tags = pos_tag(words)

# Display the sentence
print("========== GIVEN SENTENCE ==========")
print(sentence)

# Display POS tags
print("\n========== POS TAGGING ==========")

for word, tag in pos_tags:
    print(f"{word} -> {tag}")
