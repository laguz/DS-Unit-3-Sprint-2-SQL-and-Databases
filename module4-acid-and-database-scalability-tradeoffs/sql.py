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

cur.execute("SELECT COUNT(Survived) AS titanicSurvived FROM titanic WHERE Survived = 1;")
survive = cur.fetchall()
print("How many passengers survived?",survive[0][0])

cur.execute("SELECT COUNT(Survived) AS titanicSurvived FROM titanic WHERE Survived = 0;")
died = cur.fetchall()
print("How many died?",died[0][0])

cur.execute("SELECT COUNT(pclass), pclass FROM titanic GROUP BY pclass ORDER BY COUNT(pclass) DESC;")
nicole = cur.fetchall()
print("Class",nicole[0][1],"Numbers",nicole[0][0])
print("Class",nicole[1][1],"Numbers",nicole[1][0])
print("Class",nicole[2][1],"Numbers",nicole[2][0])

cur.close()
conn.close()
