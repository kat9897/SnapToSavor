from taipy import Gui

from pages.landing_page import *
from pages.found_recipes_page import *
from pages.root_page import *
from pages.confirm_ingredients_page import *
from food_api import *

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

if __name__ == "__main__":
    
    Gui(pages=pages).run(debug=True, use_reloader=True, port=8080, stylekit=stylekit, dark_mode=False)



from taipy import Gui

from pages.landing_page import *
from pages.found_recipes_page import *
from pages.root_page import *
from pages.confirm_ingredients_page import *

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

if __name__ == "__main__":
    Gui(pages=pages).run(debug=True, use_reloader=True, port=8081, stylekit=stylekit, dark_mode=False)


