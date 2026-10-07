from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

documents = [
    "machine learning algorithms and data",
    "deep learning neural networks and data",
    "football match team player goal",
    "football player scored a goal",
    "python programming machine learning",
    "neural network training and algorithms"
]

vectorizer = CountVectorizer(stop_words="english")
X = vectorizer.fit_transform(documents)

lda = LatentDirichletAllocation(
    n_components=2,
    random_state=42
)
lda.fit(X)

words = vectorizer.get_feature_names_out()

for topic_index, topic in enumerate(lda.components_):
    top_words = topic.argsort()[-5:][::-1]
    print(f"Topic {topic_index + 1}:")
    print([words[i] for i in top_words])
