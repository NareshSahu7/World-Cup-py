import os
import sys


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


from firebase.firebase_config import db


def delete_collection(collection_name):
    """
    Delete all documents from a Firestore collection.
    """

    print("\n" + "=" * 60)
    print(
        f"DELETE COLLECTION: {collection_name}"
    )
    print("=" * 60)

    collection_ref = db.collection(
        collection_name
    )

    documents = list(
        collection_ref.stream()
    )

    if not documents:
        print(
            "⚠️ Collection is already empty."
        )
        return

    print(
        f"📊 Documents found: {len(documents)}"
    )

    confirmation = input(
        f"\nType DELETE to delete "
        f"all documents from '{collection_name}': "
    )

    if confirmation != "DELETE":
        print(
            "❌ Delete operation cancelled."
        )
        return

    deleted = 0

    for document in documents:

        collection_ref.document(
            document.id
        ).delete()

        deleted += 1

        if deleted % 100 == 0:
            print(
                f"Deleted {deleted}/"
                f"{len(documents)}"
            )

    print(
        f"\n🎉 Successfully deleted "
        f"{deleted} documents."
    )


def main():

    print("\n")
    print("=" * 60)
    print("FIREBASE DATA DELETE TOOL")
    print("=" * 60)

    print(
        "\nAvailable collections:"
    )

    print("1. matches")
    print("2. batting")
    print("3. bowling")
    print("4. all")

    choice = input(
        "\nEnter your choice: "
    )

    if choice == "1":

        delete_collection(
            "matches"
        )

    elif choice == "2":

        delete_collection(
            "batting"
        )

    elif choice == "3":

        delete_collection(
            "bowling"
        )

    elif choice == "4":

        delete_collection(
            "matches"
        )

        delete_collection(
            "batting"
        )

        delete_collection(
            "bowling"
        )

    else:

        print(
            "❌ Invalid choice."
        )


if __name__ == "__main__":
    main()
