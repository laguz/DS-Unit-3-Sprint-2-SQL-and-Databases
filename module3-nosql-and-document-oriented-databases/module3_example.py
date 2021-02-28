import os
from dotenv import load_dotenv
import sqlite3
import pymongo

load_dotenv()

DBNAME =os.getenv("DBNAME")
PASSWORD=os.getenv("DBPASSWORD")


def create_mdb_conn(password, dbname):
    client = pymongo.MongoClient(
        "mongodb+srv://MacOS-laguz:{}@cluster0.sal6s.mongodb.net/{}?retryWrites=true&w=majority"
        .format(password, dbname)
    )
    return client

def create_sl_conn(extraction_db="rpg_db.sqlite3"):
    return sqlite3.connect(extraction_db)

def execute_query(curs, query):
    curs.execute(query)
    return curs.fetchall()

def character_doc_creation(mongo_db, characters):
    i = 0
    # character - {id, name, level, exp, hp, strength, intelligence, dexterity, wisdom}
    for character in characters:
        character_doc = {
            "name": characters[i][1],
            "level": characters[i][2],
            "exp": characters[i][3],
            "hp": characters[i][4],
            "strength": characters[i][5],
            "intelligence": characters[i][6],
            "dexterity": characters[i][7],
            "wisdom": characters[i][8]
        }
        mongo_db.RPG.insert_one(character_doc)
        i+=1

def character_doc_inventory(mongo_db, inventory):
    i = 0
    # character - {id, name, level, exp, hp, strength, intelligence, dexterity, wisdom}
    for item in inventory:
        inventory_doc = {
            "character_id": characters[i][1],
            "item_id": characters[i][2],
        }
        mongo_db.RPG.insert_one(inventory_doc)
        i+=1

def character_doc_item(mongo_db, items):
    i = 0
    # character - {id, name, level, exp, hp, strength, intelligence, dexterity, wisdom}
    for item in items:
        items_doc = {
            "name": characters[i][1],
            "value": characters[i][2],
            "weight": characters[i][3],
        }
        mongo_db.RPG.insert_one(items_doc)
        i+=1

def character_doc_weapon(mongo_db, weapons):
    i = 0
    # character - {id, name, level, exp, hp, strength, intelligence, dexterity, wisdom}
    for weapon in weapons:
        weapons_doc = {
            "power": characters[i][1],
        }
        mongo_db.RPG.insert_one(weapons_doc)
        i+=1


GET_CHARACTERS = "SELECT * FROM charactercreator_character"
GET_INVENTORY = "SELECT * FROM charactercreator_character_inventory"
GET_ARMORY_ITEM = "SELECT * FROM armory_item"
GET_ARMORY_WEAPON = "SELECT * FROM armory_weapon"


if __name__=="__main__":
    sl_conn = create_sl_conn()
    sl_curs = sl_conn.cursor()
    client = create_mdb_conn(PASSWORD, DBNAME)
    db = client.RPG
    characters = execute_query(sl_curs, GET_CHARACTERS) # returns list
    inventory = execute_query(sl_curs, GET_INVENTORY) # returns list
    items = execute_query(sl_curs, GET_ARMORY_ITEM) # returns list
    weapons = execute_query(sl_curs, GET_ARMORY_WEAPON) # returns list
    character_doc_creation(db, characters)
    character_doc_inventory(db, inventory)
    character_doc_item(db, items)
    character_doc_weapon(db, weapons)
