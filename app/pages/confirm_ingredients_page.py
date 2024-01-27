from taipy.gui import navigate

# Bindings
image = r"C:\Users\katri\OneDrive\Pictures\background.jpg"
num_ingred = 0

confirm_ingredients_page="""
<|layout|columns=2 2|
<|
<|{image}|image|label="Uploaded Fridge Image"|>
|>
<|
<|Confirm {num_ingred} ingredient(s):|>
|>
|>
<|Confirm|button|on_action=confirmed_ingred|>
"""

def confirmed_ingred(state):
    navigate(state, "recipes")

