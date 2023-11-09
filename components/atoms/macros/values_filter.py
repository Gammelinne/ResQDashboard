from shiny import ui

def values_filter_ui(id):
    quarter_choice = ["2018 Q1","2018 Q2","2018 Q3","2018 Q4","2019 Q1","2019 Q2","2019 Q3","2019 Q4","2020 Q1","2020 Q2","2020 Q3","2020 Q4","2021 Q1","2021 Q2","2021 Q3","2021 Q4","2022 Q1","2022 Q2","2022 Q3","2022 Q4"]
    return ui.card(
        ui.card_header(
            ui.h5("Filter by values"),
        ),
        ui.input_slider(f"slider_x_{id}", "Filter values of x-axis variable (slider shows range of values in x-axis variable)", 10,100, [10,50] ),
        ui.input_checkbox_group(f"list_quarters_{id}", "Quarters shown in plot", choices=quarter_choice, selected=quarter_choice)
    ),
