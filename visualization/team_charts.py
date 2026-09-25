import os
import sys

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ---------------------------------------------------------
# PROJECT ROOT
# ---------------------------------------------------------

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


# ---------------------------------------------------------
# PATHS
# ---------------------------------------------------------

DATA_FILE = os.path.join(
    PROJECT_ROOT,
    "data",
    "matches.csv"
)

CHART_FOLDER = os.path.join(
    PROJECT_ROOT,
    "visualization",
    "charts"
)


# ---------------------------------------------------------
# CREATE CHART FOLDER
# ---------------------------------------------------------

def create_chart_folder():

    os.makedirs(
        CHART_FOLDER,
        exist_ok=True
    )


# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------

def load_match_data():

    if not os.path.exists(DATA_FILE):

        print("❌ matches.csv not found.")

        print(
            "Run process_world_cup_data.py first."
        )

        return pd.DataFrame()

    df = pd.read_csv(
        DATA_FILE
    )

    print(
        f"✅ Match data loaded: {len(df)} records"
    )

    return df


# ---------------------------------------------------------
# TEAM MATCHES PLAYED
# ---------------------------------------------------------

def create_matches_played_chart(df):

    if df.empty:
        return

    team_1 = df["team_1"].value_counts()

    team_2 = df["team_2"].value_counts()

    matches = team_1.add(
        team_2,
        fill_value=0
    )

    matches = (
        matches
        .sort_values(
            ascending=False
        )
        .reset_index()
    )

    matches.columns = [
        "team",
        "matches"
    ]

    plt.figure(
        figsize=(12, 7)
    )

    sns.barplot(
        data=matches,
        x="matches",
        y="team"
    )

    plt.title(
        "ICC Men's Cricket World Cup - Matches Played"
    )

    plt.xlabel(
        "Matches Played"
    )

    plt.ylabel(
        "Team"
    )

    plt.tight_layout()

    output_path = os.path.join(
        CHART_FOLDER,
        "team_matches_played.png"
    )

    plt.savefig(
        output_path,
        dpi=300
    )

    plt.close()

    print(
        f"📊 Chart saved: {output_path}"
    )


# ---------------------------------------------------------
# TEAM WINS
# ---------------------------------------------------------

def create_team_wins_chart(df):

    if df.empty:
        return

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

    plt.figure(
        figsize=(12, 7)
    )

    sns.barplot(
        data=wins,
        x="wins",
        y="team"
    )

    plt.title(
        "ICC Men's Cricket World Cup - Team Wins"
    )

    plt.xlabel(
        "Total Wins"
    )

    plt.ylabel(
        "Team"
    )

    plt.tight_layout()

    output_path = os.path.join(
        CHART_FOLDER,
        "team_wins.png"
    )

    plt.savefig(
        output_path,
        dpi=300
    )

    plt.close()

    print(
        f"📊 Chart saved: {output_path}"
    )


# ---------------------------------------------------------
# WIN PERCENTAGE
# ---------------------------------------------------------

def create_win_percentage_chart(df):

    if df.empty:
        return

    team_1 = df["team_1"].value_counts()

    team_2 = df["team_2"].value_counts()

    matches = team_1.add(
        team_2,
        fill_value=0
    )

    wins = (
        df["winner"]
        .dropna()
        .value_counts()
    )

    result = pd.DataFrame({
        "matches": matches,
        "wins": wins
    })

    result = result.fillna(0)

    result["win_percentage"] = (
        result["wins"]
        / result["matches"]
        * 100
    )

    result = (
        result
        .sort_values(
            "win_percentage",
            ascending=False
        )
        .reset_index()
    )

    result.columns = [
        "team",
        "matches",
        "wins",
        "win_percentage"
    ]

    plt.figure(
        figsize=(12, 7)
    )

    sns.barplot(
        data=result,
        x="win_percentage",
        y="team"
    )

    plt.title(
        "ICC Men's Cricket World Cup - Team Win Percentage"
    )

    plt.xlabel(
        "Win Percentage (%)"
    )

    plt.ylabel(
        "Team"
    )

    plt.xlim(
        0,
        100
    )

    plt.tight_layout()

    output_path = os.path.join(
        CHART_FOLDER,
        "team_win_percentage.png"
    )

    plt.savefig(
        output_path,
        dpi=300
    )

    plt.close()

    print(
        f"📊 Chart saved: {output_path}"
    )


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

def main():

    print("\n")
    print("=" * 70)
    print("ICC WORLD CUP - TEAM VISUALIZATION")
    print("=" * 70)

    create_chart_folder()

    df = load_match_data()

    if df.empty:
        return

    print("\n📊 Creating charts...")

    create_matches_played_chart(
        df
    )

    create_team_wins_chart(
        df
    )

    create_win_percentage_chart(
        df
    )

    print("\n" + "=" * 70)
    print("🎉 ALL TEAM CHARTS CREATED")
    print("=" * 70)


# ---------------------------------------------------------
# RUN PROGRAM
# ---------------------------------------------------------

if __name__ == "__main__":

    main()
