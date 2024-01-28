found_recipes_page = """
<|layout|columns=1 3|
<|card card-bg|
<|card card-bg| {.red}
##  Ingredients
|>
|>
<|card card-bg|
## Recipes
<|part|render=nonempty|>
|>
|>
"""

def nonempty():
    return 