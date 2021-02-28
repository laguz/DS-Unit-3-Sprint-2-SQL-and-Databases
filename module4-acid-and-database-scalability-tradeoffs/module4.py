import os
from dotenv import load_dotenv
import sqlite3
import pymongo
import psycopg2

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

DBNAME =os.getenv("DBNAME")
PASSWORD=os.getenv("DBPASSWORD")

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
class_numbers = cur.fetchall()
print("Class",class_numbers[1][1],"Numbers",class_numbers[1][0])
print("Class",class_numbers[2][1],"Numbers",class_numbers[2][0])
print("Class",class_numbers[0][1],"Numbers",class_numbers[0][0])

cur.close()
conn.close()

def create_sl_conn(extraction_db="rpg_db.sqlite3"):
    return sqlite3.connect(extraction_db)

def execute_query(curs, query):
    curs.execute(query)
    return curs.fetchall()


GET_CHARACTERS = "SELECT COUNT() FROM charactercreator_character"
GET_INVENTORY = "SELECT COUNT() FROM armory_item INNER JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id;"
GET_ARMORY_ITEM = "SELECT COUNT() FROM armory_item"
GET_CHARACTERS_ITEM = "SELECT armory_item.item_id  FROM armory_item INNER JOIN charactercreator_character_inventory ON armory_item.item_id = charactercreator_character_inventory.item_id LIMIT 20;"


if __name__=="__main__":
    sl_conn = create_sl_conn()
    sl_curs = sl_conn.cursor()

    characters = execute_query(sl_curs, GET_CHARACTERS) # returns list
    print("How many total Characters are there?", characters[0][0])

    total_items = execute_query(sl_curs, GET_ARMORY_ITEM) # returns list
    print("How many total Items?", total_items[0][0])
    total_items = int(total_items[0][0])

    weapons = execute_query(sl_curs, GET_INVENTORY) # returns list
    print("How many of the Items are weapons?", weapons[0][0])
    weapons = int(weapons[0][0])
    not_weapons = total_items - weapons
    print("How many are not?", not_weapons)

    characters_item = execute_query(sl_curs, GET_CHARACTERS_ITEM) # returns list
    print("How many Items does each character have?", characters_item)
