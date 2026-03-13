
# Real-Time News Intelligence System

An end-to-end news analytics pipeline that collects news articles from external APIs, performs NLP analysis, and visualizes insights through an interactive dashboard.

The system analyzes hundreds of news articles to identify sentiment, trending topics, major sources, and news volume trends over time.

---

## Features

- Automated news collection using NewsAPI
- Sentiment analysis of news articles
- Topic extraction using TF-IDF (NLP)
- Trend analysis of news volume over time
- Interactive dashboard for exploring insights
- Filtering by topic and source
- Incremental dataset updates with duplicate removal

---

## Dashboard Preview

The dashboard visualizes:

- Total articles collected
- Sentiment distribution
- News volume trend over time
- Top news sources
- Trending news topics
- Latest articles table

Built using Streamlit and Plotly for interactive visualization.

---

## Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Plotly
- NewsAPI
- Requests
- Python-dotenv

---

## Project Architecture

```

NewsAPI
↓
collector.py (data ingestion)
↓
dataset stored in CSV
↓
preprocessing & NLP analysis
↓
Streamlit dashboard visualization

```

The dashboard reads the dataset locally to avoid excessive API calls.

---

## Project Structure

```

real-time-news-analysis
│
├── app.py
├── main.py
├── collector.py
├── fetch_news.py
├── preprocess.py
├── sentiment.py
├── analysis.py
├── topics.py
├── trends.py
│
├── requirements.txt
├── README.md
├── .gitignore
│
├── data
│   └── raw_news.csv

````

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/news-intelligence-dashboard.git
cd news-intelligence-dashboard
````

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file and add your NewsAPI key:

```
NEWS_API_KEY=your_api_key_here
```

---

## Collect News Data

Run the collector to fetch news articles:

```bash
python collector.py
```

This updates the dataset stored in `data/raw_news.csv`.

---

## Run the Dashboard

Start the Streamlit dashboard:

```bash
streamlit run app.py
```

The dashboard will open in your browser.

---

## Example Insights

The system can reveal insights such as:

* Sudden spikes in news volume
* Most active news sources
* Trending topics like global conflicts or sports events
* Sentiment trends across news coverage

---

## Future Improvements

* Breaking news spike detection
* Topic trend tracking over time
* Scheduled data ingestion
* Advanced NLP topic modeling

---

## License

This project is for educational and portfolio purposes.

````

---

