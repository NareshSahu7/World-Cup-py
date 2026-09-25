import os
import pandas as pd


def print_section(title):
    """
    Print a formatted section heading.
    """

    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def check_file_exists(file_path):
    """
    Check whether a file exists.
    """

    if os.path.exists(file_path):
        return True

    print(f"❌ File not found: {file_path}")
    return False


def load_csv(file_path):
    """
    Load a CSV file into a Pandas DataFrame.
    """

    if not check_file_exists(file_path):
        return pd.DataFrame()

    try:
        df = pd.read_csv(file_path)

        print(
            f"✅ Loaded {len(df)} records "
            f"from {os.path.basename(file_path)}"
        )

        return df

    except Exception as error:
        print(
            f"❌ Error loading "
            f"{os.path.basename(file_path)}: {error}"
        )

        return pd.DataFrame()


def save_dataframe(df, file_path):
    """
    Save a DataFrame as CSV.
    """

    if df.empty:
        print("⚠️ DataFrame is empty.")
        return False

    directory = os.path.dirname(file_path)

    if directory:
        os.makedirs(
            directory,
            exist_ok=True
        )

    try:
        df.to_csv(
            file_path,
            index=False
        )

        print(
            f"💾 File saved successfully: "
            f"{file_path}"
        )

        return True

    except Exception as error:
        print(f"❌ Error saving file: {error}")
        return False


def show_dataframe_summary(df, name="DataFrame"):
    """
    Display basic DataFrame information.
    """

    print_section(
        f"{name.upper()} SUMMARY"
    )

    if df.empty:
        print("No data available.")
        return

    print(
        f"Rows: {len(df)}"
    )

    print(
        f"Columns: {len(df.columns)}"
    )

    print("\nColumns:")

    for column in df.columns:
        print(f"• {column}")

    print("\nFirst 5 records:")

    print(
        df.head()
    )


def clean_numeric_columns(df, columns):
    """
    Convert selected columns into numeric values.
    """

    for column in columns:

        if column in df.columns:

            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

    return df


def create_directory(directory):
    """
    Create a directory if it does not exist.
    """

    os.makedirs(
        directory,
        exist_ok=True
    )

    return directory
