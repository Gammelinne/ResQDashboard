from shiny import ui

def compare_ui(id):
    site_choice=["General", "Hope", "Paradise", "Rose", "Angelvale", "Mercy"]
    return ui.card(
        ui.card_header(
            ui.h5("Compare"),
        ),
        ui.input_checkbox(f"checkbox_compare_contry_{id}", "Compare with country"),
        ui.input_checkbox_group(id=f"list_site_{id}", label="Compare with hospitals", choices=site_choice),
    ),
