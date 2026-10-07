from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "I love machine learning",
    "I love artificial intelligence",
    "The weather is beautiful today"
]

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(documents)

similarity = cosine_similarity(vectors)

print("Cosine Similarity Matrix:")
print(similarity)

print("\nSimilarity between Document 1 and Document 2:")
print(similarity[0][1])
