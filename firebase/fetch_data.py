import os
import sys
import pandas as pd

# Add project root to Python path
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from firebase.firebase_config import db


def fetch_collection(collection_name):
    """
    Fetch all documents from a Firestore collection
    and return them as a Pandas DataFrame.
    """

    print(f"📥 Fetching data from: {collection_name}")

    collection_ref = db.collection(collection_name)

    documents = collection_ref.stream()

    records = []

    for document in documents:
        data = document.to_dict()

        # Store Firestore document ID
        data["document_id"] = document.id

        records.append(data)

    if not records:
        print(f"⚠️ No data found in '{collection_name}' collection.")
        return pd.DataFrame()

    df = pd.DataFrame(records)

    print(f"✅ Records fetched: {len(df)}")
    print(f"📊 Columns: {len(df.columns)}")

    return df


def save_to_csv(df, filename):
    """
    Save a Pandas DataFrame to a CSV file.
    """

    if df.empty:
        print("❌ DataFrame is empty. Nothing to save.")
        return

    output_directory = os.path.join(
        PROJECT_ROOT,
        "data"
    )

    os.makedirs(output_directory, exist_ok=True)

    output_path = os.path.join(
        output_directory,
        filename
    )

    df.to_csv(
        output_path,
        index=False
    )

    print(f"💾 Data saved to: {output_path}")


if __name__ == "__main__":

    # Firestore collection to fetch
    collection_name = "matches"

    # Fetch data
    matches_df = fetch_collection(collection_name)

    # Display basic information
    if not matches_df.empty:

        print("\n========== DATA PREVIEW ==========")

        print(matches_df.head())

        print("\n========== DATA INFORMATION ==========")

        print(matches_df.info())

        print("\n========== COLUMN NAMES ==========")

        print(matches_df.columns.tolist())

        # Save downloaded data locally
        save_to_csv(
            matches_df,
            "matches_from_firebase.csv"
        )
