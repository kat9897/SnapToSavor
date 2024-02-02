from taipy.gui import navigate
from .landing_page import *
from food_api import *

# Extension Docs: https://docs.taipy.io/en/develop/manuals/gui/extension/
# All types of taipy.gui.builder classes: https://docs.taipy.io/en/develop/manuals/reference/pkg_taipy.gui.builder/

# Bindings
# here = os.path.dirname(os.path.abspath(__file__))
# image = os.path.join(here, "./img/image-missing.svg") # default image without any user input

def confirmed_ingred(state):
    print(state.selected_files)
    print(state.num_ingred)
    print(state.ingredients)
    navigate(state, "recipes")

def delete_ingred(state):
    state.selected_files = None
    navigate(state, to="ingredients")

with tgb.Page() as confirm_ingredients_page:
    with tgb.layout("2 3"):
        with tgb.part(class_name="card card-bg"):
            tgb.image(content="{selected_files}", class_name="center")
        with tgb.part(class_name="card card-bg"):
            tgb.text(value="Confirmed Ingredient(s): {num_ingred}")
            tgb.table(data="{ingredients_table}", editable=True)
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
