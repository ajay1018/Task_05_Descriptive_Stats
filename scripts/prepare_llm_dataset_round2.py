import pandas as pd
from pathlib import Path

# Load latest analysis data
df = pd.read_csv("data/basketball_2023_analysis_round2.csv")

# Convert the DataFrame into a plain-text table for LLM ingestion
table_str = df.to_csv(index=False)

# Add instructions + dataset
prompt = f"""
You are given the Syracuse Men's Basketball 2023-24 season player statistics.
The table includes both raw stats and derived metrics from previous analysis.

Dataset:
{table_str}

Your job is to answer user questions about this dataset, whether simple (e.g., top scorer) or complex (e.g., most efficient rebounder).

Answer only based on the dataset above. 
If information is not available, clearly state that it is not present.
"""

# Save the prepared prompt
out_file = Path("data/llm_prompt_round2.txt")
out_file.write_text(prompt)
print(f"✅ LLM-ready dataset saved to {out_file.resolve()}")
