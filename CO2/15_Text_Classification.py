from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

texts = [
    "I love this movie",
    "This film is amazing",
    "The movie was excellent",
    "I hated this movie",
    "This film is terrible",
    "The movie was boring",
    "Amazing acting and story",
    "Worst movie ever",
    "Excellent and enjoyable",
    "Very boring and bad"
]

labels = [
    "positive", "positive", "positive",
    "negative", "negative", "negative",
    "positive", "negative", "positive", "negative"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.3, random_state=42, stratify=labels
)

model = MultinomialNB()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))

new_text = ["The movie was amazing"]
new_vector = vectorizer.transform(new_text)

print("Prediction:", model.predict(new_vector)[0])
