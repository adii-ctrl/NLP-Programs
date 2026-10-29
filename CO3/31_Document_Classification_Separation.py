from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline

samples = [
    ("sports", "The team won the football match with a goal."),
    ("sports", "The player and coach celebrated the victory."),
    ("technology", "The new processor improves computer performance."),
    ("technology", "Machine learning models process datasets."),
    ("business", "The company reported higher revenue and profit."),
    ("business", "Investors reacted to the earnings report.")
]
texts = [x[1] for x in samples]
labels = [x[0] for x in samples]
model = make_pipeline(TfidfVectorizer(), LinearSVC()).fit(texts, labels)

out = Path("classified_documents")
for i, text in enumerate(texts, 1):
    label = model.predict([text])[0]
    folder = out / label
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f"document_{i}.txt").write_text(text, encoding="utf-8")
    print(f"Document {i} -> {label}")
print("Separated files saved in:", out.resolve())
