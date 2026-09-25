import os
import sys

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report
)
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
# PATHS
# ---------------------------------------------------------

FEATURE_FILE = os.path.join(
    PROJECT_ROOT,
    "data",
    "ml_features.csv"
)

MODEL_FOLDER = os.path.join(
    PROJECT_ROOT,
    "ml",
    "models"
)

MODEL_FILE = os.path.join(
    MODEL_FOLDER,
    "world_cup_model.pkl"
)


# ---------------------------------------------------------
# LOAD FEATURES
# ---------------------------------------------------------

def load_features():

    if not os.path.exists(
        FEATURE_FILE
    ):

        print(
            "❌ ml_features.csv not found."
        )

        print(
            "Run prepare_features.py first."
        )

        return pd.DataFrame()

    return pd.read_csv(
        FEATURE_FILE
    )


# ---------------------------------------------------------
# TRAIN MODEL
# ---------------------------------------------------------

def train_model(df):

    if df.empty:

        print(
            "❌ No training data available."
        )

        return None, None

    feature_columns = [
        "team_1_matches",
        "team_1_wins",
        "team_1_win_percentage",
        "team_2_matches",
        "team_2_wins",
        "team_2_win_percentage",
        "win_percentage_difference"
    ]

    X = df[
        feature_columns
    ]

    y = df[
        "target"
    ]

    if len(df) < 10:

        print(
            "❌ Not enough data for training."
        )

        return None, None

    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=0.20,
            random_state=42,
            stratify=y
        )
    )

    print(
        f"📚 Training records: {len(X_train)}"
    )

    print(
        f"🧪 Testing records: {len(X_test)}"
    )

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print(
        f"\n🎯 Model Accuracy: "
        f"{accuracy * 100:.2f}%"
    )

    print("\n📋 Classification Report:")

    print(
        classification_report(
            y_test,
            predictions,
            zero_division=0
        )
    )

    return model, feature_columns


# ---------------------------------------------------------
# SAVE MODEL
# ---------------------------------------------------------

def save_model(model):

    if model is None:
        return

    os.makedirs(
        MODEL_FOLDER,
        exist_ok=True
    )

    joblib.dump(
        model,
        MODEL_FILE
    )

    print(
        f"💾 Model saved to: {MODEL_FILE}"
    )


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

def main():

    print("\n")
    print("=" * 70)
    print("ICC WORLD CUP - MACHINE LEARNING MODEL")
    print("=" * 70)

    df = load_features()

    if df.empty:
        return

    model, _ = train_model(
        df
    )

    save_model(
        model
    )

    print("\n🎉 Model training completed.")


if __name__ == "__main__":

    main()
