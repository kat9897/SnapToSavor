from taipy.gui import navigate
from .landing_page import *
from food_api import *

num_ingred = 0
selected_files = selected_files

confirm_ingredients_page="""
<|layout|columns=2 3|
<|card card-bg|
<|{selected_files}|image|> 
|>
<|card card-bg|
<|Confirm {num_ingred} ingredient(s):|>\n
<|layout|columns=2 1 1|
<|edit|>
<|del|>
|>
|>
<|Confirm|button|on_action=confirmed_ingred|>
|>
"""

# food_name_test = get_ingredients(selected_files)

# <|{food_name_test}|>

# |label="Uploaded Fridge Image"

def confirmed_ingred(state):
    # print(image)
    navigate(state, "recipes")
