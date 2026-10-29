from transformers import MarianMTModel, MarianTokenizer

name = "Helsinki-NLP/opus-mt-en-fr"
tokenizer = MarianTokenizer.from_pretrained(name)
model = MarianMTModel.from_pretrained(name)
sentences = ["Hello, how are you?", "Natural language processing is interesting."]
batch = tokenizer(sentences, return_tensors="pt", padding=True, truncation=True)
outputs = model.generate(**batch, max_new_tokens=80)
for source, translated in zip(sentences, tokenizer.batch_decode(outputs, skip_special_tokens=True)):
    print("English:", source)
    print("French:", translated)
