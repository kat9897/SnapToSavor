from taipy.gui import navigate

# Bindings
selected_files = None

landing_page="""
<|{selected_files}|file_selector|label=Upload File|on_action=uploaded_files|extensions=.jpg,.jpeg,.png|drop_message=Drop Message|>
"""

def uploaded_files(state):
    navigate(state, "confirm")

