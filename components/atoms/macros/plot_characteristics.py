from shiny import ui, render, Inputs, Outputs, Session
import utils.data_handler

def plot_characteristics_ui(id):
    return ui.card(
        ui.h4("Plot characteristics"),
        ui.output_ui(f"qi_selector_{id}"),
        ui.output_ui(f"selected_qi_value_{id}"),
    ),

def plot_characteristics_server(input: Inputs, output: Outputs, session: Session, data_handler : utils.data_handler, id: str):

    qi_value = data_handler.get_qi_data()
    input_id = f"qi_select_{id}"
    tooltip_id = f"qi_tooltip_{id}"
    
    @output
    @render.ui
    def qi_selector_timeline():
        return ui.tooltip(ui.input_select(id=f"{input_id}", label="bob", choices=list(qi_value.keys())), "", id=tooltip_id)

    @output
    @render.ui
    def selected_qi_value_timeline():
        selected_value = input[input_id].get()
        if type(qi_value[selected_value]['commentsInfo']) is str:
            return ui.update_tooltip(tooltip_id, f"{selected_value}: {qi_value[selected_value]['commentsInfo']}")
        else:
            return ui.update_tooltip(tooltip_id, f"{selected_value}")
