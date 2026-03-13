import streamlit as st
import pandas as pd
import plotly.express as px

from preprocess import preprocess_data
from sentiment import analyze_sentiment
from topics import extract_topics


st.set_page_config(page_title="News Intelligence Dashboard", layout="wide")

st.title("Real-Time News Intelligence Dashboard")
st.caption("News analysis with sentiment, topic extraction, and trend monitoring")

# Load dataset
df = preprocess_data()
df = analyze_sentiment(df)

# Convert time
df["publishedAt"] = pd.to_datetime(df["publishedAt"])
df["date"] = df["publishedAt"].dt.date


# -------------------------
# Sidebar Filters
# -------------------------

st.sidebar.header("Filters")

topic_filter = st.sidebar.selectbox(
    "Topic",
    ["All"] + sorted(df["topic"].dropna().unique())
)

source_filter = st.sidebar.selectbox(
    "Source",
    ["All"] + sorted(df["source"].dropna().unique())
)

if topic_filter != "All":
    df = df[df["topic"] == topic_filter]

if source_filter != "All":
    df = df[df["source"] == source_filter]


# -------------------------
# KPI Metrics
# -------------------------

# col1, col2, col3, col4 = st.columns(4)

# col1.metric("Total Articles", len(df))
# col2.metric("Sources", df["source"].nunique())
# col3.metric("Topics", df["topic"].nunique())
# col4.metric(
#     "Positive Sentiment %",
#     round((df["sentiment"] == "positive").mean() * 100, 1)
# )


# -------------------------
# News Trend
# -------------------------

st.subheader("News Volume Over Time")

trend = df.groupby("date").size().reset_index(name="articles")

fig_trend = px.line(
    trend,
    x="date",
    y="articles",
    markers=True,
    title="Articles Published Per Day"
)

st.plotly_chart(fig_trend, use_container_width=True)


# -------------------------
# Sentiment Distribution
# -------------------------

st.subheader("Sentiment Distribution")

sentiment_counts = df["sentiment"].value_counts().reset_index()
sentiment_counts.columns = ["sentiment", "count"]

fig_sentiment = px.bar(
    sentiment_counts,
    x="sentiment",
    y="count",
    color="sentiment",
    title="Sentiment Distribution"
)

st.plotly_chart(fig_sentiment, use_container_width=True)


# -------------------------
# Top Sources
# -------------------------

st.subheader("Top News Sources")

top_sources = df["source"].value_counts().head(10).reset_index()
top_sources.columns = ["source", "count"]

fig_sources = px.bar(
    top_sources,
    x="source",
    y="count",
    title="Top News Sources"
)

st.plotly_chart(fig_sources, use_container_width=True)


# -------------------------
# Trending Topics
# -------------------------

st.subheader("Trending Topics")

topics = extract_topics(df)

for phrase, score in topics:
    st.write(f"• {phrase}")


# -------------------------
# Latest Articles
# -------------------------

st.subheader("Latest Articles")

latest = df.sort_values("publishedAt", ascending=False)

st.dataframe(
    latest[["publishedAt", "title", "source", "topic"]].head(20),
    use_container_width=True
)