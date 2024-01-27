from taipy.gui import navigate
from PIL import Image

# Bindings
image = Image.open("app/pages/img/missing_img.jpg") # default image without any user input
resized_image = image.resize(400,400)
resized_image.save("app/pages/img/missing_img.jpg")

num_ingred = 0

confirm_ingredients_page="""
<|layout|columns=2 2|
<|card card-bg|
<|{resized_image}|image|label="Uploaded Fridge Image"|>
|>
<|
<|
<|card card-bg|
<|Confirm {num_ingred} ingredient(s):|>\n
|>
<|{selected_files}|file_selector|label=Upload File|on_action=confirmed_ingred|extensions=.jpg,.jpeg,.png|drop_message=Drop Message|multiple|>
|>
|>
<|Confirm|button|on_action=confirmed_ingred|>
"""

def confirmed_ingred(state):
    navigate(state, "recipes")


