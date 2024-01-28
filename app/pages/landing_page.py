from taipy.gui import navigate
from food_api import get_ingredients

# Bindings
selected_files = None
value = "Search for recipe..."

landing_page="""
<|{selected_files}|file_selector|label=Upload File|on_action=uploaded_files|extensions=.jpg,.jpeg,.png|drop_message=Drop Message|>
## Search for recipe
<|{value}|input|><|find|button|on_action=uploaded_files|>
"""

def uploaded_files(state):
    state.ingredients = get_ingredients(state.selected_files)
    state.num_ingred = len(state.ingredients)
    navigate(state, to="confirm")

