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

BAT_IN_FILE = os.path.join(
    PROJECT_ROOT,
    "data",
    "batting.csv"
)

BOWL_IN_FILE = os.path.join(
    PROJECT_ROOT,
    "data",
    "bowling.csv"
)

CHART_FOLDER = os.path.join(
    PROJECT_ROOT,
    "visualization",
    "charts"
)


# ---------------------------------------------------------
# CREATE FOLDER
# ---------------------------------------------------------

def create_chart_folder():

    os.makedirs(
        CHART_FOLDER,
        exist_ok=True
    )


# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------

def load_batting_data():

    if not os.path.exists(BAT_IN_FILE):
        return pd.DataFrame()

    return pd.read_csv(
        BAT_IN_FILE
    )


def load_bowling_data():

    if not os.path.exists(BOWL_IN_FILE):
        return pd.DataFrame()

    return pd.read_csv(
        BOWL_IN_FILE
    )


# ---------------------------------------------------------
# RUN DISTRIBUTION
# ---------------------------------------------------------

def create_run_distribution(df):

    if df.empty:
        return

    plt.figure(
        figsize=(10, 6)
    )

    sns.histplot(
        data=df,
        x="batter_runs",
        bins=10
    )

    plt.title(
        "Distribution of Runs Scored per Delivery"
    )

    plt.xlabel(
        "Runs Scored"
    )

    plt.ylabel(
        "Number of Deliveries"
    )

    plt.tight_layout()

    output_path = os.path.join(
        CHART_FOLDER,
        "run_distribution.png"
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
# WICKET DISTRIBUTION
# ---------------------------------------------------------

def create_wicket_distribution(df):

    if df.empty:
        return

    wicket_counts = (
        df["wickets"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    wicket_counts.columns = [
        "wickets",
        "deliveries"
    ]

    plt.figure(
        figsize=(10, 6)
    )

    sns.barplot(
        data=wicket_counts,
        x="wickets",
        y="deliveries"
    )

    plt.title(
        "Wicket Distribution per Delivery"
    )

    plt.xlabel(
        "Wickets"
    )

    plt.ylabel(
        "Number of Deliveries"
    )

    plt.tight_layout()

    output_path = os.path.join(
        CHART_FOLDER,
        "wicket_distribution.png"
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
# TOP PLAYER COMPARISON
# ---------------------------------------------------------

def create_player_comparison(df):

    if df.empty:
        return

    player_data = (
        df.groupby("batter")["batter_runs"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(10)
        .reset_index()
    )

    player_data.columns = [
        "player",
        "runs"
    ]

    plt.figure(
        figsize=(12, 7)
    )

    sns.barplot(
        data=player_data,
        x="runs",
        y="player"
    )

    plt.title(
        "Top 10 Players by Total Runs"
    )

    plt.xlabel(
        "Total Runs"
    )

    plt.ylabel(
        "Player"
    )

    plt.tight_layout()

    output_path = os.path.join(
        CHART_FOLDER,
        "top_10_player_comparison.png"
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
    print("ICC WORLD CUP - STATISTICAL VISUALIZATION")
    print("=" * 70)

    create_chart_folder()

    batting = load_batting_data()

    bowling = load_bowling_data()

    create_run_distribution(
        batting
    )

    create_wicket_distribution(
        bowling
    )

    create_player_comparison(
        batting
    )

    print("\n🎉 Statistical charts created.")


if __name__ == "__main__":

    main()
