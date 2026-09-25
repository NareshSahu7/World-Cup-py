import os
import sys
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


from config import (
    MATCHES_FILE,
    BATTING_FILE,
    BOWLING_FILE
)


st.set_page_config(
    page_title="ICC World Cup Dashboard",
    page_icon="🏏",
    layout="wide"
)


@st.cache_data
def load_data():

    matches = pd.DataFrame()
    batting = pd.DataFrame()
    bowling = pd.DataFrame()

    if os.path.exists(MATCHES_FILE):
        matches = pd.read_csv(
            MATCHES_FILE
        )

    if os.path.exists(BATTING_FILE):
        batting = pd.read_csv(
            BATTING_FILE
        )

    if os.path.exists(BOWLING_FILE):
        bowling = pd.read_csv(
            BOWLING_FILE
        )

    return (
        matches,
        batting,
        bowling
    )


matches, batting, bowling = load_data()


st.title(
    "🏏 ICC Men's Cricket World Cup Dashboard"
)

st.write(
    "Data analysis and visualization dashboard "
    "for ICC Men's Cricket World Cup data."
)


if matches.empty:

    st.error(
        "Match data not found. "
        "Run the data processing script first."
    )

    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header(
    "Dashboard Filters"
)


if "season" in matches.columns:

    seasons = sorted(
        matches["season"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_season = st.sidebar.selectbox(
        "Select Season",
        ["All"] + seasons
    )

else:

    selected_season = "All"


filtered_matches = matches.copy()


if (
    selected_season != "All"
    and "season" in filtered_matches.columns
):

    filtered_matches = filtered_matches[
        filtered_matches["season"].astype(str)
        == selected_season
    ]


# ============================================================
# KEY STATISTICS
# ============================================================

st.header(
    "📊 Tournament Statistics"
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Total Matches",
        len(filtered_matches)
    )


with col2:

    if "winner" in filtered_matches.columns:

        total_wins = (
            filtered_matches["winner"]
            .notna()
            .sum()
        )

    else:

        total_wins = 0

    st.metric(
        "Completed Matches",
        total_wins
    )


with col3:

    if (
        "team_1" in filtered_matches.columns
        and "team_2" in filtered_matches.columns
    ):

        teams = set(
            filtered_matches["team_1"]
            .dropna()
            .tolist()
        )

        teams.update(
            filtered_matches["team_2"]
            .dropna()
            .tolist()
        )

        total_teams = len(teams)

    else:

        total_teams = 0

    st.metric(
        "Teams",
        total_teams
    )


with col4:

    st.metric(
        "Batting Records",
        len(batting)
    )


# ============================================================
# TEAM WINS
# ============================================================

st.header(
    "🏆 Team Wins"
)


if "winner" in filtered_matches.columns:

    wins = (
        filtered_matches["winner"]
        .dropna()
        .value_counts()
    )

    if not wins.empty:

        fig, ax = plt.subplots()

        wins.head(15).plot(
            kind="bar",
            ax=ax
        )

        ax.set_xlabel(
            "Team"
        )

        ax.set_ylabel(
            "Wins"
        )

        ax.set_title(
            "Top Teams by Match Wins"
        )

        plt.xticks(
            rotation=45,
            ha="right"
        )

        st.pyplot(fig)

        plt.close(fig)


# ============================================================
# TOP RUN SCORERS
# ============================================================

st.header(
    "🏏 Top Run Scorers"
)


if (
    not batting.empty
    and "batter" in batting.columns
    and "batter_runs" in batting.columns
):

    batting["batter_runs"] = pd.to_numeric(
        batting["batter_runs"],
        errors="coerce"
    )

    top_batters = (
        batting.groupby("batter")[
            "batter_runs"
        ]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(10)
    )

    if not top_batters.empty:

        fig, ax = plt.subplots()

        top_batters.sort_values().plot(
            kind="barh",
            ax=ax
        )

        ax.set_xlabel(
            "Runs"
        )

        ax.set_ylabel(
            "Player"
        )

        ax.set_title(
            "Top 10 Run Scorers"
        )

        st.pyplot(fig)

        plt.close(fig)


# ============================================================
# TOP WICKET TAKERS
# ============================================================

st.header(
    "🎯 Top Wicket Takers"
)


if (
    not bowling.empty
    and "bowler" in bowling.columns
    and "wickets" in bowling.columns
):

    bowling["wickets"] = pd.to_numeric(
        bowling["wickets"],
        errors="coerce"
    )

    top_bowlers = (
        bowling.groupby("bowler")[
            "wickets"
        ]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(10)
    )

    if not top_bowlers.empty:

        fig, ax = plt.subplots()

        top_bowlers.sort_values().plot(
            kind="barh",
            ax=ax
        )

        ax.set_xlabel(
            "Wickets"
        )

        ax.set_ylabel(
            "Bowler"
        )

        ax.set_title(
            "Top 10 Wicket Takers"
        )

        st.pyplot(fig)

        plt.close(fig)


# ============================================================
# MATCHES BY SEASON
# ============================================================

if "season" in matches.columns:

    st.header(
        "📅 Matches by Season"
    )

    season_data = (
        filtered_matches
        .groupby("season")
        .size()
    )

    if not season_data.empty:

        fig, ax = plt.subplots()

        season_data.plot(
            kind="bar",
            ax=ax
        )

        ax.set_xlabel(
            "Season"
        )

        ax.set_ylabel(
            "Matches"
        )

        ax.set_title(
            "Matches Played by Season"
        )

        plt.xticks(
            rotation=45,
            ha="right"
        )

        st.pyplot(fig)

        plt.close(fig)


# ============================================================
# RAW DATA
# ============================================================

with st.expander(
    "📋 View Match Data"
):

    st.dataframe(
        filtered_matches,
        use_container_width=True
    )


st.success(
    "Dashboard loaded successfully."
)
