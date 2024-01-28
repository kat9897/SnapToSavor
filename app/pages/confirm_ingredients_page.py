from taipy.gui import navigate
from .landing_page import *
import os

# Bindings
# here = os.path.dirname(os.path.abspath(__file__))
# image = os.path.join(here, "./img/image-missing.svg") # default image without any user input
num_ingred = 0

confirm_ingredients_page="""
<|layout|columns=2 3|
<|card card-bg|
<|{selected_files}|image|> 
|>
<|card card-bg|
<|Confirm {num_ingred} ingredient(s):|>\n
|>
<|Confirm|button|on_action=confirmed_ingred|>
|>
"""

# |label="Uploaded Fridge Image"

def confirmed_ingred(state):
    # print(image)
    navigate(state, "recipes")


def resize_img(img):
    '''
    Resize the image img to a desired size.
    '''
    pass

