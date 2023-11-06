# Page1.py
from shiny import ui

dashboard_ui = ui.page_fluid(
    ui.h1("Contenu de l'onglet 1")
)

def page_1_server(input, output, session):
    # Aucune logique particulière pour cet exemple
    pass
