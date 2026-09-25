import os
import sys

# ---------------------------------------------------------
# PROJECT ROOT
# ---------------------------------------------------------

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


# ---------------------------------------------------------
# FIREBASE CONNECTION
# ---------------------------------------------------------

try:

    from firebase.firebase_config import db

    print("=" * 60)
    print("FIREBASE CONNECTION TEST")
    print("=" * 60)

    # Try accessing Firestore
    collections = db.collections()

    print("\n✅ Firebase connection successful!")
    print("🔥 Firestore is connected.")

    # Convert generator to list
    collection_list = list(collections)

    if collection_list:

        print("\n📦 Existing Firestore collections:")

        for collection in collection_list:

            print(
                f"   • {collection.id}"
            )

    else:

        print(
            "\nℹ️ No collections found."
        )

        print(
            "You can upload your World Cup data "
            "after creating the required CSV files."
        )

    print("\n" + "=" * 60)
    print("TEST COMPLETED")
    print("=" * 60)


except FileNotFoundError as error:

    print("\n❌ Firebase credentials file not found.")
    print(error)

    print(
        "\nMake sure your Firebase service-account "
        "JSON file is placed in the project root."
    )

except Exception as error:

    print("\n❌ Firebase connection failed.")

    print(
        f"Error: {error}"
    )

    print(
        "\nCheck your Firebase credentials, "
        "Firestore setup, and internet connection."
    )
