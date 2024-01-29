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
<|Confirmed {num_ingred} ingredient(s):|>\n
<|{ingredients}|>
|>
<|Confirm|button|class_name=success|on_action=confirmed_ingred|>
<|Delete|button|class_name=error|on_action=delete_ingred|>
|>
"""

def update_num_ingred(state):
    num_ingred = num_ingred + 1

def confirmed_ingred(state):
    navigate(state, "recipes")

def delete_ingred(state):
    navigate(state, to="ingredients")
