import os


# ============================================================
# PROJECT CONFIGURATION
# ============================================================

PROJECT_ROOT = os.path.dirname(
    os.path.abspath(__file__)
)


# ============================================================
# DATA DIRECTORIES
# ============================================================

DATA_FOLDER = os.path.join(
    PROJECT_ROOT,
    "data"
)

RAW_DATA_FOLDER = os.path.join(
    DATA_FOLDER,
    "raw"
)

CHART_FOLDER = os.path.join(
    PROJECT_ROOT,
    "visualization",
    "charts"
)

MODEL_FOLDER = os.path.join(
    PROJECT_ROOT,
    "ml",
    "models"
)


# ============================================================
# DATA FILES
# ============================================================

MATCHES_FILE = os.path.join(
    DATA_FOLDER,
    "matches.csv"
)

BATTING_FILE = os.path.join(
    DATA_FOLDER,
    "batting.csv"
)

BOWLING_FILE = os.path.join(
    DATA_FOLDER,
    "bowling.csv"
)

ML_FEATURE_FILE = os.path.join(
    DATA_FOLDER,
    "ml_features.csv"
)


# ============================================================
# FIREBASE
# ============================================================

FIREBASE_CREDENTIALS = os.getenv(
    "FIREBASE_CREDENTIALS",
    os.path.join(
        PROJECT_ROOT,
        "firebase-service-account.json"
    )
)


# ============================================================
# FIRESTORE COLLECTIONS
# ============================================================

MATCHES_COLLECTION = "matches"

BATTING_COLLECTION = "batting"

BOWLING_COLLECTION = "bowling"


# ============================================================
# MACHINE LEARNING
# ============================================================

MODEL_FILE = os.path.join(
    MODEL_FOLDER,
    "world_cup_model.pkl"
)

TEST_SIZE = 0.20

RANDOM_STATE = 42


# ============================================================
# CREATE REQUIRED DIRECTORIES
# ============================================================

os.makedirs(
    DATA_FOLDER,
    exist_ok=True
)

os.makedirs(
    RAW_DATA_FOLDER,
    exist_ok=True
)

os.makedirs(
    CHART_FOLDER,
    exist_ok=True
)

os.makedirs(
    MODEL_FOLDER,
    exist_ok=True
)
