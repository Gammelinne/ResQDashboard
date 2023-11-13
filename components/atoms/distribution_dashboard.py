from shiny import ui, Inputs, Outputs, Session, render
import utils.data_handler
from components.atoms.macros.plot_characteristics import plot_characteristics_ui
from components.atoms.macros.subgroups_filter import subgroups_filter_ui
from components.atoms.macros.compare import compare_ui
from components.atoms.macros.values_filter import values_filter_ui

distribution_dashboard_ui = ui.layout_sidebar(
    ui.sidebar(
        ui.row(
            ui.column(
                6,
                plot_characteristics_ui("distribution"),
                subgroups_filter_ui("distribution")
            ),
            ui.column(
                6,
                compare_ui("distribution"),
                values_filter_ui("distribution")
            )
        ),
        width=500,
        title="Distribution",
    )
)

def distribution_dashboard_server(input: Inputs, output: Outputs, session: Session, data_handler : utils.data_handler):
    qi_value = data_handler.get_filter_data()
    
    @output
    @render.ui
    def x_qi_selector_distribution():
        return ui.tooltip(ui.input_select(id="qi_select_distribution", label="Select y-axis", choices=list(qi_value.keys())), "", id="x_qi_tooltip_distribution")

    @output
    @render.ui
    def x_selected_qi_value_distribution():
        selected_value = input["qi_select_distribution"].get()
        if type(qi_value[selected_value]['commentsInfo']) is str:
            return ui.update_tooltip("x_qi_tooltip_distribution", f"{selected_value}: {qi_value[selected_value]['commentsInfo']}")
        else:
            return ui.update_tooltip("x_qi_tooltip_distribution", f"{selected_value}")
        
    @output
    @render.ui
    def checkbox_median_distribution():
        return ui.input_checkbox(f"checkbox_median_distribution", "Show median line"),

    @output
    @render.ui
    def checkbox_mean_distribution():
        return ui.input_checkbox(f"checkbox_mean_distribution", "Show median line"),