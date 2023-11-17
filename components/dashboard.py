from shiny import ui, render, Inputs, Outputs, Session, reactive, module
import pandas as pd
import matplotlib.pyplot as plt
import utils.data_handler
from components.atoms.section_accordion import section_ui, section_server

csv = pd.read_csv("assets/filter.csv")
categories = csv['QICategory'].unique()
    
sections = [
    ui.accordion_panel(f"Section {categorie}", section_ui(categorie))
    for categorie in categories
]

dashboard_ui = ui.page_fluid(
    ui.card(
        ui.card_header(
            ui.h3('Hospital overview'),
        ),
        ui.layout_column_wrap(
            ui.card(
                ui.h5('Open Hospital'),
                class_="rounded"
            ),
            ui.card(
                ui.h5('36 patients discharged in range'),
                class_="rounded"
            ),
            ui.card(
                ui.h5('495 total discharged patients'),
                class_="rounded"
            ),
            class_='text-center',
        ),
        ui.accordion(*sections, id="acc", height=len(categories) * 100),
    ),
)

def dashboard_server(input: Inputs, output: Outputs, session: Session, data_handler: utils.data_handler):
    [section_server(x) for x in categories]