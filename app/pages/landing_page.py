from taipy.gui import navigate

# Bindings
selected_files = None

value = "Search for recipe..."
content = 

landing_page="""
<|{selected_files}|file_selector|label=Upload File|on_action=uploaded_files|extensions=.jpg,.jpeg,.png|drop_message=Drop Message|>
#Search for recipe:
<|{value}|input|> <|{content}| image |label=Search | on_action=confirmed_ingred>
"""

def uploaded_files(state):
    navigate(state, to="confirm")

