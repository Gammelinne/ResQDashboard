from shiny import ui, Inputs, Outputs, Session, render
import utils.data_handler
from components.atoms.macros.plot_characteristics import plot_characteristics_ui
from components.atoms.macros.values_filter import values_filter_ui
comparison_dashboard_ui = ui.layout_sidebar(
    ui.sidebar(
        ui.row(
            ui.column(
                6,
                plot_characteristics_ui("comparison")
            ),
            ui.column(
                6,
                values_filter_ui("comparison")
            ),
        ),
        width=500,
        title="comparison",
    ),
    ui.output_plot("comparison_plot")
)

def comparison_dashboard_server(input: Inputs, output: Outputs, session: Session, data_handler : utils.data_handler):
    qi_value = data_handler.get_qi_data()
    
    @output
    @render.ui
    def x_qi_selector_comparison():
        return ui.tooltip(ui.input_select(id="qi_select_comparison", label="Select x-axis", choices=list(qi_value.keys())), "", id="x_qi_tooltip_comparison")

    @output
    @render.ui
    def x_selected_qi_value_comparison():
        return update_tooltips("x_qi_tooltip_comparison", input["qi_select_comparison"].get())

    @output
    @render.ui    
    def comparison_selector_comparison():
        return ui.tooltip(ui.input_select(id="comparison_select_comparison", label="Select factor to compare data", choices=list(qi_value.keys())), "", id="comparison_tooltip_comparison")
    
    @output
    @render.ui
    def selected_comparison_value_comparison():
        return update_tooltips("comparison_tooltip_comparison", input["comparison_select_comparison"].get())
        
    def update_tooltips(tooltips_name, selected_value):
        if type(qi_value[selected_value]['commentsInfo']) is str:
            return ui.update_tooltip(tooltips_name, f"{selected_value}: {qi_value[selected_value]['commentsInfo']}")
        else:
            return ui.update_tooltip(tooltips_name, f"{selected_value}")
        
    @output
    @render.ui
    def factor_to_compare_comparison():
        factor_choice = [ "None", "Gender", "mRS on discharge", "3-month mRS", "Arrival pre-notified", "Imaging done", "Physiotherapy initiated", "Test for dysphagia screen"]
        return ui.input_select(id="factor_to_compare", label="Select factor to colour data", choices=factor_choice)