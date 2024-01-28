from taipy.gui import navigate
import os
from food_api import *

# Bindings
#here = os.path.dirname(os.path.abspath(__file__))
#image = os.path.join(here, "./img/image-missing.svg") # default image without any user input
num_ingred = 0

confirm_ingredients_page="""
<|layout|columns=2 2|
<|card card-bg|
<|{selected_files}|image|label="Uploaded Fridge Image"|>
|>
<|card card-bg|
<|Confirm {num_ingred} ingredient(s):|>\n
<|{food_name_test}|>
|>
<|Confirm|button|on_action=confirmed_ingred|>
|>
"""

def confirmed_ingred(state):
    print(image)
    # navigate(state, "recipes")


