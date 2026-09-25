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
# LOAD MATCH DATA
# ---------------------------------------------------------

def load_match_data():

    file_path = os.path.join(
        PROJECT_ROOT,
        "data",
        "matches.csv"
    )

    if not os.path.exists(file_path):
        print("❌ matches.csv not found.")
        return pd.DataFrame()

    return pd.read_csv(file_path)


# ---------------------------------------------------------
# YEAR / SEASON ANALYSIS
# ---------------------------------------------------------

def season_analysis(df):

    if df.empty:
        return pd.DataFrame()

    result = (
        df.groupby("season")
        .size()
        .reset_index(
            name="matches"
        )
    )

    return result.sort_values(
        "season"
    )


# ---------------------------------------------------------
# VENUE ANALYSIS
# ---------------------------------------------------------

def venue_analysis(df):

    if df.empty:
        return pd.DataFrame()

    result = (
        df.groupby("venue")
        .size()
        .sort_values(
            ascending=False
        )
        .reset_index(
            name="matches"
        )
    )

    return result


# ---------------------------------------------------------
# WINNING MARGIN ANALYSIS
# ---------------------------------------------------------

def margin_analysis(df):

    if df.empty:
        return pd.DataFrame()

    result = (
        df.groupby("result_type")
        .size()
        .reset_index(
            name="matches"
        )
    )

    return result


# ---------------------------------------------------------
# TOSS ANALYSIS
# ---------------------------------------------------------

def toss_analysis(df):

    if df.empty:
        return pd.DataFrame()

    valid_data = df[
        df["toss_winner"].notna()
    ]

    result = (
        valid_data["toss_decision"]
        .value_counts()
        .reset_index()
    )

    result.columns = [
        "toss_decision",
        "count"
    ]

    return result


# ---------------------------------------------------------
# DISPLAY
# ---------------------------------------------------------

def display_match_analysis(df):

    if df.empty:
        print("❌ No match data available.")
        return

    print("\n")
    print("=" * 70)
    print("ICC WORLD CUP - MATCH ANALYSIS")
    print("=" * 70)

    print("\n📅 MATCHES BY SEASON")
    print("-" * 70)

    print(
        season_analysis(df).to_string(
            index=False
        )
    )

    print("\n🏟️ MATCHES BY VENUE")
    print("-" * 70)

    print(
        venue_analysis(df).head(15).to_string(
            index=False
        )
    )

    print("\n🏆 RESULT TYPES")
    print("-" * 70)

    print(
        margin_analysis(df).to_string(
            index=False
        )
    )

    print("\n🪙 TOSS DECISIONS")
    print("-" * 70)

    print(
        toss_analysis(df).to_string(
            index=False
        )
    )

    print("\n" + "=" * 70)


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

def main():

    df = load_match_data()

    display_match_analysis(df)


if __name__ == "__main__":
    main()
