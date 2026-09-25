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
    """
    Load World Cup match data from CSV.
    """

    file_path = os.path.join(
        PROJECT_ROOT,
        "data",
        "matches.csv"
    )

    if not os.path.exists(file_path):
        print("❌ matches.csv not found.")
        print("Run process_world_cup_data.py first.")
        return pd.DataFrame()

    df = pd.read_csv(file_path)

    print(f"✅ Match data loaded: {len(df)} records")

    return df


# ---------------------------------------------------------
# TEAM MATCH COUNT
# ---------------------------------------------------------

def team_match_count(df):
    """
    Count how many matches each team played.
    """

    if df.empty:
        return pd.DataFrame()

    team_1 = df["team_1"].value_counts()
    team_2 = df["team_2"].value_counts()

    total_matches = (
        team_1.add(
            team_2,
            fill_value=0
        )
    )

    result = (
        total_matches
        .astype(int)
        .sort_values(
            ascending=False
        )
        .reset_index()
    )

    result.columns = [
        "team",
        "matches_played"
    ]

    return result


# ---------------------------------------------------------
# TEAM WINS
# ---------------------------------------------------------

def team_wins(df):
    """
    Calculate total wins for every team.
    """

    if df.empty:
        return pd.DataFrame()

    wins = (
        df["winner"]
        .dropna()
        .value_counts()
        .reset_index()
    )

    wins.columns = [
        "team",
        "wins"
    ]

    return wins


# ---------------------------------------------------------
# TEAM WIN PERCENTAGE
# ---------------------------------------------------------

def team_win_percentage(df):
    """
    Calculate matches played, wins and win percentage.
    """

    if df.empty:
        return pd.DataFrame()

    matches = team_match_count(df)
    wins = team_wins(df)

    result = pd.merge(
        matches,
        wins,
        on="team",
        how="left"
    )

    result["wins"] = (
        result["wins"]
        .fillna(0)
        .astype(int)
    )

    result["win_percentage"] = (
        result["wins"]
        / result["matches_played"]
        * 100
    ).round(2)

    result = result.sort_values(
        "win_percentage",
        ascending=False
    )

    return result


# ---------------------------------------------------------
# DISPLAY TEAM ANALYSIS
# ---------------------------------------------------------

def display_team_analysis(df):
    """
    Display important team statistics.
    """

    if df.empty:
        print("❌ No match data available.")
        return

    print("\n")
    print("=" * 70)
    print("ICC MEN'S CRICKET WORLD CUP - TEAM ANALYSIS")
    print("=" * 70)

    # Matches played
    print("\n🏏 MATCHES PLAYED")
    print("-" * 70)

    matches = team_match_count(df)

    print(
        matches.to_string(
            index=False
        )
    )

    # Wins
    print("\n🏆 TOTAL WINS")
    print("-" * 70)

    wins = team_wins(df)

    print(
        wins.to_string(
            index=False
        )
    )

    # Win percentage
    print("\n📊 WIN PERCENTAGE")
    print("-" * 70)

    percentage = team_win_percentage(df)

    print(
        percentage.to_string(
            index=False
        )
    )

    print("\n" + "=" * 70)


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

def main():

    df = load_match_data()

    if df.empty:
        return

    display_team_analysis(df)


if __name__ == "__main__":
    main()
