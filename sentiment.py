from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(df):

    sentiments = []
    
    for text in df["content"]:
        score = analyzer.polarity_scores(text)
        compound = score["compound"]

        if compound >= 0.05:
            sentiments.append("positive")
        elif compound <= -0.05:
            sentiments.append("negative")
        else:
            sentiments.append("neutral")

    df["sentiment"] = sentiments

    return df