import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from database.db import connection


def load_places():

    query = "SELECT * FROM places"

    df = pd.read_sql(query, connection)

    return df


def recommend_places(category, budget):

    df = load_places()

    # Make sure text columns don't contain NULL values
    df["category"] = df["category"].fillna("")
    df["description"] = df["description"].fillna("")

    # Combine category and description for AI similarity
    df["combined"] = (
        df["category"] + " " + df["description"]
    )

    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform(df["combined"])

    similarity = cosine_similarity(vectors)

    # Filter according to user's preferences
    filtered = df[
        (df["category"].str.lower() == category.lower())
        &
        (df["average_cost"] <= int(budget))
    ]

    if filtered.empty:
        return []

    # Use the first matching destination as the recommendation reference
    index = filtered.index[0]

    scores = list(enumerate(similarity[index]))

    # Highest similarity first
    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for i, score in scores:

        place = df.iloc[i]

        if (
            place["category"].lower() == category.lower()
            and place["average_cost"] <= int(budget)
        ):

            # Convert Pandas Series → normal Python dictionary
            place_data = place.to_dict()

            # Add AI similarity score
            place_data["match_score"] = round(
                score * 100,
                1
            )

            recommendations.append(place_data)

        if len(recommendations) == 5:
            break

    return recommendations