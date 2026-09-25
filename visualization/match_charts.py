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

def load_match_data():

    if not os.path.exists(DATA_FILE):

        print("❌ matches.csv not found.")

        return pd.DataFrame()

    df = pd.read_csv(
        DATA_FILE
    )

    print(
        f"✅ Match data loaded: {len(df)} records"
    )

    return df


# ---------------------------------------------------------
# MATCHES BY SEASON
# ---------------------------------------------------------

def create_season_chart(df):

    if df.empty:
        return

    season = (
        df.groupby("season")
        .size()
        .reset_index(
            name="matches"
        )
    )

    season["season"] = (
        season["season"]
        .astype(str)
    )

    plt.figure(
        figsize=(12, 7)
    )

    sns.barplot(
        data=season,
        x="season",
        y="matches"
    )

    plt.title(
        "ICC Men's Cricket World Cup Matches by Season"
    )

    plt.xlabel(
        "Season"
    )

    plt.ylabel(
        "Number of Matches"
    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()

    output_path = os.path.join(
        CHART_FOLDER,
        "matches_by_season.png"
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
# RESULT TYPES
# ---------------------------------------------------------

def create_result_type_chart(df):

    if df.empty:
        return

    results = (
        df["result_type"]
        .fillna("Unknown")
        .value_counts()
        .reset_index()
    )

    results.columns = [
        "result_type",
        "matches"
    ]

    plt.figure(
        figsize=(10, 6)
    )

    sns.barplot(
        data=results,
        x="result_type",
        y="matches"
    )

    plt.title(
        "World Cup Match Result Types"
    )

    plt.xlabel(
        "Result Type"
    )

    plt.ylabel(
        "Number of Matches"
    )

    plt.xticks(
        rotation=30
    )

    plt.tight_layout()

    output_path = os.path.join(
        CHART_FOLDER,
        "match_result_types.png"
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
# TOSS DECISION
# ---------------------------------------------------------

def create_toss_chart(df):

    if df.empty:
        return

    toss = (
        df["toss_decision"]
        .fillna("Unknown")
        .value_counts()
        .reset_index()
    )

    toss.columns = [
        "decision",
        "matches"
    ]

    plt.figure(
        figsize=(10, 6)
    )

    sns.barplot(
        data=toss,
        x="decision",
        y="matches"
    )

    plt.title(
        "Toss Decisions in World Cup Matches"
    )

    plt.xlabel(
        "Toss Decision"
    )

    plt.ylabel(
        "Number of Matches"
    )

    plt.tight_layout()

    output_path = os.path.join(
        CHART_FOLDER,
        "toss_decisions.png"
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
    print("ICC WORLD CUP - MATCH VISUALIZATION")
    print("=" * 70)

    create_chart_folder()

    df = load_match_data()

    if df.empty:
        return

    create_season_chart(
        df
    )

    create_result_type_chart(
        df
    )

    create_toss_chart(
        df
    )

    print("\n🎉 Match charts created.")


if __name__ == "__main__":

    main()
