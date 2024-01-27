from taipy import *


path = ""
content = "src/img/MBTI.png" #user uploaded image here

page_file = """
<|{content}|image|>


"""
# [<img=content >](content)
# <|{path}|file_selector|extensions=.jpg|label=Upload .txt file|on_action=analyze_file|> <|{f'Downloading {treatment}%...'}|>

pages = {"/":"<center>\n<|navbar|>\n</center>",
         "home":'',
         "ingredients":page_file}


# <|toggle|theme|>

Gui(pages=pages).run()