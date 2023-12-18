from shiny import ui, Inputs, Outputs, Session, render
import pandas as pd
import utils.data_handler
from components.atoms.section_accordion import section_ui, section_server

csv = pd.read_csv("assets/filter.csv")
categories = csv['QICategory'].unique()
    
sections = [
    ui.accordion_panel(f"Section {categorie}", section_ui(categorie, categorie))
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
                ui.output_text('total_patient'),
                class_="rounded"
            ),
            ui.card(
                ui.output_text('total_patient_range'),
                class_="rounded"
            ),
            class_='text-center',
        ),
        ui.accordion(*sections, id="acc"),
    ),
)

def dashboard_server(input: Inputs, output: Outputs, session: Session, data_handler: utils.data_handler, quarter_choice):
    [section_server(x) for x in categories]

    @output
    @render.text
    def total_patient():
        dataframe = data_handler.get_data()
        total_patient = dataframe["subject_id"].unique()
        return f"{len(total_patient)} total patients"
    
    @output
    @render.text
    def total_patient_range():
        dataframe = data_handler.get_data()
        total_patient = dataframe["subject_id"].unique()
        return f"{round(len(total_patient)/len(quarter_choice))} total patient in range"
    
    