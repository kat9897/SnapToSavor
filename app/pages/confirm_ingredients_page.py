from taipy.gui import navigate
import os

# Bindings
# here = os.path.dirname(os.path.abspath(__file__))
# image = os.path.join(here, "./img/image-missing.svg") # default image without any user input
selected_files = None
ingredients = []
num_ingred = 1

confirm_ingredients_page="""
<|layout|columns=2 2|
<|card card-bg|
<center>
<|{selected_files}|image|>
</center>
|>
<|card card-bg|
Confirm <|{num_ingred}|text|> ingredient(s):\n
<|{ingredients[0]}|>
|>
<|Confirm|button|on_action=confirmed_ingred|>
|>
"""

def update_num_ingred(state):
    num_ingred = num_ingred + 1

def confirmed_ingred(state):
    print(state.image)
    # navigate(state, "recipes")


