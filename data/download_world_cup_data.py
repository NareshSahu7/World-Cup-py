import os
import io
import json
import zipfile
import urllib.request


# Cricsheet ICC Men's Cricket World Cup data
DATA_URL = (
    "https://cricsheet.org/downloads/"
    "icc_mens_cricket_world_cup_male_json.zip"
)

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_FOLDER = os.path.join(
    PROJECT_ROOT,
    "data"
)

RAW_FOLDER = os.path.join(
    DATA_FOLDER,
    "raw"
)


def download_world_cup_data():
    """
    Download ICC Men's Cricket World Cup JSON data
    from Cricsheet and extract it into data/raw/.
    """

    print("=" * 60)
    print("ICC MEN'S CRICKET WORLD CUP DATA DOWNLOADER")
    print("=" * 60)

    os.makedirs(RAW_FOLDER, exist_ok=True)

    zip_path = os.path.join(
        DATA_FOLDER,
        "world_cup_data.zip"
    )

    print("\n📥 Downloading World Cup data...")
    print("Source: Cricsheet")

    try:
        urllib.request.urlretrieve(
            DATA_URL,
            zip_path
        )

        print("✅ Download completed.")

    except Exception as error:
        print("\n❌ Download failed.")
        print(f"Error: {error}")
        return False

    print("\n📦 Extracting JSON files...")

    try:
        with zipfile.ZipFile(
            zip_path,
            "r"
        ) as zip_file:

            zip_file.extractall(RAW_FOLDER)

        print("✅ Extraction completed.")

    except zipfile.BadZipFile:
        print("❌ Downloaded file is not a valid ZIP file.")
        return False

    except Exception as error:
        print("\n❌ Extraction failed.")
        print(f"Error: {error}")
        return False

    # Remove ZIP file after extraction
    try:
        os.remove(zip_path)
        print("🗑️ Temporary ZIP file removed.")
    except OSError:
        pass

    json_files = [
        file
        for file in os.listdir(RAW_FOLDER)
        if file.endswith(".json")
    ]

    print("\n" + "=" * 60)
    print("DOWNLOAD SUMMARY")
    print("=" * 60)

    print(f"📁 Data folder: {RAW_FOLDER}")
    print(f"📄 JSON files found: {len(json_files)}")

    print("\n🎉 World Cup data is ready.")

    return True


if __name__ == "__main__":
    download_world_cup_data()
