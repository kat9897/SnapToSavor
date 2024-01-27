from taipy.gui import navigate

# Bindings
selected_files = None

value = "Search for recipe..."
content = None

landing_page="""
<|{selected_files}|file_selector|label=Upload File|on_action=uploaded_files|extensions=.jpg,.jpeg,.png|drop_message=Drop Message|>
#Search for recipe:
<|{value}|input|>
"""

def uploaded_files(state):
    navigate(state, to="confirm")

