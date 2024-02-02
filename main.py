from taipy import Gui

from pages.landing_page import landing_page
from pages.found_recipes_page import found_recipes_page
from pages.root_page import *
from pages.confirm_ingredients_page import confirm_ingredients_page
from food_api import *

# Bindings
value = ""
ingredients = ['avocado', 'apple', 'broccoli', 'berries', 'ham meat', 'pomegranate', 'lemon', 'orange', 'pomegranate', 'onion', 'broccoli', 'ketchup sauce', 'ham meat', 'broccoli', 'oatmeal porridge', 'ham meat', 'ham meat', 'brown rice', 'ham meat']
selected_files = None
num_ingred = 1

pages = {
    "/": root_page,
    "ingredients": landing_page,
    "confirm": confirm_ingredients_page,
    "recipes": found_recipes_page
}

stylekit = {
  "color_primary": "#F87F7F",
  "color_secondary": "#C0FFE",
}

#if __name__ == "__main__":
Gui(pages=pages).run(debug=True, use_reloader=True, port=8080, stylekit=stylekit, dark_mode=False, title="SnapToSavor")


