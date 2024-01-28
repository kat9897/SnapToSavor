import sqlite3

from .confirm_ingredients_page import *
from app.backend.sql_func import *

db = sql_connect('recipes')

food_name_test = food_name_test

items = get_recipe_by_ingredient(db[0], db[1], food_name_test)

found_recipes_page = """
<|layout|columns=1 3|
<|card card-bg|
##  Ingredients
<|card card-bg|
{food_name_test[0]}\n
{food_name_test[1]}\n
|>
|>
<|card card-bg|
## Recipes

<|layout|columns=1 1 1|
<|card card-bg|
{items[0][1]}
{items[0][4]|image}
{items[0][6]}
|>
<|card card-bg|
{items[1][1]}
{items[1][4]|image}
{items[1][6]}
<|app/pages/img/banana-baby-producto-caribbean-exotics.png|image|>
|>
<|card card-bg|
{items[2][1]}
{items[2][4]|image}
{items[2][6]}
<|app/pages/img/banana.jpg|image|>
|>
|>
|>
|>
"""
