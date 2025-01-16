import psycopg2
from config import load_config
from connect import connect


def get_teams_by_position(year: str, positions: tuple, cur):
    query = f"""
        SELECT Team FROM Table_{year}
        WHERE Pos in {positions}; 
    """
    cur.execute(query)
    results = cur.fetchall()
    print(results)


def get_first_k_places(year: str, k: int, cur):
    positions = tuple(range(1, k+1))
    get_teams_by_position(year, positions, cur)


def get_position_in_these_years(team: str, years: list, cur):
    results = []
    for year in years:
        query = f"""
            SELECT Pos FROM Table_{year}
            WHERE Team = '{team}';
        """
        cur.execute(query)
        results.extend(cur.fetchall()[0])
    print(results)


def get_all_teams_with_highest_GF(year: str, cur):
    query = f"""
        SELECT * FROM Table_{year}
        WHERE gf = (SELECT MAX(gf) FROM Table_{year});
    """

    cur.execute(query)
    results = cur.fetchall()
    print(results)


if __name__ == "__main__":
    config = load_config()
    conn = connect(config)
    cur = conn.cursor()
    # get_teams_by_position("1992_1993", (1, 3, 5), cur)
    # get_first_k_places("1992_1993", 4, cur)
    # get_position_in_these_years("Liverpool", ["1992_1993"], cur)
    get_all_teams_with_highest_GF("1992_1993", cur)
