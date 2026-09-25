import os
import sys

import joblib


# ---------------------------------------------------------
# PROJECT ROOT
# ---------------------------------------------------------

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


# ---------------------------------------------------------
# MODEL PATH
# ---------------------------------------------------------

MODEL_FILE = os.path.join(
    PROJECT_ROOT,
    "ml",
    "models",
    "world_cup_model.pkl"
)


# ---------------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------------

def load_model():

    if not os.path.exists(
        MODEL_FILE
    ):

        print(
            "❌ Trained model not found."
        )

        print(
            "Run train_model.py first."
        )

        return None

    model = joblib.load(
        MODEL_FILE
    )

    print(
        "✅ Machine learning model loaded."
    )

    return model


# ---------------------------------------------------------
# PREDICT MATCH
# ---------------------------------------------------------

def predict_match(
    model,
    team_1_matches,
    team_1_wins,
    team_1_win_percentage,
    team_2_matches,
    team_2_wins,
    team_2_win_percentage
):

    if model is None:

        return None

    win_percentage_difference = (
        team_1_win_percentage
        -
        team_2_win_percentage
    )

    features = [[

        team_1_matches,

        team_1_wins,

        team_1_win_percentage,

        team_2_matches,

        team_2_wins,

        team_2_win_percentage,

        win_percentage_difference

    ]]

    prediction = model.predict(
        features
    )[0]

    probabilities = (
        model.predict_proba(
            features
        )[0]
    )

    return prediction, probabilities


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

def main():

    print("\n")
    print("=" * 70)
    print("ICC WORLD CUP - MATCH PREDICTION")
    print("=" * 70)

    model = load_model()

    if model is None:
        return

    print(
        "\nEnter statistics for Team 1:"
    )

    team_1_matches = int(
        input(
            "Matches played: "
        )
    )

    team_1_wins = int(
        input(
            "Matches won: "
        )
    )

    team_1_win_percentage = float(
        input(
            "Win percentage: "
        )
    )

    print(
        "\nEnter statistics for Team 2:"
    )

    team_2_matches = int(
        input(
            "Matches played: "
        )
    )

    team_2_wins = int(
        input(
            "Matches won: "
        )
    )

    team_2_win_percentage = float(
        input(
            "Win percentage: "
        )
    )

    result = predict_match(

        model,

        team_1_matches,

        team_1_wins,

        team_1_win_percentage,

        team_2_matches,

        team_2_wins,

        team_2_win_percentage

    )

    if result is None:
        return

    prediction, probabilities = result

    print("\n" + "=" * 70)

    if prediction == 1:

        print(
            "🏆 Prediction: TEAM 1"
        )

    else:

        print(
            "🏆 Prediction: TEAM 2"
        )

    print(
        f"Team 1 probability: "
        f"{probabilities[1] * 100:.2f}%"
    )

    print(
        f"Team 2 probability: "
        f"{probabilities[0] * 100:.2f}%"
    )

    print("=" * 70)


if __name__ == "__main__":

    main()
