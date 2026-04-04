import pandas as pd
from datetime import datetime

# Load dataset
data = pd.read_csv("algorithm/final_dataset.csv")


def get_crowd():
    hour = datetime.now().hour

    if 8 <= hour <= 11 or 17 <= hour <= 21:
        return "high"
    elif 12 <= hour <= 16:
        return "medium"
    else:
        return "low"


def crowd_penalty(c):
    if c == "high":
        return 1
    elif c == "medium":
        return 3
    else:
        return 5


def safety_score(row):
    crowd = get_crowd()

    score = row["crime_rate"] * 2
    score += crowd_penalty(crowd)

    return score


def get_safety_scores():
    scores = {}

    for _, row in data.iterrows():
        scores[row["area"]] = safety_score(row)

    return scores


if __name__ == "__main__":
    print(get_safety_scores())
