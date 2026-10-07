from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "machine learning is used for artificial intelligence",
    "natural language processing works with text data",
    "deep learning uses neural networks",
    "machine learning algorithms learn from data"
]

query = "machine learning data"

vectorizer = TfidfVectorizer()
document_vectors = vectorizer.fit_transform(documents)
query_vector = vectorizer.transform([query])

scores = cosine_similarity(query_vector, document_vectors)[0]

ranking = scores.argsort()[::-1]

print("Query:", query)
print("\nRanked Documents:")

for rank, index in enumerate(ranking, start=1):
    print(f"{rank}. Score = {scores[index]:.4f}")
    print("   ", documents[index])
