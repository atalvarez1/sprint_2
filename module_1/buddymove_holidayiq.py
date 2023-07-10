import pandas as pd
import sqlite3


def connect_to_db(db_name='buddymove_holidayiq.sqlite3'):
    return sqlite3.connect(db_name)


def execute_q(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    return curs.fetchall()


TOTAL_ROWS = '''
    SELECT Count("User Id")
    FROM review
    '''

TOTAL_CENTURIONS_NATURE_SHOPPING = '''
    SELECT COUNT("User Id")
    FROM review
    WHERE Nature > 99 AND Shopping > 99
    '''

AVERAGE_REVIEWS_PER_CATEGORY = '''
    SELECT
        (SELECT AVG(Sports) FROM review) as avg_sports,
        (SELECT AVG(Religious) FROM review) as avg_religious,
        (SELECT AVG(Nature) FROM review) as avg_nature,
        (SELECT AVG(Theatre) FROM review) as avg_theatre,
        (SELECT AVG(Shopping) FROM review) as avg_shopping,
        (SELECT AVG(Picnic) FROM review) as avg_picnic;
        '''

if __name__ == '__main__':
    conn = connect_to_db()
    results = execute_q(conn, AVERAGE_REVIEWS_PER_CATEGORY)
    df = pd.DataFrame(results)
    # df.columns = ['total_rows']
    print(df)
