from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

text = "I really love this product. It is excellent and useful."

# TextBlob
blob = TextBlob(text)
print("TextBlob polarity:", blob.sentiment.polarity)
print("TextBlob subjectivity:", blob.sentiment.subjectivity)

# VADER
analyzer = SentimentIntensityAnalyzer()
scores = analyzer.polarity_scores(text)

print("\nVADER scores:")
print(scores)

if scores["compound"] >= 0.05:
    print("Sentiment: Positive")
elif scores["compound"] <= -0.05:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")
