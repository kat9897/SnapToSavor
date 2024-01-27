from taipy.gui import navigate

# Bindings
image = "app/pages/img/image-missing.svg" # default image without any user input
num_ingred = 0

confirm_ingredients_page="""
<|layout|columns=2 2|
<|card card-bg|
<|{image}|image|label="Uploaded Fridge Image"|>
|>
<|
<|
<|card card-bg|
<|Confirm {num_ingred} ingredient(s):|>\n
|>
<|{selected_files}|file_selector|label=Upload File|on_action=upload_files|extensions=.jpg,.jpeg,.png|drop_message=Drop Message|multiple|>
|>
|>
"""

def upload_files(state):
    navigate(state, "recipes")


