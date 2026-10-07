from textblob import TextBlob

reviews = [
    "The phone has an excellent camera and great battery life.",
    "The display is beautiful but the battery is disappointing.",
    "The performance is fast and the design is amazing.",
    "The product is poor and the quality is bad."
]

for review in reviews:
    polarity = TextBlob(review).sentiment.polarity

    if polarity > 0:
        opinion = "Positive"
    elif polarity < 0:
        opinion = "Negative"
    else:
        opinion = "Neutral"

    print("\nReview:", review)
    print("Polarity:", polarity)
    print("Opinion:", opinion)
