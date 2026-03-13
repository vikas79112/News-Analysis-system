import pandas as pd
from collector import collect_news
from preprocess import preprocess_data
from sentiment import analyze_sentiment
from analysis import analyze_news
from topics import extract_topics
from trends import analyze_trends


# Step 1: fetch latest news
collect_news()

# Step 2: preprocessing
clean_df = preprocess_data()

# Step 3: sentiment analysis
sentiment_df = analyze_sentiment(clean_df)

# Step 4: statistical analysis
analyze_news(sentiment_df)

# Step 5: topic extraction
top_topics = extract_topics(sentiment_df)

print("\nTrending News Topics:\n")

for phrase, score in top_topics:
    print(phrase)

# Step 6: trend analysis
analyze_trends(sentiment_df)

print("\nArticles after cleaning:", len(clean_df))