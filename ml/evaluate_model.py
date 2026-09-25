import os
import sys

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)


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

FEATURE_FILE = os.path.join(
    PROJECT_ROOT,
    "data",
    "ml_features.csv"
)

MODEL_FILE = os.path.join(
    PROJECT_ROOT,
    "ml",
    "models",
    "world_cup_model.pkl"
)


# ---------------------------------------------------------
# FEATURE COLUMNS
# ---------------------------------------------------------

FEATURE_COLUMNS = [

    "team_1_matches",

    "team_1_wins",

    "team_1_win_percentage",

    "team_2_matches",

    "team_2_wins",

    "team_2_win_percentage",

    "win_percentage_difference"

]


# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------

def load_data():

    if not os.path.exists(
        FEATURE_FILE
    ):

        print(
            "❌ ml_features.csv not found."
        )

        return None

    return pd.read_csv(
        FEATURE_FILE
    )


# ---------------------------------------------------------
# EVALUATE MODEL
# ---------------------------------------------------------

def evaluate_model():

    df = load_data()

    if df is None or df.empty:
        return

    if not os.path.exists(
        MODEL_FILE
    ):

        print(
            "❌ Trained model not found."
        )

        print(
            "Run train_model.py first."
        )

        return

    X = df[
        FEATURE_COLUMNS
    ]

    y = df[
        "target"
    ]

    _, X_test, _, y_test = (
        train_test_split(
            X,
            y,
            test_size=0.20,
            random_state=42,
            stratify=y
        )
    )

    model = joblib.load(
        MODEL_FILE
    )

    predictions = model.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    matrix = confusion_matrix(
        y_test,
        predictions
    )

    print("\n")
    print("=" * 70)
    print("ICC WORLD CUP - MODEL EVALUATION")
    print("=" * 70)

    print(
        f"\n🎯 Accuracy: "
        f"{accuracy * 100:.2f}%"
    )

    print(
        "\n📊 Confusion Matrix:"
    )

    print(
        matrix
    )

    print(
        "\n📋 Classification Report:"
    )

    print(
        classification_report(
            y_test,
            predictions,
            zero_division=0
        )
    )

    print("=" * 70)


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

if __name__ == "__main__":

    evaluate_model()
