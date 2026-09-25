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
# LOAD BATTING DATA
# ---------------------------------------------------------

def load_batting_data():

    file_path = os.path.join(
        PROJECT_ROOT,
        "data",
        "batting.csv"
    )

    if not os.path.exists(file_path):
        print("❌ batting.csv not found.")
        print("Run process_world_cup_data.py first.")
        return pd.DataFrame()

    df = pd.read_csv(file_path)

    print(
        f"✅ Batting data loaded: {len(df)} records"
    )

    return df


# ---------------------------------------------------------
# PLAYER RUNS
# ---------------------------------------------------------

def player_runs(df):

    if df.empty:
        return pd.DataFrame()

    result = (
        df.groupby("batter")["batter_runs"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    result.columns = [
        "player",
        "total_runs"
    ]

    return result


# ---------------------------------------------------------
# PLAYER BALLS
# ---------------------------------------------------------

def player_balls(df):

    if df.empty:
        return pd.DataFrame()

    result = (
        df.groupby("batter")
        .size()
        .reset_index(name="balls_faced")
    )

    result.columns = [
        "player",
        "balls_faced"
    ]

    return result


# ---------------------------------------------------------
# PLAYER STRIKE RATE
# ---------------------------------------------------------

def player_strike_rate(df):

    if df.empty:
        return pd.DataFrame()

    runs = player_runs(df)

    balls = player_balls(df)

    result = pd.merge(
        runs,
        balls,
        on="player",
        how="left"
    )

    result["strike_rate"] = (
        result["total_runs"]
        / result["balls_faced"]
        * 100
    ).round(2)

    result = result.sort_values(
        "total_runs",
        ascending=False
    )

    return result


# ---------------------------------------------------------
# TOP BATTERS
# ---------------------------------------------------------

def top_batters(df, number=10):

    result = player_strike_rate(df)

    if result.empty:
        return result

    return result.head(number)


# ---------------------------------------------------------
# DISPLAY ANALYSIS
# ---------------------------------------------------------

def display_player_analysis(df):

    if df.empty:
        print("❌ No batting data available.")
        return

    print("\n")
    print("=" * 70)
    print("ICC WORLD CUP - PLAYER BATTING ANALYSIS")
    print("=" * 70)

    result = player_strike_rate(df)

    print("\n🏏 TOP BATTERS")
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

    df = load_batting_data()

    if df.empty:
        return

    display_player_analysis(df)


if __name__ == "__main__":
    main()
