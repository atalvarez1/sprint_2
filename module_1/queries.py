GET_CHARACTERS = 'SELECT * FROM charactercreator_character;'

AVG_ITEM_WEIGHT_PER_CHARACTER = '''
    SELECT cc_char.name, AVG(ai.weight) AS avg_item_weight
    FROM charactercreator_character AS cc_char
    JOIN charactercreator_character_inventory AS cc_inv
    ON cc_char.character_id = cc_inv.character_id
    JOIN armory_item AS ai
    ON ai.item_id = cc_inv.item_id
    GROUP BY cc_char.character_id
    '''

TOTAL_CHARACTERS = '''
    SELECT COUNT(cc_char.character_id)
    FROM charactercreator_character as cc_char;
    '''

TOTAL_SUBCLASS = '''
    SELECT 
        (SELECT COUNT(character_ptr_id) FROM charactercreator_cleric) AS num_clerics,
        (SELECT COUNT(character_ptr_id) FROM charactercreator_fighter) AS num_fighters,
        (SELECT COUNT(character_ptr_id) FROM charactercreator_mage) AS num_mages,
        (SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer) AS num_necromancers;
    '''

TOTAL_ITEMS = '''
    SELECT COUNT(cc_inv.item_id)
    FROM charactercreator_character_inventory AS cc_inv;
    '''

WEAPONS = '''
    SELECT COUNT(aw.item_ptr_id) AS weapons
    FROM armory_item AS ai
    JOIN armory_weapon AS aw
    ON ai.item_id = aw.item_ptr_id;
    '''

NON_WEAPONS = '''
    SELECT COUNT(item_id) AS non_weapons
    FROM armory_item AS ai
    LEFT JOIN armory_weapon AS aw
    ON ai.item_id = aw.item_ptr_id
    WHERE aw.item_ptr_id IS NULL;
    '''

CHARACTER_ITEMS = '''
    SELECT cc_c.name, COUNT(cc_inv.item_id) as item_count
    FROM charactercreator_character_inventory as cc_inv
    JOIN charactercreator_character as cc_c ON cc_c.character_id = cc_inv.character_id
    GROUP BY cc_c.name
    LIMIT 20;
    '''


CHARACTER_WEAPONS = '''
    SELECT cc_c.name, COUNT(aw.item_ptr_id) AS weapon_count
    FROM charactercreator_character_inventory AS cc_inv
    JOIN charactercreator_character AS cc_c ON cc_c.character_id = cc_inv.character_id
    JOIN armory_weapon AS aw ON cc_inv.item_id = aw.item_ptr_id
    GROUP BY cc_c.name
    LIMIT 20;
    '''

AVG_CHARACTER_ITEMS = '''
    SELECT AVG(item_count) as avg_items_per_character
    FROM (
    SELECT cc_c.name, COUNT(cc_inv.item_id) as item_count
    FROM charactercreator_character_inventory as cc_inv
    JOIN charactercreator_character as cc_c ON cc_c.character_id = cc_inv.character_id
    GROUP BY cc_c.name
    );
    '''

AVG_CHARACTER_WEAPONS = '''
    SELECT AVG(weapon_count) as avg_weapons_per_character
    FROM(
        SELECT cc_c.name, COUNT(aw.item_ptr_id) AS weapon_count
        FROM charactercreator_character_inventory AS cc_inv
        JOIN charactercreator_character AS cc_c ON cc_c.character_id = cc_inv.character_id
        JOIN armory_weapon AS aw ON cc_inv.item_id = aw.item_ptr_id
        GROUP BY cc_c.name
    );
    '''

CREATE_TEST_TABLE = '''
    CREATE TABLE IF NOT EXISTS test_table
    ("id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(200) NOT NULL, 
    "age" INT NOT NULL,
    "country_of_origin" VARCHAR(200) NOT NULL);
    '''

INSERT_TEST_TABLE = '''
    INSERT INTO test_table ("name", "age", "country_of_origin")
    Values ('Adam Alvarez', '32', 'USA');
    '''

DROP_TEST_TABLE = '''
    DROP TABLE IF EXISTS test_table
    '''

CREATE_CHARACTER_TABLE = '''
    CREATE TABLE IF NOT EXISTS characters 
    (
    "character_id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(30),
    "level" INT NOT NULL,
    "exp" INT NOT NULL,
    "hp" INT NOT NULL,
    "strength" INT NOT NULL,
    "intelligence" INT NOT NULL,
    "dexterity" INT NOT NULL,
    "wisdom" INT NOT NULL
    );
'''

INSERT_ADAM = '''
    INSERT INTO characters ("name", "level", "exp", "hp", "strength", "intelligence", "dexterity", "wisdom")
    VALUES ('Adam Alvarez', 50, 100, 1000, 9000, 4, -5, 12)
    '''

DROP_CHARACTER_TABLE = '''
    DROP TABLE IF EXISTS characters
    '''