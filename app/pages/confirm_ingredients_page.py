from taipy.gui import navigate

# Bindings
image = "app/pages/img/missing_img.jpg" # default image without any user input

num_ingred = 0

confirm_ingredients_page="""
<|layout|columns=2 3|
<|card card-bg|
<|{image}|image|> 
|>
<|
<|
<|card card-bg|
<|Confirm {num_ingred} ingredient(s):|>\n
|>
|>
|>
<|Confirm|button|on_action=confirmed_ingred|>
"""

# |label="Uploaded Fridge Image"

def confirmed_ingred(state):
    navigate(state, "recipes")


def resize_img(img):
    '''
    Resize the image img to a desired size.
    '''
    pass

