import pandas as pd

data = pd.read_csv("algorithm/safety_data.csv")


def lighting_penalty(l):

    if l == "low":
        return 5
    elif l == "medium":
        return 2
    else:
        return 0


def crowd_penalty(c):

    if c == "low":
        return 4
    elif c == "medium":
        return 2
    else:
        return 0


def safety_score(row):

    score = 0

    score += row["crime_rate"] * 2
    score += lighting_penalty(row["lighting"])
    score += crowd_penalty(row["crowd"])

    return score


def get_safety_scores():

    scores = {}

    for i, row in data.iterrows():
        scores[row["area"]] = safety_score(row)

    return scores


if __name__ == "__main__":
    print(get_safety_scores())
