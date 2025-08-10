import pandas as pd
from pathlib import Path

csv_path = Path("data/basketball_2023_clean.csv")
df = pd.read_csv(csv_path)

print("Players:", len(df))
print("Columns:", df.columns.tolist())

# ---------- SIMPLE ----------
top_scorer = df.loc[df['PTS'].idxmax()]
print("\nTop Scorer:", top_scorer['Player'], "-", top_scorer['PTS'], "points")

best_3pt = df.loc[df['3PT%'].idxmax()]
print("Best 3PT%:", best_3pt['Player'], "-", best_3pt['3PT%'])

most_rebounds = df.loc[df['Rebounds'].idxmax()]
print("Most Rebounds:", most_rebounds['Player'], "-", most_rebounds['Rebounds'])

# ---------- HELPERS ----------
def left_gp(gp_gs):
    try:
        return int(str(gp_gs).split("-")[0])
    except:
        return pd.NA

# From Task 04 table we had FG-FGA and FT-FTA but our cleaned table doesn’t include them.
# So we will compute only with columns present.
# If you later add FG-FGA or FT-FTA, you can extend these metrics.

# ---------- COMPLEX (ROUND 2) ----------
# 1) Efficient rebounder = Rebounds / GP
df["GP"] = df["GP-GS"].apply(left_gp)
df["Rebounds_per_game"] = df["Rebounds"] / df["GP"]
reb_eff = df.loc[df["Rebounds_per_game"].idxmax()]
print("\nMost efficient rebounder (REB/GP):", reb_eff["Player"], "-", round(reb_eff["Rebounds_per_game"], 2))

# 2) Impact = PTS + Rebounds + Assists + Steals + Blocks
df["Impact"] = df["PTS"] + df["Rebounds"] + df["Assists"] + df["Steals"] + df["Blocks"]
impact_leader = df.loc[df["Impact"].idxmax()]
print("Highest Impact:", impact_leader["Player"], "-", impact_leader["Impact"])

# 3) Team AVG PPG
team_avg_ppg = df["AVG"].mean()
ppg_above_team = df.iloc[(df["AVG"] - team_avg_ppg).abs().idxmax()]  # furthest from mean
top_above = df.loc[(df["AVG"] - team_avg_ppg).idxmax()]
print("Team average PPG:", round(team_avg_ppg, 2))
print("Highest PPG above team average:", top_above["Player"], "-", round(top_above["AVG"] - team_avg_ppg, 2))

# 4) Gap between FG% and 3PT% (absolute)
df["FG_3PT_gap"] = (df["FG%"] - df["3PT%"]).abs()
gap_leader = df.loc[df["FG_3PT_gap"].idxmax()]
print("Largest FG% vs 3PT% gap:", gap_leader["Player"], "-", round(gap_leader["FG_3PT_gap"], 3))

# Save the computed metrics
out_csv = Path("data/basketball_2023_analysis_round2.csv")
df.to_csv(out_csv, index=False)
print(f"\n✅ Saved extended metrics to {out_csv.resolve()}")

