from nltk.util import ngrams
from nltk.tokenize import word_tokenize
import nltk

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

text = "Natural language processing is very useful"

words = word_tokenize(text.lower())

print("Unigrams:")
print(list(ngrams(words, 1)))

print("\nBigrams:")
print(list(ngrams(words, 2)))

print("\nTrigrams:")
print(list(ngrams(words, 3)))
