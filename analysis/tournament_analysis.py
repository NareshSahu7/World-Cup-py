import os
import sys
import pandas as pd


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


from config import MATCHES_FILE


def load_matches():
    """
    Load World Cup match data.
    """

    if not os.path.exists(MATCHES_FILE):

        print(
            f"❌ File not found: {MATCHES_FILE}"
        )

        return pd.DataFrame()

    df = pd.read_csv(
        MATCHES_FILE
    )

    return df


def analyze_tournaments():
    """
    Perform tournament and season-level analysis.
    """

    df = load_matches()

    if df.empty:

        print(
            "❌ No match data available."
        )

        return

    print("\n")
    print("=" * 60)
    print("TOURNAMENT ANALYSIS")
    print("=" * 60)

    # --------------------------------------------------------
    # Matches by season
    # --------------------------------------------------------

    if "season" in df.columns:

        print("\n========== MATCHES BY SEASON ==========")

        season_matches = (
            df.groupby("season")
            .size()
            .reset_index(
                name="matches"
            )
            .sort_values(
                "season"
            )
        )

        print(
            season_matches.to_string(
                index=False
            )
        )

    # --------------------------------------------------------
    # Wins by team
    # --------------------------------------------------------

    if "winner" in df.columns:

        print("\n========== TOURNAMENT WINS ==========")

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

        print(
            wins.to_string(
                index=False
            )
        )

    # --------------------------------------------------------
    # Venues
    # --------------------------------------------------------

    if "venue" in df.columns:

        print("\n========== TOP VENUES ==========")

        venues = (
            df["venue"]
            .dropna()
            .value_counts()
            .head(10)
            .reset_index()
        )

        venues.columns = [
            "venue",
            "matches"
        ]

        print(
            venues.to_string(
                index=False
            )
        )

    # --------------------------------------------------------
    # Match result types
    # --------------------------------------------------------

    if "result_type" in df.columns:

        print(
            "\n========== RESULT TYPES =========="
        )

        results = (
            df["result_type"]
            .fillna("Unknown")
            .value_counts()
        )

        print(results)

    # --------------------------------------------------------
    # Toss decisions
    # --------------------------------------------------------

    if "toss_decision" in df.columns:

        print(
            "\n========== TOSS DECISIONS =========="
        )

        toss = (
            df["toss_decision"]
            .dropna()
            .value_counts()
        )

        print(toss)

    print(
        "\n🎉 Tournament analysis completed."
    )


if __name__ == "__main__":
    analyze_tournaments()
