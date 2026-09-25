import os
import sys


# ---------------------------------------------------------
# PROJECT ROOT
# ---------------------------------------------------------

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


# ---------------------------------------------------------
# IMPORT VISUALIZATION MODULES
# ---------------------------------------------------------

from visualization.team_charts import (
    load_match_data,
    create_chart_folder,
    create_matches_played_chart,
    create_team_wins_chart,
    create_win_percentage_chart
)

from visualization.player_charts import (
    load_batting_data,
    create_top_run_scorers_chart,
    create_strike_rate_chart
)

from visualization.bowling_charts import (
    load_bowling_data,
    create_top_wicket_takers_chart,
    create_runs_conceded_chart
)

from visualization.match_charts import (
    create_season_chart,
    create_result_type_chart,
    create_toss_chart
)

from visualization.statistical_charts import (
    create_run_distribution,
    create_wicket_distribution,
    create_player_comparison
)


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

def main():

    print("\n")
    print("=" * 70)
    print("ICC MEN'S CRICKET WORLD CUP")
    print("COMPLETE VISUALIZATION SYSTEM")
    print("=" * 70)

    # Create chart folder
    create_chart_folder()

    # -----------------------------------------------------
    # TEAM CHARTS
    # -----------------------------------------------------

    print("\n🏏 Creating team charts...")

    match_data = load_match_data()

    if not match_data.empty:

        create_matches_played_chart(
            match_data
        )

        create_team_wins_chart(
            match_data
        )

        create_win_percentage_chart(
            match_data
        )

    # -----------------------------------------------------
    # PLAYER CHARTS
    # -----------------------------------------------------

    print("\n🏏 Creating player charts...")

    batting_data = load_batting_data()

    if not batting_data.empty:

        create_top_run_scorers_chart(
            batting_data
        )

        create_strike_rate_chart(
            batting_data
        )

        create_run_distribution(
            batting_data
        )

        create_player_comparison(
            batting_data
        )

    # -----------------------------------------------------
    # BOWLING CHARTS
    # -----------------------------------------------------

    print("\n🎯 Creating bowling charts...")

    bowling_data = load_bowling_data()

    if not bowling_data.empty:

        create_top_wicket_takers_chart(
            bowling_data
        )

        create_runs_conceded_chart(
            bowling_data
        )

        create_wicket_distribution(
            bowling_data
        )

    # -----------------------------------------------------
    # MATCH CHARTS
    # -----------------------------------------------------

    print("\n📊 Creating match charts...")

    if not match_data.empty:

        create_season_chart(
            match_data
        )

        create_result_type_chart(
            match_data
        )

        create_toss_chart(
            match_data
        )

    # -----------------------------------------------------
    # COMPLETED
    # -----------------------------------------------------

    print("\n")
    print("=" * 70)
    print("🎉 ALL VISUALIZATIONS CREATED SUCCESSFULLY")
    print("=" * 70)

    print("\n📁 Charts are available in:")

    print(
        "visualization/charts/"
    )

    print("\n")


# ---------------------------------------------------------
# RUN
# ---------------------------------------------------------

if __name__ == "__main__":

    main()
