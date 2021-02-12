# Import libraries
import sqlite3
import pandas as pd



#Create the connection and Database
def connect_to_db(db_name='titanic.sqlite3'):
    return sqlite3.connect(db_name)
#Create execute function
def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

# Open the cvs file in pandas
df = pd.read_csv('titanic.csv')

#Create the query
buddymove_holiday = """
    SELECT COUNT(*)
    FROM buddymove_holidayiq;
"""

if __name__ == "__main__":
    conn = connect_to_db()
    curs = conn.cursor()

    df.to_sql('titanic', con=conn)
