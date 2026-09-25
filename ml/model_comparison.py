import os
import sys
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier
)

from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


from config import (
    ML_FEATURE_FILE,
    RANDOM_STATE,
    TEST_SIZE
)


def load_features():

    if not os.path.exists(
        ML_FEATURE_FILE
    ):

        print(
            "❌ ML feature file not found."
        )

        print(
            "Run prepare_features.py first."
        )

        return None

    return pd.read_csv(
        ML_FEATURE_FILE
    )


def compare_models():

    df = load_features()

    if df is None or df.empty:
        return

    print("\n")
    print("=" * 60)
    print("MACHINE LEARNING MODEL COMPARISON")
    print("=" * 60)

    target_column = "team_1_won"

    if target_column not in df.columns:

        print(
            f"❌ Target column '{target_column}' "
            "not found."
        )

        return

    df = df.dropna(
        subset=[target_column]
    )

    X = df.drop(
        columns=[target_column]
    )

    y = df[target_column]

    # Remove non-numeric columns
    X = X.select_dtypes(
        include=["number"]
    )

    if X.empty:

        print(
            "❌ No numeric features available."
        )

        return

    X = X.fillna(0)

    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=TEST_SIZE,
            random_state=RANDOM_STATE,
            stratify=y
        )
    )

    models = {

        "Logistic Regression":
            LogisticRegression(
                max_iter=1000
            ),

        "Decision Tree":
            DecisionTreeClassifier(
                random_state=RANDOM_STATE
            ),

        "Random Forest":
            RandomForestClassifier(
                n_estimators=200,
                random_state=RANDOM_STATE
            ),

        "Gradient Boosting":
            GradientBoostingClassifier(
                random_state=RANDOM_STATE
            )
    }

    results = []

    for name, model in models.items():

        print(
            f"\nTraining: {name}"
        )

        try:

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

            results.append(
                {
                    "model": name,
                    "accuracy": accuracy
                }
            )

            print(
                f"Accuracy: "
                f"{accuracy:.4f}"
            )

        except Exception as error:

            print(
                f"❌ Error with {name}: "
                f"{error}"
            )

    if results:

        results_df = pd.DataFrame(
            results
        )

        print("\n")
        print("=" * 60)
        print("MODEL RESULTS")
        print("=" * 60)

        print(
            results_df.to_string(
                index=False
            )
        )

        print(
            "\nModel comparison completed."
        )


if __name__ == "__main__":
    compare_models()
