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
    "batting.csv"
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

    if not os.path.exists(DATA_FILE):

        print("❌ batting.csv not found.")

        print(
            "Run process_world_cup_data.py first."
        )

        return pd.DataFrame()

    df = pd.read_csv(
        DATA_FILE
    )

    print(
        f"✅ Batting data loaded: {len(df)} records"
    )

    return df


# ---------------------------------------------------------
# TOP RUN SCORERS
# ---------------------------------------------------------

def create_top_run_scorers_chart(
    df,
    top_n=10
):

    if df.empty:
        return

    runs = (
        df.groupby("batter")["batter_runs"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(top_n)
        .reset_index()
    )

    runs.columns = [
        "player",
        "runs"
    ]

    plt.figure(
        figsize=(12, 7)
    )

    sns.barplot(
        data=runs,
        x="runs",
        y="player"
    )

    plt.title(
        "Top Run Scorers - ICC Men's Cricket World Cup"
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
        "top_run_scorers.png"
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
# PLAYER STRIKE RATE
# ---------------------------------------------------------

def create_strike_rate_chart(
    df,
    top_n=10
):

    if df.empty:
        return

    player_data = (
        df.groupby("batter")
        .agg(
            runs=(
                "batter_runs",
                "sum"
            ),
            balls=(
                "batter",
                "count"
            )
        )
        .reset_index()
    )

    player_data["strike_rate"] = (
        player_data["runs"]
        / player_data["balls"]
        * 100
    )

    player_data = (
        player_data
        .sort_values(
            "runs",
            ascending=False
        )
        .head(top_n)
    )

    plt.figure(
        figsize=(12, 7)
    )

    sns.barplot(
        data=player_data,
        x="strike_rate",
        y="batter"
    )

    plt.title(
        "Strike Rate of Top Run Scorers"
    )

    plt.xlabel(
        "Strike Rate"
    )

    plt.ylabel(
        "Player"
    )

    plt.tight_layout()

    output_path = os.path.join(
        CHART_FOLDER,
        "player_strike_rate.png"
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
    print("ICC WORLD CUP - PLAYER VISUALIZATION")
    print("=" * 70)

    create_chart_folder()

    df = load_batting_data()

    if df.empty:
        return

    create_top_run_scorers_chart(
        df
    )

    create_strike_rate_chart(
        df
    )

    print("\n🎉 Player charts created.")


if __name__ == "__main__":

    main()
