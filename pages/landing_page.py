from taipy.gui import navigate
from food_api import get_ingredients
import taipy.gui.builder as tgb
import pandas as pd

def uploaded_files(state):
    # Change once you have a more permanent ai
    #state.ingredients = get_ingredients(state.selected_files)
    state.num_ingred = len(state.ingredients)
    state.ingredients_table = create_ingred_table(state)
    navigate(state, to="confirm")

def create_ingred_table(state):
    food_df = {
        "Ingredients": []
    }
    for ingred in state.ingredients:
        # Unique ingredients
        if ingred not in food_df["Ingredients"]:
            food_df["Ingredients"].append(ingred)
        else:
            state.num_ingred -= 1
    return pd.DataFrame(food_df)

with tgb.Page() as landing_page:
    with tgb.part(class_name="card card-bg"):
        tgb.file_selector(content="{selected_files}", label="Upload File", extensions=".jpg,.jpeg,.png", on_action=uploaded_files)
    #tgb.html("h2", "Search Function")
    #tgb.input(label="Search for recipe...", value="{value}")
    #tgb.button("Search", on_action=uploaded_files)

# landing_page="""
# <|{selected_files}|file_selector|label=Upload File|on_action=uploaded_files|extensions=.jpg,.jpeg,.png|drop_message=Drop Message|>
# ## Search for recipe
# <|{value}|input|><|find|button|on_action=uploaded_files|>
# """



