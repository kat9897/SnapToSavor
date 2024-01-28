found_recipes_page = """
<|layout|columns=1 3|
<|card card-bg|
##  Ingredients
<|card card-bg| {.red}
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