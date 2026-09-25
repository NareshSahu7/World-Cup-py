import os
import sys
import pandas as pd

# Add project root to Python path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from firebase.firebase_config import db


def upload_csv_to_firestore(csv_file, collection_name):
    """
    Upload a CSV file to a Firestore collection.

    Each CSV row becomes one Firestore document.
    """

    # Check whether CSV exists
    if not os.path.exists(csv_file):
        print(f"❌ File not found: {csv_file}")
        return

    # Read CSV
    df = pd.read_csv(csv_file)

    if df.empty:
        print("❌ CSV file is empty.")
        return

    print(f"📂 Reading: {csv_file}")
    print(f"📊 Total records: {len(df)}")

    collection_ref = db.collection(collection_name)

    uploaded = 0

    # Upload each row
    for index, row in df.iterrows():

        # Convert row to dictionary
        data = row.to_dict()

        # Replace NaN values with None
        cleaned_data = {}

        for key, value in data.items():

            if pd.isna(value):
                cleaned_data[key] = None
            else:
                cleaned_data[key] = value

        # Create document
        document_id = str(index + 1)

        collection_ref.document(document_id).set(cleaned_data)

        uploaded += 1

        print(f"✅ Uploaded record {uploaded}/{len(df)}")

    print("\n--------------------------------")
    print("🎉 Upload completed successfully!")
    print(f"📦 Collection: {collection_name}")
    print(f"📊 Records uploaded: {uploaded}")
    print("--------------------------------")


if __name__ == "__main__":

    # Cricket World Cup match data
    csv_file = os.path.join(
        PROJECT_ROOT,
        "data",
        "matches.csv"
    )

    collection_name = "matches"

    upload_csv_to_firestore(
        csv_file,
        collection_name
    )
