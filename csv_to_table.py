from config import load_config
from connect import connect

import pandas as pd
import os


def csv_to_table(csv_path):
    csv_name = os.path.basename(csv_path)
    table_name = csv_name[:csv_name.rfind('.')]

    df = pd.read_csv(csv_path)

    config = load_config()
    conn = connect(config)
    cur = conn.cursor()

    insert_query = f"INSERT INTO {table_name} (" + ", ".join(list(df.columns)) + ") VALUES (" + ", ".join(["%s"]*len(df.columns)) + ")"

    # Execute query for each data row
    cur.executemany(insert_query, df.values)

    # Commit the transaction
    conn.commit()


def csvs_to_tables(csv_path_list):
    for csv_path in csv_path_list:
        csv_to_table(csv_path)


if __name__ == "__main__":
    csv_files_path = "csv_files"
    csv_path_list = [os.path.join(csv_files_path, file_name) for file_name in os.listdir(csv_files_path)]
    csvs_to_tables(csv_path_list)


