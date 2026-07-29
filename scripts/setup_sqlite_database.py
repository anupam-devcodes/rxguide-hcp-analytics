from pathlib import Path
import sqlite3

import pandas as pd


# ------------------------------------------------------------
# 1. Define project folders
# ------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
DATABASE_DIR = PROJECT_ROOT / "database"

DATABASE_DIR.mkdir(exist_ok=True)

DATABASE_PATH = DATABASE_DIR / "rxguide_analytics.db"


# ------------------------------------------------------------
# 2. Connect table names with processed CSV files
# ------------------------------------------------------------

table_files = {
    "hcps": "clean_hcps.csv",
    "sales_reps": "clean_sales_reps.csv",
    "products": "clean_products.csv",
    "call_activity": "clean_call_activity.csv",
    "monthly_prescriptions": "analysis_monthly_prescriptions.csv",
    "ic_quotas": "clean_ic_quotas.csv",
}


# Columns that should be stored as YYYY-MM-DD dates
date_columns = {
    "sales_reps": ["hire_date"],
    "call_activity": ["call_date", "call_month"],
    "monthly_prescriptions": ["rx_month"],
    "ic_quotas": ["quarter_start", "quarter_end"],
}


# ------------------------------------------------------------
# 3. Create the database and load every CSV
# ------------------------------------------------------------

with sqlite3.connect(DATABASE_PATH) as connection:

    for table_name, file_name in table_files.items():

        file_path = PROCESSED_DIR / file_name

        if not file_path.exists():
            raise FileNotFoundError(
                f"Required file not found: {file_path}"
            )

        dataframe = pd.read_csv(file_path)

        # Standardize date columns before storing them
        for column in date_columns.get(table_name, []):
            dataframe[column] = (
                pd.to_datetime(
                    dataframe[column],
                    errors="raise"
                )
                .dt.strftime("%Y-%m-%d")
            )

        dataframe.to_sql(
            name=table_name,
            con=connection,
            if_exists="replace",
            index=False
        )

        print(
            f"{table_name:<25}"
            f"{len(dataframe):>8,} rows loaded"
        )


    # --------------------------------------------------------
    # 4. Verify the database row counts
    # --------------------------------------------------------

    print("\nDatabase verification:")

    for table_name in table_files:

        query = f"""
            SELECT COUNT(*)
            FROM {table_name}
        """

        row_count = connection.execute(query).fetchone()[0]

        print(
            f"{table_name:<25}"
            f"{row_count:>8,} rows"
        )


print(f"\nDatabase created at:\n{DATABASE_PATH}")