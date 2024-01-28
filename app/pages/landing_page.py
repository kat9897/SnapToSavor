from taipy.gui import navigate 
from backend.sql_func import *

# Bindings
selected_files = None
recipe_from_search = None
value = None

landing_page="""
<|{selected_files}|file_selector|label=Upload File|on_action=uploaded_files|extensions=.jpg,.jpeg,.png|drop_message=Drop Message|>
#Search for recipe:
<|{recipe_from_search}|input|label=Search for recipe|><|find|button|on_action=search_recipe|>
"""

def uploaded_files(state):
    navigate(state, to="confirm")

def search_recipe(state):
    recipe_from_search = get_recipe_by_ingredient(sql_connect('RecipePublic.db'), value)