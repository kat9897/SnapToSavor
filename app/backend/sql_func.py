import sqlite3
from sqlite3 import Error

import datetime 
import random

from generate_recipes import *

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

    insert_query = '''INSERT INTO Ingredients (IngredientID, IngredientName, Description, Sugar_g, Sodium_mg, Fats_g, Protien_g, Vitamin_A_mcg, Vitamin_B_mcg, Vitamin_C_mcg, Vitamin_D_mcg, Fiber_g, Calories)
    VALUES ("{IngredientID}", "{IngredientName}", "{Description}", "{Sugar_g}", "{Sodium_mg}", "{Fats_g}", "{Protein_g}", "{Vitamin_A_mcg}", "{Vitamin_B_mcg}", "{Vitamin_C_mcg}", "{Vitamin_D_mcg}", "{Fiber_g}", "{Calories}")
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

        insert_recipe_ingredient = '''INSERT INTO Recipe_Ingredients_STG (RecipeID, IngredientID, Quantity, QuantityUnit)
        VALUES (
            "{RecipeID}",
            "{IngredientID}',
            "{Quantity}",
            "{QuantityUnit}"
        )
        '''.format(**RecipeIngredient)

        cursor.execute(insert_recipe_ingredient)


    for Ingredient in Recipe["Ingredients"]:
        add_ingredient(db, cursor, Ingredient)

    db.commit()


    


## ------------- Testing Workspace ----------------

db, cursor = sql_connect('RecipePublic.db')
##add_user(db, cursor,  "Jane", "Doe")
##add_ingredient(db, cursor, IngredientName = "Banana", Description = "An elongated, edible fruit, botanically a berry")

recipes = parse_recipes(1)
for recipe in recipes:
    add_recipe(db, cursor, recipe)

##with open('sql_bcknd/test.sql', 'r') as sql_file:
    ##sql_script = sql_file.read()

##cursor.execute(sql_script)

##result = cursor.fetchall()

#3for row in result:
    ##print(row)

