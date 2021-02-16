import os
from dotenv import load_dotenv
import json
import pandas as pd
import psycopg2

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

#print(DB_NAME,DB_USER,DB_PASSWORD,DB_HOST)

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
#Create the cursor
cur = conn.cursor()

#Load the CSV data
data = pd.read_csv('titanic.csv')
#Create the DataFrame
df = pd.DataFrame(data, columns= ['Survived','Pclass','Name','Sex','Age','Siblings_Spouses_Aboard', 'Parents_Children_Aboard','Fare'])

#Create the for loop to load the data.
for row in df.itertuples():
    insertion_query = "INSERT INTO titanic (Survived,Pclass,Name,Sex,Age,Siblings_Spouses_Aboard,Parents_Children_Aboard,Fare) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(insertion_query,
    (row.Survived,row.Pclass,row.Name,row.Sex,row.Age,row.Siblings_Spouses_Aboard,row.Parents_Children_Aboard,row.Fare))
    print(row.Survived,row.Pclass,row.Name,row.Sex,row.Age,row.Siblings_Spouses_Aboard,row.Parents_Children_Aboard,row.Fare)

    conn.commit()

#Close the connection
cur.close()
conn.close()
