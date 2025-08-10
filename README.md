# Task 05 – Using LLMs for Sports Data Analysis

## 📘 Objective
This project tests how well a Large Language Model (LLM) can answer natural language questions based on structured sports data. The dataset used is the Syracuse Men's Basketball 2023–24 season statistics.

## 📊 Dataset
- **Name:** Syracuse Men's Basketball Stats 2023–24
- **Source:** Team statistics PDF (cleaned into `basketball_2023_clean.csv`)
- **Note:** Dataset is local and excluded from GitHub.

## ✅ Work Done (First Reporting Period)
- Cleaned dataset from PDF and structured it as CSV
- Created Python validation script to compute ground-truth answers
- Designed and stored natural language prompts for testing
- Asked LLM questions and saved responses
- Compared answers to actual stats and recorded evaluation results

## 🔍 Initial Observations
- LLM answered factual questions correctly (scorer, rebounds, 3PT%)
- Performed reasonably on “all-around” player analysis
- Struggled with subjective strategy questions (offense vs. defense)

## 📂 Repo Structure
Task_05_Descriptive_Stats/
├── data/ (local only)
├── prompts/ (text prompts used for testing)
├── results/ (llm_responses and evaluation.csv)
├── scripts/ (validation Python script)
├── README.md
└── .gitignore

## ⏭️ Next Steps
- Refine prompt engineering to improve complex answers
- Try multiple LLMs (ChatGPT, Claude) for comparison
- Expand metrics for evaluating subjective responses

# Task 05 – Using LLMs for Sports Data Analysis (Second Reporting Period)  

## 📘 Objective  
This project continues testing how well a Large Language Model (LLM) can answer natural language questions based on structured sports data.  
The dataset used is the Syracuse Men's Basketball 2023–24 season statistics, now with **additional derived metrics** to enable more complex analysis.  

---

## 📊 Dataset  
- **Name:** Syracuse Men's Basketball Stats 2023–24 (Round 2)  
- **Source:** Team statistics PDF (cleaned into `basketball_2023_clean.csv`)  
- **Enhancements in Round 2:**  
  - Added `Rebounds_per_game`  
  - Added `Impact` score (Points + Rebounds + Assists + Steals + Blocks)  
  - Added `FG_3PT_gap` (difference between FG% and 3PT%)  
  - Added points-per-game deviation from team average  
- **Note:** Dataset is local and excluded from GitHub.  

---

## ✅ Work Done (Second Reporting Period)  
- Expanded dataset with **calculated metrics** to support complex LLM queries  
- Created new Python validation script (`validate_stats_round2.py`) to compute extended metrics  
- Designed and stored **updated simple and complex prompts** for testing  
- Queried LLM with the updated dataset and **saved separate responses** for simple and complex questions  
- Prepared structured dataset for LLM ingestion (`prepare_llm_dataset_round2.py`)  
- Saved Round 2 outputs to `basketball_2023_analysis_round2.csv`  

---

## 🔍 Key Observations in Round 2  
- LLM continued to answer factual questions (top scorer, best 3PT%, most rebounds) with high accuracy  
- Additional metrics allowed for more nuanced queries (e.g., most efficient rebounder, largest FG% vs 3PT% gap)  
- LLM handled ranking and filtering tasks better when metrics were pre-calculated in the dataset  
- Some ambiguity remained for subjective “recommendation” style questions  

---

## 📂 Repo Structure  
Task_05_Descriptive_Stats/
├── data/ (local CSVs and prompts for LLM input)
├── prompts/ (simple & complex prompts for Round 2)
├── results/ (LLM responses for simple & complex questions)
├── scripts/ (Python scripts for validation & dataset preparation)
├── commands_round2.ipynb (Jupyter commands for Round 2)
├── README.md
└── .gitignore

---

## ⏭️ Next Steps  
- Evaluate and score LLM responses against ground truth for Round 2  
- Compare performance across different LLM models  
- Prepare for **Round 3** with a potential “AI Street Interview” narrative format of findings  
