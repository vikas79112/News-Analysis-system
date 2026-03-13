from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


def extract_topics(df, n_topics=10):

    custom_stopwords = {
        "new","million","announced","launch","latest",
        "says","report","company","year","years",
        "design","deal","technology","framework","pr"
    }

    weak_words = {
        "complete","pretty","series","support",
        "people","leaving","leader","global"
    }

    date_words = {
        "january","february","march","april","may","june",
        "july","august","september","october","november","december"
    }

    stop_words = list(
        ENGLISH_STOP_WORDS
        .union(custom_stopwords)
        .union(weak_words)
    )

    # use cleaned text column
    text_data = df["content"].fillna("")

    vectorizer = TfidfVectorizer(
        stop_words=stop_words,
        ngram_range=(2,3),
        max_features=1000,
        min_df=2
    )

    tfidf_matrix = vectorizer.fit_transform(text_data)

    feature_names = vectorizer.get_feature_names_out()

    scores = tfidf_matrix.sum(axis=0).A1

    word_scores = list(zip(feature_names, scores))

    sorted_words = sorted(word_scores, key=lambda x: x[1], reverse=True)

    filtered_topics = []

    for phrase, score in sorted_words:

        words = phrase.split()

        if any(word in date_words for word in words):
            continue

        filtered_topics.append((phrase, score))

        if len(filtered_topics) == n_topics:
            break

    return filtered_topics