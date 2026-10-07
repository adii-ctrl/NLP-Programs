from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

documents = [
    "I love natural language processing",
    "NLP is useful for text analysis",
    "I love text analysis"
]

bow_vectorizer = CountVectorizer()
bow = bow_vectorizer.fit_transform(documents)

tfidf_vectorizer = TfidfVectorizer()
tfidf = tfidf_vectorizer.fit_transform(documents)

print("BoW Vocabulary:")
print(bow_vectorizer.get_feature_names_out())
print("\nBoW Matrix:")
print(bow.toarray())

print("\nTF-IDF Vocabulary:")
print(tfidf_vectorizer.get_feature_names_out())
print("\nTF-IDF Matrix:")
print(tfidf.toarray())
