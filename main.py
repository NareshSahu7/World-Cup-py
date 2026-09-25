import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


def run_data_download():
    print("\n" + "=" * 60)
    print("STEP 1: DOWNLOADING WORLD CUP DATA")
    print("=" * 60)

    from data.download_world_cup_data import download_world_cup_data

    return download_world_cup_data()


def run_data_processing():
    print("\n" + "=" * 60)
    print("STEP 2: PROCESSING WORLD CUP DATA")
    print("=" * 60)

    from data.process_world_cup_data import process_all_files

    return process_all_files()


def run_analysis():
    print("\n" + "=" * 60)
    print("STEP 3: RUNNING DATA ANALYSIS")
    print("=" * 60)

    from analysis.team_analysis import analyze_teams
    from analysis.player_analysis import analyze_players
    from analysis.bowling_analysis import analyze_bowling
    from analysis.match_analysis import analyze_matches
    from analysis.statistics import generate_statistics
    from analysis.tournament_analysis import analyze_tournaments

    try:
        analyze_teams()
    except Exception as error:
        print(f"Team analysis error: {error}")

    try:
        analyze_players()
    except Exception as error:
        print(f"Player analysis error: {error}")

    try:
        analyze_bowling()
    except Exception as error:
        print(f"Bowling analysis error: {error}")

    try:
        analyze_matches()
    except Exception as error:
        print(f"Match analysis error: {error}")

    try:
        generate_statistics()
    except Exception as error:
        print(f"Statistics error: {error}")

    try:
        analyze_tournaments()
    except Exception as error:
        print(f"Tournament analysis error: {error}")


def run_visualizations():
    print("\n" + "=" * 60)
    print("STEP 4: CREATING VISUALIZATIONS")
    print("=" * 60)

    from visualization.run_all_charts import run_all_charts

    try:
        run_all_charts()
    except Exception as error:
        print(f"Visualization error: {error}")


def run_machine_learning():
    print("\n" + "=" * 60)
    print("STEP 5: MACHINE LEARNING")
    print("=" * 60)

    from ml.prepare_features import prepare_features
    from ml.train_model import train_model

    try:
        prepare_features()
        train_model()
    except Exception as error:
        print(f"Machine learning error: {error}")


def main():
    print("\n")
    print("=" * 60)
    print(" ICC MEN'S CRICKET WORLD CUP DATA PROJECT")
    print("=" * 60)

    print("\nProject root:")
    print(PROJECT_ROOT)

    # Step 1
    download_success = run_data_download()

    if download_success is False:
        print("\n❌ Data download failed.")
        return

    # Step 2
    try:
        run_data_processing()
    except Exception as error:
        print(f"\n❌ Data processing failed: {error}")
        return

    # Step 3
    run_analysis()

    # Step 4
    run_visualizations()

    # Step 5
    run_machine_learning()

    print("\n" + "=" * 60)
    print("🎉 PROJECT EXECUTION COMPLETED")
    print("=" * 60)

    print("\nGenerated files are available inside:")
    print("• data/")
    print("• visualization/charts/")
    print("• ml/models/")

    print("\nFirebase upload can be run separately using:")
    print("python firebase/upload_all_data.py")


if __name__ == "__main__":
    main()
