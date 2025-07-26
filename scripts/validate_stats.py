import pandas as pd

df = pd.read_csv("data/basketball_2023_clean.csv")

print("Players:", len(df))
print("Columns:", df.columns.tolist())

# Top Scorer
top_scorer = df.loc[df['PTS'].idxmax()]
print("\nTop Scorer:", top_scorer['Player'], "-", top_scorer['PTS'], "points")

# Best 3PT%
best_3pt = df.loc[df['3PT%'].idxmax()]
print("Best 3PT%:", best_3pt['Player'], "-", best_3pt['3PT%'])

# Most Rebounds
most_rebounds = df.loc[df['Rebounds'].idxmax()]
print("Most Rebounds:", most_rebounds['Player'], "-", most_rebounds['Rebounds'])
