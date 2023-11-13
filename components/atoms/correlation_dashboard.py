from shiny import ui, Inputs, Outputs, Session, render
import utils.data_handler
from components.atoms.macros.plot_characteristics import plot_characteristics_ui
from components.atoms.macros.subgroups_filter import subgroups_filter_ui
from components.atoms.macros.values_filter import values_filter_ui

correlation_dashboard_ui = ui.layout_sidebar(
    ui.sidebar(
        ui.row(
            ui.column(
                6,
                plot_characteristics_ui("correlation"),
                subgroups_filter_ui("correlation")
            ),
            ui.column(
                6,
                values_filter_ui("correlation")
            )
        ),
        width=500,
        title="Correlation",
    )
)

def correlation_dashboard_server(input: Inputs, output: Outputs, session: Session, data_handler : utils.data_handler):
    qi_value = data_handler.get_filter_data()
    
    @output
    @render.ui
    def x_qi_selector_correlation():
        return ui.tooltip(ui.input_select(id="x_qi_select_correlation", label="Select x-axis", choices=list(qi_value.keys())), "", id="x_qi_tooltip_correlation")

    @output
    @render.ui
    def x_selected_qi_value_correlation():
        return update_tooltips("x_qi_tooltip_correlation", input["x_qi_select_correlation"].get())

    @output
    @render.ui    
    def y_qi_selector_correlation():
        return ui.tooltip(ui.input_select(id="y_qi_select_correlation", label="Select y-axis", choices=list(qi_value.keys())), "", id="y_qi_tooltip_correlation")
    
    @output
    @render.ui
    def y_selected_qi_value_correlation():
        return update_tooltips("y_qi_tooltip_correlation", input["y_qi_select_correlation"].get())
        
    def update_tooltips(tooltips_name, selected_value):
        if type(qi_value[selected_value]['commentsInfo']) is str:
            return ui.update_tooltip(tooltips_name, f"{selected_value}: {qi_value[selected_value]['commentsInfo']}")
        else:
            return ui.update_tooltip(tooltips_name, f"{selected_value}")
        
    @output
    @render.ui
    def factor_to_compare_correlation():
        factor_choice = [ "None", "Gender", "mRS on discharge", "3-month mRS", "Arrival pre-notified", "Imaging done", "Physiotherapy initiated", "Test for dysphagia screen"]
        return ui.input_select(id="factor_to_compare", label="Select factor to colour data", choices=factor_choice)