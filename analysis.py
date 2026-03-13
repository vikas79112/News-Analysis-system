import pandas as pd
import matplotlib.pyplot as plt

def analyze_news(df):

    # -------- Sentiment Distribution --------
    sentiment_counts = df["sentiment"].value_counts()

    print("\nSentiment distribution:\n")
    print(sentiment_counts)

    ax = sentiment_counts.plot(kind="bar")

    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Articles")

    # add numbers on bars
    for i, value in enumerate(sentiment_counts):
        ax.text(i, value + 1, str(value), ha='center')

    plt.show()


    # -------- Top News Sources --------
    source_counts = df["source"].value_counts().head(10)

    print("\nTop news sources:\n")
    print(source_counts)

    ax = source_counts.plot(kind="bar")

    plt.title("Top News Sources")
    plt.xlabel("Source")
    plt.ylabel("Number of Articles")

    plt.xticks(rotation=45)

    # add numbers on bars
    for i, value in enumerate(source_counts):
        ax.text(i, value + 1, str(value), ha='center')
    plt.tight_layout()
    plt.show()