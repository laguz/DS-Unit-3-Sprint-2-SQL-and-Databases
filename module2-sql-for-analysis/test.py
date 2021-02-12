import pandas as pd
import psycopg2
import sqlite3

#Create the connection and Database
def connect_to_db(db_name='titanic'):
    return psycopg2.connect(dbname='mnrfsowc', user='mnrfsowc', password='itj0jFb-QZrJEVbMlpR3W9zDki75lW_h', host='ziggy.db.elephantsql.com')
#Create execute function
df = pd.read_csv('titanic.csv')

if __name__ == "__main__":
    conn = connect_to_db()
    curs = conn.cursor()

    df.to_sql('titanic', con=conn)
