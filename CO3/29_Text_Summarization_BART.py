from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
text = """
Natural language processing is a field of artificial intelligence. It enables
computers to process human language and includes classification, translation,
summarization, sentiment analysis and question answering. Transformer models
are trained on large text collections and support many of these applications.
"""
print(summarizer(text, max_length=55, min_length=15, do_sample=False)[0]["summary_text"])
