import spacy

# Educational baseline: links common pronouns to the most recent PERSON entity.
# This is not a full neural coreference resolver.
nlp = spacy.load("en_core_web_sm")
text = "Riya bought a book. She read it at home."
doc = nlp(text)
last_person = None

for token in doc:
    if token.ent_type_ == "PERSON":
        last_person = token.text
    if token.lower_ in {"he", "she", "they"} and last_person:
        print(f"Possible coreference: {token.text} -> {last_person}")

print("Note: this simple baseline will not resolve every pronoun.")
