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
