from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "I love natural language processing",
    "NLP is useful for text analysis",
    "I love text analysis"
]

vectorizer = CountVectorizer()
bow = vectorizer.fit_transform(documents)

print("Words:", vectorizer.get_feature_names_out())
print("BoW Matrix:")
print(bow.toarray())
