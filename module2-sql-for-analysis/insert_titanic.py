import os
from dotenv import load_dotenv
import pandas as pd
import psycopg2

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

print(DB_NAME,DB_USER,DB_PASSWORD,DB_HOST)

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION", conn)
### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()
print('CURSOR', cur)
### An example query
cur.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
print(cur.fetchall())

insertion_sql ="""
INSERT INTO test_table (name, data) VALUES
(
  'A row name',
  null
),
(
  'Another row, with JSON',
  '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB
);
"""

cur.execute(insertion_sql)


conn.commit()

cur.close()
conn.close()
