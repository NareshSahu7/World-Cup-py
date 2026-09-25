import os
import json
import pandas as pd


# ---------------------------------------------------------
# PROJECT PATHS
# ---------------------------------------------------------

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

RAW_FOLDER = os.path.join(
    PROJECT_ROOT,
    "data",
    "raw"
)

OUTPUT_FOLDER = os.path.join(
    PROJECT_ROOT,
    "data"
)


# ---------------------------------------------------------
# HELPER FUNCTIONS
# ---------------------------------------------------------

def get_player_name(player):
    """
    Return a player's name safely.
    """

    if isinstance(player, str):
        return player

    return str(player)


def get_team_name(team):
    """
    Return a team's name safely.
    """

    if isinstance(team, str):
        return team

    return str(team)


# ---------------------------------------------------------
# PROCESS MATCH DATA
# ---------------------------------------------------------

def process_matches():

    matches = []

    print("\n🏏 Processing match data...")

    if not os.path.exists(RAW_FOLDER):
        print("❌ Raw data folder does not exist.")
        print("Run download_world_cup_data.py first.")
        return pd.DataFrame()

    json_files = [
        file
        for file in os.listdir(RAW_FOLDER)
        if file.endswith(".json")
    ]

    print(f"📄 JSON files found: {len(json_files)}")

    for filename in json_files:

        file_path = os.path.join(
            RAW_FOLDER,
            filename
        )

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

            meta = data.get("meta", {})
            info = data.get("info", {})

            teams = info.get(
                "teams",
                []
            )

            dates = info.get(
                "dates",
                []
            )

            event = info.get(
                "event",
                {}
            )

            outcome = info.get(
                "outcome",
                {}
            )

            toss = info.get(
                "toss",
                {}
            )

            venue = info.get(
                "venue",
                ""
            )

            city = info.get(
                "city",
                ""
            )

            match_type = info.get(
                "match_type",
                ""
            )

            gender = info.get(
                "gender",
                ""
            )

            season = info.get(
                "season",
                ""
            )

            # Get winner
            winner = outcome.get(
                "winner",
                ""
            )

            # Get result type
            result_type = ""

            if "winner" in outcome:

                if "by" in outcome:

                    by_data = outcome["by"]

                    if "runs" in by_data:
                        result_type = "Runs"

                    elif "wickets" in by_data:
                        result_type = "Wickets"

            if "result" in outcome:
                result_type = outcome["result"]

            # Toss information
            toss_winner = toss.get(
                "winner",
                ""
            )

            toss_decision = toss.get(
                "decision",
                ""
            )

            # Date
            match_date = ""

            if dates:

                first_date = dates[0]

                match_date = str(
                    first_date
                )

            # Tournament
            tournament_name = event.get(
                "name",
                "ICC Men's Cricket World Cup"
            )

            # Match number
            match_number = event.get(
                "match_number",
                ""
            )

            # Team names
            team_1 = ""

            team_2 = ""

            if len(teams) >= 1:
                team_1 = get_team_name(
                    teams[0]
                )

            if len(teams) >= 2:
                team_2 = get_team_name(
                    teams[1]
                )

            # Result margin
            margin_value = None
            margin_type = ""

            if "by" in outcome:

                by_data = outcome["by"]

                if "runs" in by_data:

                    margin_value = by_data["runs"]
                    margin_type = "Runs"

                elif "wickets" in by_data:

                    margin_value = by_data["wickets"]
                    margin_type = "Wickets"

            matches.append({

                "match_id": filename.replace(
                    ".json",
                    ""
                ),

                "date": match_date,

                "season": season,

                "tournament": tournament_name,

                "match_number": match_number,

                "gender": gender,

                "match_type": match_type,

                "team_1": team_1,

                "team_2": team_2,

                "toss_winner": toss_winner,

                "toss_decision": toss_decision,

                "winner": winner,

                "result_type": result_type,

                "margin": margin_value,

                "margin_type": margin_type,

                "venue": venue,

                "city": city

            })

        except Exception as error:

            print(
                f"⚠️ Could not process "
                f"{filename}: {error}"
            )

    df = pd.DataFrame(matches)

    return df


# ---------------------------------------------------------
# PROCESS BATTING DATA
# ---------------------------------------------------------

