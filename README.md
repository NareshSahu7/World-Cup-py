# 🏏 ICC Men's Cricket World Cup Data Analysis & Machine Learning

A Python-based data analysis and machine learning project using ICC Men's Cricket World Cup data.

The project downloads cricket match data, processes it into structured datasets, stores data in Firebase Firestore, performs statistical analysis, creates visualizations, and prepares machine learning models.

---

# 📌 Project Objectives

The main objectives of this project are:

- Collect ICC Men's Cricket World Cup data.
- Process raw cricket JSON data.
- Create structured CSV datasets.
- Store cricket data in Firebase Firestore.
- Analyze teams and players.
- Analyze batting performance.
- Analyze bowling performance.
- Analyze match results.
- Analyze tournament statistics.
- Generate charts and visualizations.
- Build machine learning models.
- Compare different machine learning algorithms.
- Create an interactive Streamlit dashboard.

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Firebase Firestore
- Firebase Admin SDK
- Joblib
- Streamlit
- Jupyter Notebook
- GitHub

---

# 📂 Project Structure

```text
World-Cup-py/
│
├── main.py
├── config.py
├── utils.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── data/
│   ├── download_world_cup_data.py
│   ├── process_world_cup_data.py
│   └── raw/
│
├── firebase/
│   ├── firebase_config.py
│   ├── upload_data.py
│   ├── fetch_data.py
│   ├── upload_all_data.py
│   ├── test_connection.py
│   └── delete_data.py
│
├── analysis/
│   ├── __init__.py
│   ├── team_analysis.py
│   ├── player_analysis.py
│   ├── bowling_analysis.py
│   ├── match_analysis.py
│   ├── statistics.py
│   └── tournament_analysis.py
│
├── visualization/
│   ├── __init__.py
│   ├── team_charts.py
│   ├── player_charts.py
│   ├── bowling_charts.py
│   ├── match_charts.py
│   ├── statistical_charts.py
│   ├── run_all_charts.py
│   └── dashboard.py
│
└── ml/
    ├── __init__.py
    ├── prepare_features.py
    ├── train_model.py
    ├── predict_match.py
    ├── evaluate_model.py
    └── model_comparison.py
