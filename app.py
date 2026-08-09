from flask import Flask, render_template, request
from database.db import connection, cursor
from recommendation.recommendation import recommend_places

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():

    category = request.form["category"]
    budget = request.form["budget"]
    days = request.form["days"]

    # Save search history
    query = """
    INSERT INTO search_history(destination, category)
    VALUES (?, ?)
    """

    values = ("AI Recommendation", category)

    cursor.execute(query, values)
    connection.commit()

    # Get AI recommendations
    places = recommend_places(category, budget)

    print(places)

    return render_template(
        "result.html",
        destination="AI Recommendation",
        category=category,
        budget=budget,
        days=days,
        places=places
    )


if __name__ == "__main__":
    app.run(debug=True)