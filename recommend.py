import pandas as pd

# Step 1: Load CSV file
songs = pd.read_csv("songs.csv")

# ✅ Add these lines to check what’s inside your CSV
print("Columns found in CSV:", songs.columns)
print(songs.head())

# Step 2: Take user input for mood or artist
print("🎵 Welcome to Music Recommender 🎶")
choice = input("Enter a mood or artist name: ").strip().lower()

# Step 3: Filter based on user input
recommendations = songs[
    (songs['Mood'].str.lower() == choice) |
    (songs['Artist'].str.lower().str.contains(choice))
]

# Step 4: Show results
if not recommendations.empty:
    print("\n🎧 Recommended Songs:")
    for index, row in recommendations.iterrows():
        print(f"- {row['Song']} by {row['Artist']} [{row['Genre']}]")
else:
    print("❌ No songs found for that mood or artist.")
