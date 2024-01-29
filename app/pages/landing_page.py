from taipy.gui import navigate
from food_api import get_ingredients
import taipy.gui.builder as tgb

# Bindings
selected_files = None
value = ""

def uploaded_files(state):
    state.ingredients = get_ingredients(state.selected_files)
    state.num_ingred = len(state.ingredients)
    navigate(state, to="confirm")

with tgb.Page() as landing_page:
    tgb.file_selector(content="{selected_files}", label="Upload File", on_action=uploaded_files, extensions=".jpg,.jpeg,.png")
    tgb.html("h2", "Search Function")
    tgb.input(label="Search for recipe...", value="{value}")
    tgb.button("Search", on_action=uploaded_files)

# landing_page="""
# <|{selected_files}|file_selector|label=Upload File|on_action=uploaded_files|extensions=.jpg,.jpeg,.png|drop_message=Drop Message|>
# ## Search for recipe
# <|{value}|input|><|find|button|on_action=uploaded_files|>
# """



