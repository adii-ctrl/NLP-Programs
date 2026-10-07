from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

documents = [
    "machine learning and artificial intelligence",
    "deep learning and neural networks",
    "football match and football player",
    "team scored a goal in the match"
]

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(documents)

lsa = TruncatedSVD(n_components=2, random_state=42)
lsa_matrix = lsa.fit_transform(X)

print("LSA Document-Topic Matrix:")
print(lsa_matrix)

terms = vectorizer.get_feature_names_out()

for topic_index, component in enumerate(lsa.components_):
    top_words = component.argsort()[-5:][::-1]
    print(f"\nTopic {topic_index + 1}:")
    print([terms[i] for i in top_words])
