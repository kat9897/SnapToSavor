from taipy.gui import navigate

# Bindings
image = "app/pages/img/MBTI.png"
num_ingred = 0

confirm_ingredients_page="""
<|layout|columns=2 2|
<|
<|{image}|image|label="Uploaded Fridge Image"|>
|>
<|
<|Confirm {num_ingred} ingredient(s):|>
|>
<|{selected_files}|file_selector|label=Upload File|on_action=upload_files|extensions=.jpg,.jpeg,.png|drop_message=Drop Message|multiple|>
|>
"""

def upload_files(state):
    navigate(state, "recipes")


