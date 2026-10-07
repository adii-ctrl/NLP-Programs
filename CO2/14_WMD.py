from gensim.models import Word2Vec

# Small custom corpus for demonstration.
sentences = [
    ["dog", "animal", "pet"],
    ["cat", "animal", "pet"],
    ["dog", "runs", "fast"],
    ["cat", "runs", "slow"],
    ["car", "vehicle", "road"],
    ["bus", "vehicle", "road"]
]

model = Word2Vec(
    sentences,
    vector_size=50,
    window=2,
    min_count=1,
    workers=1
)

document1 = ["dog", "is", "an", "animal", "pet"]
document2 = ["cat", "is", "an", "animal", "pet"]

# Keep only words known to the model.
doc1 = [word for word in document1 if word in model.wv]
doc2 = [word for word in document2 if word in model.wv]

try:
    distance = model.wv.wmdistance(doc1, doc2)
    print("Word Mover's Distance:", distance)
except Exception as e:
    print("WMD could not be calculated.")
    print("Install the required WMD dependency if necessary:", e)
