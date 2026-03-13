import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("NEWS_API_KEY")


def fetch_news():

    url = "https://newsapi.org/v2/everything"

    queries = {
        "technology": "AI OR technology OR software OR cybersecurity OR semiconductor",
        "business": "business OR startup OR economy OR finance OR stock market",
        "health": "health OR medicine OR disease OR vaccine",
        "science": "science OR research OR space",
        "sports": "sports OR football OR cricket OR olympics"
    }

    news_list = []

    for topic, query in queries.items():

        params = {
            "q": query,
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": 100,
            "searchIn": "title",
            "apiKey": API_KEY
        }

        try:
            response = requests.get(url, params=params, timeout=10)
        except requests.exceptions.RequestException as e:
            print("News API request failed:", e)
            continue

        if response.status_code != 200:
            print("Request failed:", response.status_code)
            continue

        data = response.json()

        if data.get("status") != "ok":
            print("API error:", data)
            continue

        articles = data.get("articles", [])

        for article in articles:

            news_list.append({
                "title": article.get("title"),
                "description": article.get("description"),
                "source": article["source"]["name"] if article.get("source") else None,
                "publishedAt": article.get("publishedAt"),
                "url": article.get("url"),
                "topic": topic
            })

    if not news_list:
        return None

    df = pd.DataFrame(news_list)

    return df