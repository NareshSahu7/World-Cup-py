import os
import sys
import pandas as pd


# ---------------------------------------------------------
# PROJECT ROOT
# ---------------------------------------------------------

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


# ---------------------------------------------------------
# LOAD BOWLING DATA
# ---------------------------------------------------------

def load_bowling_data():

    file_path = os.path.join(
        PROJECT_ROOT,
        "data",
        "bowling.csv"
    )

    if not os.path.exists(file_path):
        print("❌ bowling.csv not found.")
        print("Run process_world_cup_data.py first.")
        return pd.DataFrame()

    df = pd.read_csv(file_path)

    print(
        f"✅ Bowling data loaded: {len(df)} records"
    )

    return df


# ---------------------------------------------------------
# TOTAL WICKETS
# ---------------------------------------------------------

def player_wickets(df):

    if df.empty:
        return pd.DataFrame()

    result = (
        df.groupby("bowler")["wickets"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    result.columns = [
        "player",
        "wickets"
    ]

    return result


# ---------------------------------------------------------
# TOTAL RUNS CONCEDED
# ---------------------------------------------------------

def player_runs_conceded(df):

    if df.empty:
        return pd.DataFrame()

    result = (
        df.groupby("bowler")["runs_conceded"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    result.columns = [
        "player",
        "runs_conceded"
    ]

    return result


# ---------------------------------------------------------
# BOWLING SUMMARY
# ---------------------------------------------------------

def bowling_summary(df):

    if df.empty:
        return pd.DataFrame()

    wickets = player_wickets(df)

    runs = player_runs_conceded(df)

    result = pd.merge(
        wickets,
        runs,
        on="player",
        how="outer"
    )

    result = result.fillna(0)

    result["wickets"] = (
        result["wickets"]
        .astype(int)
    )

    result["runs_conceded"] = (
        result["runs_conceded"]
        .astype(int)
    )

    result = result.sort_values(
        "wickets",
        ascending=False
    )

    return result


# ---------------------------------------------------------
# TOP BOWLERS
# ---------------------------------------------------------

def top_bowlers(df, number=10):

    result = bowling_summary(df)

    if result.empty:
        return result

    return result.head(number)


# ---------------------------------------------------------
# DISPLAY ANALYSIS
# ---------------------------------------------------------

def display_bowling_analysis(df):

    if df.empty:
        print("❌ No bowling data available.")
        return

    print("\n")
    print("=" * 70)
    print("ICC WORLD CUP - BOWLING ANALYSIS")
    print("=" * 70)

    result = bowling_summary(df)

    print("\n🎯 TOP BOWLERS")
    print("-" * 70)

    print(
        result.head(10).to_string(
            index=False
        )
    )

    print("\n" + "=" * 70)


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

def main():

    df = load_bowling_data()

    if df.empty:
        return

    display_bowling_analysis(df)


if __name__ == "__main__":
    main()
