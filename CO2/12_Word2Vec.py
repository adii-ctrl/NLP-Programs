from gensim.models import Word2Vec

sentences = [
    ["natural", "language", "processing", "is", "interesting"],
    ["machine", "learning", "is", "useful"],
    ["natural", "language", "processing", "uses", "text"],
    ["machine", "learning", "uses", "data"]
]

model = Word2Vec(
    sentences,
    vector_size=50,
    window=3,
    min_count=1,
    workers=1
)

word = "language"

print("Vector for:", word)
print(model.wv[word])

print("\nWords similar to", word)
print(model.wv.most_similar(word, topn=3))
