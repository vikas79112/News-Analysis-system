import pandas as pd
import matplotlib.pyplot as plt


def analyze_trends(df):

    df["publishedAt"] = pd.to_datetime(df["publishedAt"])

    df["date"] = df["publishedAt"].dt.date

    # articles per day
    articles_per_day = df.groupby("date").size()

    print("\nArticles per day:\n")
    print(articles_per_day)

    ax = articles_per_day.plot(kind="line", marker="o")

    plt.title("News Volume Trend")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")

    plt.tight_layout()
    plt.show()


    # sentiment trend
    sentiment_trend = df.groupby(["date","sentiment"]).size().unstack()

    print("\nSentiment trend:\n")
    print(sentiment_trend)

    sentiment_trend.plot(kind="line", marker="o")

    plt.title("Sentiment Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")

    plt.tight_layout()
    plt.show()