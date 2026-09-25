import os
import sys
import pandas as pd
import numpy as np


# ---------------------------------------------------------
# PROJECT ROOT
# ---------------------------------------------------------

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------

def load_matches():

    path = os.path.join(
        PROJECT_ROOT,
        "data",
        "matches.csv"
    )

    if not os.path.exists(path):
        return pd.DataFrame()

    return pd.read_csv(path)


def load_batting():

    path = os.path.join(
        PROJECT_ROOT,
        "data",
        "batting.csv"
    )

    if not os.path.exists(path):
        return pd.DataFrame()

    return pd.read_csv(path)


def load_bowling():

    path = os.path.join(
        PROJECT_ROOT,
        "data",
        "bowling.csv"
    )

    if not os.path.exists(path):
        return pd.DataFrame()

    return pd.read_csv(path)


# ---------------------------------------------------------
# BASIC DATASET STATISTICS
# ---------------------------------------------------------

def dataset_statistics(df):

    if df.empty:
        return {}

    statistics = {
        "records": len(df),
        "columns": len(df.columns),
        "missing_values": int(
            df.isnull().sum().sum()
        )
    }

    return statistics


# ---------------------------------------------------------
# BATTING STATISTICS
# ---------------------------------------------------------

def batting_statistics(df):

    if df.empty:
        return {}

    runs = df["batter_runs"]

    statistics = {
        "total_runs": int(
            runs.sum()
        ),
        "average_runs_per_delivery": round(
            runs.mean(),
            2
        ),
        "maximum_runs_in_delivery": int(
            runs.max()
        ),
        "minimum_runs_in_delivery": int(
            runs.min()
        )
    }

    return statistics


# ---------------------------------------------------------
# BOWLING STATISTICS
# ---------------------------------------------------------

def bowling_statistics(df):

    if df.empty:
        return {}

    statistics = {
        "total_wickets": int(
            df["wickets"].sum()
        ),
        "total_runs_conceded": int(
            df["runs_conceded"].sum()
        ),
        "average_runs_conceded": round(
            df["runs_conceded"].mean(),
            2
        )
    }

    return statistics


# ---------------------------------------------------------
# DISPLAY STATISTICS
# ---------------------------------------------------------

def display_statistics():

    matches = load_matches()
    batting = load_batting()
    bowling = load_bowling()

    print("\n")
    print("=" * 70)
    print("ICC WORLD CUP - STATISTICAL SUMMARY")
    print("=" * 70)

    print("\n📊 MATCH DATA")

    match_stats = dataset_statistics(
        matches
    )

    for key, value in match_stats.items():

        print(
            f"{key}: {value}"
        )

    print("\n🏏 BATTING DATA")

    batting_stats = batting_statistics(
        batting
    )

    for key, value in batting_stats.items():

        print(
            f"{key}: {value}"
        )

    print("\n🎯 BOWLING DATA")

    bowling_stats = bowling_statistics(
        bowling
    )

    for key, value in bowling_stats.items():

        print(
            f"{key}: {value}"
        )

    print("\n" + "=" * 70)


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

if __name__ == "__main__":

    display_statistics()
