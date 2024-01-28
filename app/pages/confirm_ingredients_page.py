from taipy.gui import navigate
from .landing_page import *
from food_api import *

# Bindings
# here = os.path.dirname(os.path.abspath(__file__))
# image = os.path.join(here, "./img/image-missing.svg") # default image without any user input
selected_files = None
ingredients = []
num_ingred = 1

confirm_ingredients_page="""
<|layout|columns=2 3|
<|card card-bg|
<center>
<|{selected_files}|image|>
</center>
|>
<|card card-bg|
<<<<<<< HEAD
<|Confirm {num_ingred} ingredient(s):|>\n
<|{food_name_test}|>
=======
Confirm <|{num_ingred}|text|> ingredient(s):\n
<|{ingredients[0]}|>
>>>>>>> ad066fef260bbcd0f37183683d2bc9bc355ae8be
|>
<|Confirm|button|on_action=confirmed_ingred|>
|>
"""

<<<<<<< HEAD
food_name_test = get_ingredients(selected_files)

# <|{food_name_test}|>

# |label="Uploaded Fridge Image"
=======
def update_num_ingred(state):
    num_ingred = num_ingred + 1
>>>>>>> ad066fef260bbcd0f37183683d2bc9bc355ae8be

def confirmed_ingred(state):
    navigate(state, "recipes")
