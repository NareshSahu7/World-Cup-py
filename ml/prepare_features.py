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
# PATHS
# ---------------------------------------------------------

INPUT_FILE = os.path.join(
    PROJECT_ROOT,
    "data",
    "matches.csv"
)

OUTPUT_FILE = os.path.join(
    PROJECT_ROOT,
    "data",
    "ml_features.csv"
)


# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------

def load_match_data():

    if not os.path.exists(INPUT_FILE):

        print("❌ matches.csv not found.")

        print(
            "Run process_world_cup_data.py first."
        )

        return pd.DataFrame()

    return pd.read_csv(
        INPUT_FILE
    )


# ---------------------------------------------------------
# CREATE TEAM STATISTICS
# ---------------------------------------------------------

def calculate_team_statistics(df):

    teams = set(
        df["team_1"].dropna()
    ).union(
        set(df["team_2"].dropna())
    )

    statistics = {}

    for team in teams:

        matches = (
            (df["team_1"] == team)
            |
            (df["team_2"] == team)
        )

        team_matches = df[matches]

        wins = (
            team_matches["winner"]
            == team
        ).sum()

        total_matches = len(
            team_matches
        )

        win_percentage = 0

        if total_matches > 0:

            win_percentage = (
                wins
                / total_matches
                * 100
            )

        statistics[team] = {
            "matches": total_matches,
            "wins": int(wins),
            "win_percentage": round(
                win_percentage,
                2
            )
        }

    return statistics


# ---------------------------------------------------------
# CREATE ML FEATURES
# ---------------------------------------------------------

def create_features(df):

    if df.empty:
        return pd.DataFrame()

    statistics = calculate_team_statistics(
        df
    )

    records = []

    for _, row in df.iterrows():

        team_1 = row["team_1"]

        team_2 = row["team_2"]

        winner = row["winner"]

        if (
            pd.isna(team_1)
            or pd.isna(team_2)
            or pd.isna(winner)
        ):
            continue

        if team_1 not in statistics:
            continue

        if team_2 not in statistics:
            continue

        team_1_stats = statistics[
            team_1
        ]

        team_2_stats = statistics[
            team_2
        ]

        # Target:
        # 1 = team 1 won
        # 0 = team 2 won

        if winner == team_1:

            target = 1

        elif winner == team_2:

            target = 0

        else:

            continue

        records.append({

            "team_1_matches":
                team_1_stats["matches"],

            "team_1_wins":
                team_1_stats["wins"],

            "team_1_win_percentage":
                team_1_stats["win_percentage"],

            "team_2_matches":
                team_2_stats["matches"],

            "team_2_wins":
                team_2_stats["wins"],

            "team_2_win_percentage":
                team_2_stats["win_percentage"],

            "win_percentage_difference":
                (
                    team_1_stats["win_percentage"]
                    -
                    team_2_stats["win_percentage"]
                ),

            "target":
                target
        })

    return pd.DataFrame(
        records
    )


# ---------------------------------------------------------
# SAVE FEATURES
# ---------------------------------------------------------

def save_features(df):

    if df.empty:

        print(
            "❌ No ML features generated."
        )

        return

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"✅ ML features saved to: "
        f"{OUTPUT_FILE}"
    )

    print(
        f"📊 Total ML records: {len(df)}"
    )


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

def main():

    print("\n")
    print("=" * 70)
    print("ICC WORLD CUP - ML FEATURE PREPARATION")
    print("=" * 70)

    df = load_match_data()

    if df.empty:
        return

    features = create_features(
        df
    )

    save_features(
        features
    )

    print("\n🎉 Feature preparation completed.")


if __name__ == "__main__":

    main()
