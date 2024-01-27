from taipy.gui import navigate

# Bindings
selected_files = None

value = "Search for recipe..."

landing_page="""
<|{selected_files}|file_selector|label=Upload File|on_action=uploaded_files|extensions=.jpg,.jpeg,.png|drop_message=Drop Message|>
#Search for recipe:
<|{value}|input|><|find|button|on_action=uploaded_files|>
"""

def uploaded_files(state):
    navigate(state, to="confirm")

