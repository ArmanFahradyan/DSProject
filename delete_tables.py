import psycopg2
from config import load_config
from connect import connect


if __name__ == "__main__":
    table_names = [f"Table_{i}_{i+1}" for i in range(1992, 2024)]

    config = load_config()
    conn = connect(config)
    cur = conn.cursor()
    for table_name in table_names:
        try:
            cur.execute(
                f"DROP TABLE {table_name};")
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)

        conn.commit()
