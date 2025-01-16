import psycopg2
from config import load_config
from connect import connect


def create_tables(table_names):

    config = load_config()
    conn = connect(config)
    cur = conn.cursor()
    for table_name in table_names:
        try:
            cur.execute(f"CREATE TABLE {table_name} (Pos integer PRIMARY KEY, Team varchar, Pld integer, W integer, D integer, L integer, GF integer, GA integer, GD integer, Pts integer);")
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)

        conn.commit()


if __name__ == "__main__":
    table_names = [f"table_{i}_{i+1}" for i in range(1992, 2024)]
    print(table_names)
    input()
    create_tables(table_names)
