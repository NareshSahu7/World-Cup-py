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

def load_bowling_data():

    if not os.path.exists(DATA_FILE):

        print("❌ bowling.csv not found.")

        return pd.DataFrame()

    df = pd.read_csv(
        DATA_FILE
    )

    print(
        f"✅ Bowling data loaded: {len(df)} records"
    )

    return df


# ---------------------------------------------------------
# TOP WICKET TAKERS
# ---------------------------------------------------------

def create_top_wicket_takers_chart(
    df,
    top_n=10
):

    if df.empty:
        return

    wickets = (
        df.groupby("bowler")["wickets"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(top_n)
        .reset_index()
    )

    wickets.columns = [
        "player",
        "wickets"
    ]

    plt.figure(
        figsize=(12, 7)
    )

    sns.barplot(
        data=wickets,
        x="wickets",
        y="player"
    )

    plt.title(
        "Top Wicket Takers - ICC Men's Cricket World Cup"
    )

    plt.xlabel(
        "Wickets"
    )

    plt.ylabel(
        "Bowler"
    )

    plt.tight_layout()

    output_path = os.path.join(
        CHART_FOLDER,
        "top_wicket_takers.png"
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
# RUNS CONCEDED
# ---------------------------------------------------------

def create_runs_conceded_chart(
    df,
    top_n=10
):

    if df.empty:
        return

    runs = (
        df.groupby("bowler")["runs_conceded"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(top_n)
        .reset_index()
    )

    runs.columns = [
        "player",
        "runs_conceded"
    ]

    plt.figure(
        figsize=(12, 7)
    )

    sns.barplot(
        data=runs,
        x="runs_conceded",
        y="player"
    )

    plt.title(
        "Runs Conceded by Top Bowlers"
    )

    plt.xlabel(
        "Runs Conceded"
    )

    plt.ylabel(
        "Bowler"
    )

    plt.tight_layout()

    output_path = os.path.join(
        CHART_FOLDER,
        "runs_conceded.png"
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
    print("ICC WORLD CUP - BOWLING VISUALIZATION")
    print("=" * 70)

    create_chart_folder()

    df = load_bowling_data()

    if df.empty:
        return

    create_top_wicket_takers_chart(
        df
    )

    create_runs_conceded_chart(
        df
    )

    print("\n🎉 Bowling charts created.")


if __name__ == "__main__":

    main()
