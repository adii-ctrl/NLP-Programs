from transformers import pipeline

ner = pipeline("token-classification", model="dslim/bert-base-NER",
               aggregation_strategy="simple")
text = "Satya Nadella works at Microsoft in the United States."
for entity in ner(text):
    print(entity["word"], entity["entity_group"], round(float(entity["score"]), 3))
