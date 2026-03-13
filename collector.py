import os
import pandas as pd
from fetch_news import fetch_news


def collect_news():

    file_path = "data/raw_news.csv"

    os.makedirs("data", exist_ok=True)

    df = fetch_news()

    # stop if API returned nothing
    if df is None or df.empty:
        print("No new data fetched. Skipping update.")
        return

    if os.path.exists(file_path):

        old_df = pd.read_csv(file_path)

        # combine old + new data
        combined = pd.concat([old_df, df], ignore_index=True)

        # remove duplicates using url
        if "url" in combined.columns:
            combined = combined.drop_duplicates(subset="url")

        # convert datetime safely
        combined["publishedAt"] = pd.to_datetime(
            combined["publishedAt"], format="mixed", errors="coerce"
        )

        # remove rows with invalid dates
        combined = combined.dropna(subset=["publishedAt"])

        # sort newest first
        combined = combined.sort_values("publishedAt", ascending=False)

        # keep only latest 2000 articles
        combined = combined.head(2000)

        # reset index
        combined = combined.reset_index(drop=True)

        # save dataset
        combined.to_csv(file_path, index=False)

        print("Total stored articles:", len(combined))

    else:

        # first dataset creation
        df["publishedAt"] = pd.to_datetime(
            df["publishedAt"], format="mixed", errors="coerce"
        )

        df = df.dropna(subset=["publishedAt"])

        df.to_csv(file_path, index=False)

        print("Dataset created:", len(df))