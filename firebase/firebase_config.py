import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def initialize_firebase():
    """
    Initialize Firebase Firestore using the Firebase service account.
    """

    if not firebase_admin._apps:

        # Get the location of the Firebase service-account file
        credentials_path = os.getenv(
            "FIREBASE_CREDENTIALS",
            "firebase-service-account.json"
        )

        # Check whether credentials file exists
        if not os.path.exists(credentials_path):
            raise FileNotFoundError(
                f"Firebase credentials file not found: {credentials_path}\n"
                "Download your Firebase service-account JSON file and "
                "place it in the project root."
            )

        # Load Firebase credentials
        cred = credentials.Certificate(credentials_path)

        # Initialize Firebase
        firebase_admin.initialize_app(cred)

    # Return Firestore database connection
    return firestore.client()


# Create Firestore database connection
db = initialize_firebase()
