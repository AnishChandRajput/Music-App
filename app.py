from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load song data
songs = pd.read_csv("songs.csv")

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []
    if request.method == "POST":
        query = request.form["query"].strip().lower()

        # Filter songs by mood, artist, or song name
        recommendations = songs[
            (songs['Mood'].str.lower() == query) |
            (songs['Artist'].str.lower().str.contains(query)) |
            (songs['Song'].str.lower().str.contains(query))
        ].to_dict(orient="records")

    return render_template("index.html", songs=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
