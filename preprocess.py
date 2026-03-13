import pandas as pd


def preprocess_data():

    file_path = "data/raw_news.csv"

    df = pd.read_csv(file_path)

    # remove rows with missing titles
    df = df.dropna(subset=["title"])

    # remove duplicates using url
    if "url" in df.columns:
        df = df.drop_duplicates(subset="url")

    # remove noisy sources
    bad_sources = [
        "Pypi.org",
        "Slashdot.org",
        "Madshrimps.be"
    ]

    df = df[~df["source"].isin(bad_sources)]

    # fill missing description
    df["description"] = df["description"].fillna("")

    # combine title + description for NLP
    df["content"] = df["title"] + " " + df["description"]

    # reset index
    df = df.reset_index(drop=True)

    print("\nArticles after cleaning:", len(df))

    return df