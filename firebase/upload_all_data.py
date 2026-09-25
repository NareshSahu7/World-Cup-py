import os
import sys
import pandas as pd

# ---------------------------------------------------------
# PROJECT ROOT
# ---------------------------------------------------------

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from firebase.firebase_config import db


# ---------------------------------------------------------
# UPLOAD FUNCTION
# ---------------------------------------------------------

def upload_csv(csv_filename, collection_name):
    """
    Upload a CSV file to a Firestore collection.
    """

    csv_path = os.path.join(
        PROJECT_ROOT,
        "data",
        csv_filename
    )

    print("\n" + "=" * 60)
    print(f"Uploading: {csv_filename}")
    print(f"Collection: {collection_name}")
    print("=" * 60)

    # Check file
    if not os.path.exists(csv_path):
        print(f"❌ File not found: {csv_path}")
        return

    # Read CSV
    df = pd.read_csv(csv_path)

    if df.empty:
        print("⚠️ CSV file is empty.")
        return

    print(f"📊 Records found: {len(df)}")

    collection_ref = db.collection(
        collection_name
    )

    uploaded = 0

    # Upload records
    for index, row in df.iterrows():

        data = {}

        for column in df.columns:

            value = row[column]

            # Convert NaN to None
            if pd.isna(value):
                data[column] = None

            else:
                # Convert NumPy values to normal Python values
                if hasattr(value, "item"):
                    value = value.item()

                data[column] = value

        # Create document ID
        document_id = str(index + 1)

        collection_ref.document(
            document_id
        ).set(data)

        uploaded += 1

        # Show progress every 100 records
        if uploaded % 100 == 0:

            print(
                f"✅ Uploaded "
                f"{uploaded}/{len(df)} records"
            )

    print(
        f"🎉 Completed: "
        f"{uploaded} records uploaded."
    )


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

def main():

    print("\n")
    print("=" * 60)
    print("ICC WORLD CUP FIREBASE DATA UPLOADER")
    print("=" * 60)

    # Upload match data
    upload_csv(
        "matches.csv",
        "matches"
    )

    # Upload batting data
    upload_csv(
        "batting.csv",
        "batting"
    )

    # Upload bowling data
    upload_csv(
        "bowling.csv",
        "bowling"
    )

    print("\n" + "=" * 60)
    print("🎉 ALL DATA UPLOADED TO FIREBASE")
    print("=" * 60)


if __name__ == "__main__":
    main()
