import psycopg2
import sqlite3
from sqlite_example import connect_to_db, execute_q
from pipeline import modify_db
import pandas as pd

DBNAME = 'yxjgfxog'
USER = 'yxjgfxog'
PASSWORD = 'E4d3z0zdxKrB1C06Pzukq_5JLgkIHM4s'
HOST = 'stampy.db.elephantsql.com'

def connect_to_pg(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST):
    pg_conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs

def connect_to_db(db_name='titanic.sqlite3'):
    return sqlite3.connect(db_name)

def load_csv_to_sqlite(csv_file_path, db_file_path, table_name):

    df = pd.read_csv(csv_file_path)

    conn = sqlite3.connect(db_file_path)

    df.to_sql(table_name, conn, if_exists='replace', index=False)

GET_TITANIC_DATA = '''
    SELECT * FROM titanic
    '''

CREATE_TITANIC_TABLE = '''
    CREATE TABLE IF NOT EXISTS titanic 
    (
    "Survived" INT NOT NULL,
    "Pclass" INT,
    "Name" VARCHAR,
    "Sex" VARCHAR,
    "Age" INT,
    "Siblings/Spouses Aboard" INT,
    "Parents/Children Aboard" INT,
    "Fare" INT
    );
    '''

DROP_TITANIC_TABLE = '''
    DROP TABLE IF EXISTS titanic
    '''

if __name__ == "__main__":
    
    # Get data from SQLite
    sl_conn = connect_to_db()
    sl_titanic = execute_q(sl_conn, GET_TITANIC_DATA)

    # Create destination table within PostgreSQL DB
    pg_conn, pg_curs = connect_to_pg()
    modify_db(pg_conn, pg_curs, DROP_TITANIC_TABLE)
    modify_db(pg_conn, pg_curs, CREATE_TITANIC_TABLE)

    # Loop over titanic data and insert into PostgreSQL with correct values
    for titanic in sl_titanic:
        modify_db(pg_conn, pg_curs,
            f'''
            INSERT INTO titanic ("Survived", "Pclass", "Name", "Sex", "Age", "Siblings/Spouses Aboard", "Parents/Children Aboard", "Fare")
            VALUES ({titanic[0]}, {titanic[1]}, '{titanic[2]}', '{titanic[3]}', {titanic[4]}, {titanic[5]}, {titanic[6]}, {titanic[7]})
            '''
        )

