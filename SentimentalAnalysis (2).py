def sentiment_analysis(text):
    
    positive_words = ["good", "happy", "love", "excellent", "great", "excellent", "victory"]
    negative_words = ["bad", "sad", "hate", "terrible", "poor", "fail", "loser","damage"]

    words = text.lower().split()
    
    pos_count = sum(1 for word in words if word in positive_words)
    neg_count = sum(1 for word in words if word in negative_words)
    
    if pos_count > neg_count:
        return "Positive"
    elif pos_count < neg_count:
        return "Negative"
    else:
        return "Neutral"

text = input("Enter your statement: ")
print("Statement is:", sentiment_analysis(text))

