from taipy.gui import navigate, notify
from .landing_page import *
from food_api import *

# Extension Docs: https://docs.taipy.io/en/develop/manuals/gui/extension/
# All types of taipy.gui.builder classes: https://docs.taipy.io/en/develop/manuals/reference/pkg_taipy.gui.builder/
# Using Tables Ex: https://docs.taipy.io/en/release-3.0/knowledge_base/tips/using_tables/
# Tables class: https://docs.taipy.io/en/latest/manuals/gui/viselements/table/

# Bindings
# here = os.path.dirname(os.path.abspath(__file__))
# image = os.path.join(here, "./img/image-missing.svg") # default image without any user input

def confirmed_ingred(state):
    # print(state.selected_files)
    # print(state.num_ingred)
    # print(state.ingredients_table)
    navigate(state, "recipes")

def delete_ingred(state):
    state.selected_files = None
    state.num_ingred = 0
    state.ingredients_table = []
    state.ingredients = []
    navigate(state, to="ingredients")

def food_df_on_edit(state, var_name, payload):
    index = payload["index"] # row index
    col = payload["col"] # column name
    value = payload["value"] # new value cast to the column type
    #user_value = payload["user_value"] # new value as entered by the user
    # Note: value and user_value are the same!

    # state.ingredients_table.loc[index, col] = value #  Don't do this! B/c they said so
    old_value = state.ingredients_table.loc[index, col]
    new_food_df = state.ingredients_table.copy()
    new_food_df.loc[index, col] = value
    state.ingredients_table = new_food_df
    notify(state, "I", f"Edited value from '{old_value}' to '{value}'. (index '{index}', column '{col}')")

with tgb.Page() as confirm_ingredients_page:
    with tgb.layout("2 3"):
        with tgb.part(class_name="card card-bg"):
            tgb.image(content="{selected_files}", class_name="center")
        with tgb.part(class_name="card card-bg"):
            tgb.text(value="Confirmed Ingredient(s): {num_ingred}")
            tgb.table(data="{ingredients_table}", on_edit=food_df_on_edit)
        tgb.button("Confirm", class_name="success", on_action=confirmed_ingred)
        tgb.button("Cancel", class_name="error", on_action=delete_ingred)

# confirm_ingredients_page="""
# <|layout|columns=2 3|
# <|card card-bg|
# <center>
# <|{selected_files}|image|>
# </center>
# |>
# <|card card-bg|
# <|Confirmed {num_ingred} ingredient(s):|>\n
# <|{ingredients}|>
# |>
# <|Confirm|button|class_name=success|on_action=confirmed_ingred|>
# <|Delete|button|class_name=error|on_action=delete_ingred|>
# |>
# """