def process_batting():

    batting = []

    print("\n🏏 Processing batting data...")

    if not os.path.exists(RAW_FOLDER):
        return pd.DataFrame()

    json_files = [
        file
        for file in os.listdir(RAW_FOLDER)
        if file.endswith(".json")
    ]

    for filename in json_files:

        file_path = os.path.join(
            RAW_FOLDER,
            filename
        )

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

            info = data.get(
                "info",
                {}
            )

            teams = info.get(
                "teams",
                []
            )

            dates = info.get(
                "dates",
                []
            )

            date = ""

            if dates:
                date = str(dates[0])

            innings = data.get(
                "innings",
                []
            )

            for innings_data in innings:

                team = innings_data.get(
                    "team",
                    ""
                )

                overs = innings_data.get(
                    "overs",
                    []
                )

                for over in overs:

                    deliveries = over.get(
                        "deliveries",
                        []
                    )

                    for delivery in deliveries:

                        batter = delivery.get(
                            "batter",
                            ""
                        )

                        bowler = delivery.get(
                            "bowler",
                            ""
                        )

                        runs = delivery.get(
                            "runs",
                            {}
                        )

                        batter_runs = runs.get(
                            "batter",
                            0
                        )

                        extras_runs = runs.get(
                            "extras",
                            0
                        )

                        total_runs = runs.get(
                            "total",
                            0
                        )

                        batting.append({

                            "match_id":
                                filename.replace(
                                    ".json",
                                    ""
                                ),

                            "date": date,

                            "team": team,

                            "batter": batter,

                            "bowler": bowler,

                            "batter_runs":
                                batter_runs,

                            "extras_runs":
                                extras_runs,

                            "total_runs":
                                total_runs

                        })

        except Exception as error:

            print(
                f"⚠️ Could not process "
                f"{filename}: {error}"
            )

    return pd.DataFrame(batting)


# ---------------------------------------------------------
# PROCESS BOWLING DATA
# ---------------------------------------------------------

def process_bowling():

    bowling = []

    print("\n🎯 Processing bowling data...")

    if not os.path.exists(RAW_FOLDER):
        return pd.DataFrame()

    json_files = [
        file
        for file in os.listdir(RAW_FOLDER)
        if file.endswith(".json")
    ]

    for filename in json_files:

        file_path = os.path.join(
            RAW_FOLDER,
            filename
        )

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

            info = data.get(
                "info",
                {}
            )

            dates = info.get(
                "dates",
                []
            )

            date = ""

            if dates:
                date = str(dates[0])

            innings = data.get(
                "innings",
                []
            )

            for innings_data in innings:

                batting_team = innings_data.get(
                    "team",
                    ""
                )

                overs = innings_data.get(
                    "overs",
                    []
                )

                for over in overs:

                    deliveries = over.get(
                        "deliveries",
                        []
                    )

                    for delivery in deliveries:

                        bowler = delivery.get(
                            "bowler",
                            ""
                        )

                        runs = delivery.get(
                            "runs",
                            {}
                        )

                        bowler_runs = runs.get(
                            "total",
                            0
                        )

                        extras = runs.get(
                            "extras",
                            0
                        )

                        wickets = delivery.get(
                            "wickets",
                            []
                        )

                        wicket_count = len(
                            wickets
                        )

                        bowling.append({

                            "match_id":
                                filename.replace(
                                    ".json",
                                    ""
                                ),

                            "date": date,

                            "bowler": bowler,

                            "batting_team":
                                batting_team,

                            "runs_conceded":
                                bowler_runs,

                            "extras":
                                extras,

                            "wickets":
                                wicket_count

                        })

        except Exception as error:

            print(
                f"⚠️ Could not process "
                f"{filename}: {error}"
            )

    return pd.DataFrame(bowling)


# ---------------------------------------------------------
# SAVE DATA
# ---------------------------------------------------------

def save_dataframe(
    dataframe,
    filename
):

    if dataframe.empty:

        print(
            f"⚠️ No data available for "
            f"{filename}"
        )

        return

    output_path = os.path.join(
        OUTPUT_FOLDER,
        filename
    )

    dataframe.to_csv(
        output_path,
        index=False
    )

    print(
        f"💾 Saved {filename} "
        f"({len(dataframe)} records)"
    )


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

def main():

    print("=" * 60)

    print(
        "ICC MEN'S CRICKET WORLD CUP "
        "DATA PROCESSOR"
    )

    print("=" * 60)

    # Process matches
    matches_df = process_matches()

    # Process batting
    batting_df = process_batting()

    # Process bowling
    bowling_df = process_bowling()

    # Save files
    save_dataframe(
        matches_df,
        "matches.csv"
    )

    save_dataframe(
        batting_df,
        "batting.csv"
    )

    save_dataframe(
        bowling_df,
        "bowling.csv"
    )

    print("\n" + "=" * 60)

    print("🎉 DATA PROCESSING COMPLETED")

    print("=" * 60)

    print("\nGenerated files:")

    print("📄 data/matches.csv")
    print("📄 data/batting.csv")
    print("📄 data/bowling.csv")


if __name__ == "__main__":
    main()
