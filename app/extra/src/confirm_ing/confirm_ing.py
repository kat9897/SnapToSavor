from taipy import *

path = ""
content = "src/img/MBTI.png" # insert user uploaded image here

page_file = """

<|{content}|image|width="400px"|height="400px"|>



"""
# ![picture](/img/MBTI.png)
# <|{content}|image|>
# <img src=content alt="image" width="50%" height="auto">
# <|{path}|file_selector|extensions=.jpg|label=Upload .txt file|on_action=analyze_file|> <|{f'Downloading {treatment}%...'}|>


pages = {"/":"<|navbar|id=nav|>",
         "home":'',
         "ingredients":page_file,
         "recipes":''}


stylekit = {
  "color_primary": "#000000",
  "color_secondary": "#FDA2A2",
}

# <|toggle|theme|>

Gui(pages=pages,css_file="src/confirm_ing/confirm_ing.css").run(dark_mode=False, stylekit=stylekit)