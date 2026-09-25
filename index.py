    success = pd.DataFrame({
        "Titles": winner_count,
        "Runner-up": runner_up_count
    }).fillna(0)

    success["Titles"] = success["Titles"].astype(int)
    success["Runner-up"] = success["Runner-up"].astype(int)
    success["Finals"] = success["Titles"] + success["Runner-up"]

    success = success.sort_values(
        by=["Titles", "Runner-up"],
        ascending=False
    )

    print("\n========== TEAM SUCCESS TABLE ==========")
    print(success)

    return success


def analyze_india(df):
    """Display India's World Cup results."""
    india_wins = (df["Winner"] == "India").sum()
    india_runnerups = (df["Runner-up"] == "India").sum()

    print("\n========== INDIA ANALYSIS ==========")
    print("India World Cup Titles:", india_wins)
    print("India Runner-up Finishes:", india_runnerups)

    india_results = df[
        (df["Winner"] == "India") |
        (df["Runner-up"] == "India")
    ]

    print("\nIndia's World Cup Final Results:")
    print(india_results[
        ["Year", "Host", "Winner", "Runner-up"]
    ].to_string(index=False))

    return india_results


def show_summary(df, winner_count, runner_up_count):
    """Print an overall project summary."""
    print("\n========== WORLD CUP SUMMARY ==========")
    print("Total World Cups:", len(df))
    print("Different winning teams:", df["Winner"].nunique())
    print("Different host entries:", df["Host"].nunique())
    print("Team with the most titles:", winner_count.idxmax())
    print("Number of titles:", winner_count.max())
    print("Team with the most runner-up finishes:",
          runner_up_count.idxmax())
    print("Number of runner-up finishes:",
          runner_up_count.max())

    india_wins = (df["Winner"] == "India").sum()
    india_runnerups = (df["Runner-up"] == "India").sum()

    print("India's titles:", india_wins)
    print("India's runner-up finishes:", india_runnerups)


def main():
    print("==============================================")
    print(" ICC MEN'S CRICKET WORLD CUP DATA ANALYSIS")
    print("==============================================")

    # Load dataset
    df = load_data()

    # Basic dataset information
    show_basic_information(df)

    # Column names
    print("\nColumns:", df.columns.tolist())

    # Analyze winners
    winner_count = analyze_winners(df)

    # Analyze runner-ups
    runner_up_count = analyze_runner_ups(df)

    # Analyze hosts
    analyze_hosts(df)

    # Combined success analysis
    success = create_success_table(
        winner_count,
        runner_up_count
    )

    # India's results
    analyze_india(df)

    # Final summary
    show_summary(
        df,
        winner_count,
        runner_up_count
    )

    # Final title summary table
    final_summary = (
        winner_count
        .rename("World Cup Titles")
        .reset_index()
    )

    final_summary.columns = ["Team", "World Cup Titles"]

    print("\n========== FINAL TITLE SUMMARY ==========")
    print(final_summary.to_string(index=False))


if __name__ == "__main__":
    main()
