import sqlite3

def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

TOTAL_CHARACTERS = """
    SELECT COUNT(*)
    FROM charactercreator_character;
"""

TOTAL_SUBCLASS_CLERIC = """
    SELECT COUNT(*)
    FROM charactercreator_cleric;
"""

TOTAL_SUBCLASS_FIGHTER = """
    SELECT COUNT(*)
    FROM charactercreator_fighter;
"""

TOTAL_SUBCLASS_MAGE = """
    SELECT COUNT(*)
    FROM charactercreator_mage;
"""

TOTAL_SUBCLASS_NECROMANCER = """
    SELECT COUNT(*)
    FROM charactercreator_necromancer;
"""

TOTAL_SUBCLASS_THIEF = """
    SELECT COUNT(*)
    FROM charactercreator_thief;
"""

if __name__ == "__main__":
    conn = connect_to_db()
    curs = conn.cursor()

    CHARACTERS = execute_query(curs, TOTAL_CHARACTERS)
    CLERIC = execute_query(curs, TOTAL_SUBCLASS_CLERIC)
    FIGHTER = execute_query(curs, TOTAL_SUBCLASS_FIGHTER)
    MAGE = execute_query(curs, TOTAL_SUBCLASS_MAGE)
    NECROMANCER = execute_query(curs, TOTAL_SUBCLASS_NECROMANCER)
    THIEF = execute_query(curs, TOTAL_SUBCLASS_THIEF)
    print(CHARACTERS[0])
    print(CLERIC[0])
    print(FIGHTER[0])
    print(MAGE[0])
    print(NECROMANCER[0])
    print(THIEF[0])
