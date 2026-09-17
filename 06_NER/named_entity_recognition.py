
# Program 6: Named Entity Recognition (NER) using spaCy

import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = """
Aditya is studying B.Tech in Computer Science at NIET in Greater Noida.
He visited New Delhi in August 2026.
"""

# Process the text using spaCy
doc = nlp(text)

# Display the original text
print("========== ORIGINAL TEXT ==========")
print(text)

# Display named entities
print("========== NAMED ENTITIES ==========")

for entity in doc.ents:
    print(f"Entity: {entity.text}")
    print(f"Label: {entity.label_}")
    print(f"Description: {spacy.explain(entity.label_)}")
    print("-" * 40)
