# I predict the phrase trump will appear most often

import glob
import json
import matplotlib.pyplot as plt

json_files = sorted(glob.glob("master_*.json"))
all_tweets = []

for file_path in json_files:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        all_tweets.extend(data)

total_tweets = len(all_tweets)
print(f"Total tweets loaded: {total_tweets}")

PHRASES = [
    "obama",
    "trump",
    "mexico",
    "russia",
    "fake news",
    "maga",
    "jobs",
    "border security",
]

phrase_counts = {phrase: 0 for phrase in PHRASES}

for tweet in all_tweets:
    text = tweet.get("full_text") or tweet.get("text") or ""
    text_lower = text.lower()

    for phrase in PHRASES:
        if phrase in text_lower:
            phrase_counts[phrase] += 1


print("\n Benchmark Check")
print(f"Trump count: {phrase_counts['trump']} (Expected: 13659)")
print(f"Obama count: {phrase_counts['obama']} (Expected: 2738)")

markdown_rows = []
print("\nMarkdown Table Output")
print("| phrase | percent of tweets |")
print("| " + "-" * 17 + " | " + "-" * 17 + " |")

for phrase in PHRASES:
    count = phrase_counts[phrase]
    percentage = (count / total_tweets) * 100 if total_tweets > 0 else 0.0
    pct_str = f"{percentage:05.2f}"

    row_str = f"| {phrase:>17} | {pct_str:>17} |"
    print(row_str)
    markdown_rows.append(row_str)

percentages = [(phrase_counts[p] / total_tweets) * 100 for p in PHRASES]

plt.figure(figsize=(10, 6))
bars = plt.barh(
    [p.title() for p in PHRASES],
    percentages,
    color="skyblue",
    edgecolor="navy",
)
plt.xlabel("Percentage of Total Tweets (%)", fontsize=12)
plt.ylabel("Search Phrase", fontsize=12)
plt.title("Keyword Frequency in Tweet Archive (2009–2018)", fontsize=14)
plt.gca().invert_yaxis()  

for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 0.3,
        bar.get_y() + bar.get_height() / 2,
        f"{width:05.2f}%",
        va="center",
        fontsize=10,
    )

plt.tight_layout()
plt.savefig("tweets.png", dpi=300)
print("\nSaved visualization to 'tweets.png'.")
