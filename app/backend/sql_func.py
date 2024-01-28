import sqlite3
from sqlite3 import Error

import datetime 
import random

def sql_connect(database):
    db = None
    cursor = None
    try:
        db = sqlite3.connect('sql_bcknd/' + database)
        cursor = db.cursor()
    except Error as e:
        print(e)
    return (db, cursor)

def get_user_ids(db, cursor):
    cursor.row_factory = lambda cursor, row: row[0]
    cursor.execute('SELECT UserID FROM UserPublic')
    return cursor.fetchall()

def get_ing_ids(db, cursor):
    cursor.row_factory = lambda cursor, row: row[0]
    cursor.execute('SELECT IngredientID FROM Ingredients')
    return cursor.fetchall()

def get_rec_ids(db, cursor):
    cursor.row_factory = lambda cursor, row: row[0]
    cursor.execute('SELECT RecipeID FROM Recipes')
    return cursor.fetchall()

def add_user(db, cursor, FirstName, LastName):
    dt_now = datetime.datetime.now()
    dt_now = int(dt_now.strftime('%Y%m%d'))

    user_ids = get_user_ids(db, cursor)
    cursor.row_factory = None

    UserID = 'C0OR5'
    while UserID in user_ids:
        UserID = ''.join(random.choice('0123456789ABCDEF') for i in range(5))
    
    cursor.execute('INSERT INTO UserPublic (UserID, FirstName, LastName, DateJoined)VALUES ("' + UserID +'","'+ FirstName +'","'+ LastName +'",'+ str(dt_now) + ')')
    db.commit()

##def add_ingredient(db, cursor, IngredientName, IngredientID, Description = None, Sugar = None, Sodium = None, Fats = None,
    ##Protien = None, A = None, B = None, C = None, D = None, Fiber = None, Calories = None):
def add_ingredient(db, cursor, Ingredient):

    db.commit()
    ing_ids = get_ing_ids(db, cursor)
    #print(ing_ids)
    cursor.row_factory = None

    if Ingredient["IngredientID"] not in ing_ids:
        insert_query = '''INSERT INTO Ingredients (IngredientID, IngredientName)
        VALUES ("{IngredientID}", "{IngredientName}")
        '''.format(**Ingredient)

        cursor.execute(insert_query)
        db.commit()


def add_recipe(db, cursor, Recipe):

    recipe_ids = get_rec_ids(db, cursor)
    cursor.row_factory = None

    RecipeID = 'ZKD3VY'
    while RecipeID in recipe_ids:
        RecipeID = ''.join(random.choice('0123456789ABCDEF') for i in range(6))

    user_ids = get_user_ids(db, cursor)
    cursor.row_factory = None
    UserID = random.choice(user_ids) ## DEV

    dt_now = datetime.datetime.now()
    dt_now = int(dt_now.strftime('%Y%m%d'))

    Recipe["RecipeID"] = RecipeID
    Recipe["UserID"] = UserID
    Recipe["DatePosted"] = dt_now
    #Recipe["RecipeThumbnailLink"] = Recipe["RecipeThumbnailLink"].replace('/','?')
    #Recipe["RecipeThumbnailLink"] = Recipe["RecipeThumbnailLink"].replace(':','-')
    Recipe["RecipeThumbnailLink"] = Recipe["RecipeThumbnailLink"].replace(' ','')
    Recipe["Description"] = ""

    insert_recipe = '''INSERT INTO Recipes (RecipeID, RecipeName, UserID, Description, RecipeThumbnailLink, DatePosted)
    VALUES (
        "{RecipeID}",
        "{RecipeName}",
        "{UserID}",
        "{Description}",
        "{RecipeThumbnailLink}",
        "{DatePosted}"
    )
    '''.format(**Recipe)

    cursor.execute(insert_recipe)
    
    for RecipeIngredient in Recipe["RecipeIngredients"]:
        RecipeIngredient["RecipeID"] = RecipeID

        insert_recipe_ingredient = '''INSERT INTO RecipeIngredients_STG (RecipeID, IngredientID, Quantity, QuantityUnit)
        VALUES (
            "{RecipeID}",
            "{IngredientID}",
            {Quantity},
            "{QuantityUnit}"
        )
        '''.format(**RecipeIngredient)

        #print(insert_recipe_ingredient)

        cursor.execute(insert_recipe_ingredient)
        db.commit()

        add_ingredient(db,cursor,RecipeIngredient)



def get_recipe(db, cursor, RecipeID):
    select_query = '''SELECT * FROM (
    SELECT 
    Recipes.*, 
    group_concat(Quantity || " " || QuantityUnit || " of " || A.IngredientName, ", ")  AS "IngredientsList"

    FROM Recipes

    JOIN RecipeIngredients_STG ON RecipeIngredients_STG.RecipeID = Recipes.RecipeID
    JOIN (
    SELECT DISTINCT IngredientID, IngredientName FROM Ingredients
    ) AS A ON RecipeIngredients_STG.IngredientID = A.IngredientID

    GROUP BY Recipes.RecipeID
    ) AS A
    WHERE A.RecipeID = "{}"
    '''.format(RecipeID)
    
    cursor.execute(select_query)
    return cursor.fetchall()

def get_recipe_by_ingredient(db, cursor, IngredientList):
    IngredientsString = ', '.join(f'"{i}"' for i in IngredientList)

    select_query = '''SELECT DISTINCT RecipeID
    FROM (
    SELECT RecipeIngredients_STG.RecipeID, RecipeIngredients_STG.IngredientID, Ingredients.IngredientName FROM RecipeIngredients_STG
    JOIN Ingredients ON Ingredients.IngredientID = RecipeIngredients_STG.IngredientID
    ) AS A
    WHERE A.IngredientName IN ({})
    '''.format(IngredientsString)

    cursor.row_factory = lambda cursor, row: row[0]
    cursor.execute(select_query)
    return cursor.fetchall()

## ------------- Testing Workspace ----------------

#db, cursor = sql_connect('RecipePublic.db')
#print(get_recipe(db, cursor, "015284"))
#print(get_recipe_by_ingredient(["butter","cream cheese"]))
##add_user(db, cursor,  "Jane", "Doe")
##add_ingredient(db, cursor, IngredientName = "Banana", Description = "An elongated, edible fruit, botanically a berry")

##recipes = get_recipes()
##for recipe in recipes:
    ##add_recipe(db, cursor, recipe)

##with open('sql_bcknd/test.sql', 'r') as sql_file:
    ##sql_script = sql_file.read()

##cursor.execute(sql_script)

##result = cursor.fetchall()

#3for row in result:
    ##print(row)

