# GloVe stores one word and its vector on each line.
# Example file format:
# king 0.123 0.456 0.789 ...

GLOVE_FILE = "glove_sample.txt"

try:
    embeddings = {}

    with open(GLOVE_FILE, "r", encoding="utf-8") as file:
        for line in file:
            values = line.strip().split()
            word = values[0]
            vector = [float(x) for x in values[1:]]
            embeddings[word] = vector

    word = "king"

    if word in embeddings:
        print("Vector for", word, ":")
        print(embeddings[word])
    else:
        print("Word not found in GloVe file.")

except FileNotFoundError:
    print(f"{GLOVE_FILE} not found.")
    print("Place a GloVe text file in the same folder and update GLOVE_FILE if needed.")
