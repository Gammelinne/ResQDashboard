from shiny import ui, Inputs, Outputs, Session, render
import utils.data_handler
from components.atoms.macros.plot_characteristics import plot_characteristics_ui
from components.atoms.macros.subgroups_filter import subgroups_filter_ui
from components.atoms.macros.compare import compare_ui
from components.atoms.macros.values_filter import values_filter_ui

timeline_dashboard_ui = ui.layout_sidebar(
    ui.sidebar(
        ui.row(
            ui.column(
                6,
                plot_characteristics_ui("timeline"),
                subgroups_filter_ui("timeline")
            ),
            ui.column(
                6,
                compare_ui("timeline"),
                values_filter_ui("timeline")
            )
        ),
        width=500,
        title="Timeline",
    ),
    ui.output_plot("timeline_plot")
)

def timeline_dashboard_server(input: Inputs, output: Outputs, session: Session, data_handler : utils.data_handler):

    qi_value = data_handler.get_qi_data()
    
    @output
    @render.ui
    def y_qi_selector_timeline():
        return ui.tooltip(ui.input_select(id="qi_select_timeline", label="Select y-axis", choices=list(qi_value.keys())), "", id="y_qi_tooltip_timeline")

    @output
    @render.ui
    def y_selected_qi_value_timeline():
        selected_value = input["qi_select_timeline"].get()
        if type(qi_value[selected_value]['commentsInfo']) is str:
            return ui.update_tooltip("y_qi_tooltip_timeline", f"{selected_value}: {qi_value[selected_value]['commentsInfo']}")
        else:
            return ui.update_tooltip("y_qi_tooltip_timeline", f"{selected_value}")
    
    @output
    @render.ui
    def aggregation_type_timeline():
        aggregation_choice=["median","mean", "standard deviation", "minimum", "maximum"]
        return ui.input_select("aggregation_type_timeline", "Select aggregation type", aggregation_choice),

    @output
    @render.ui
    def checkbox_error_bar_timeline():
        return ui.input_checkbox("error_bar_timeline", "Show error bars")
    
    @output
    @render.ui
    def checkbox_trend_timeline():
        return ui.input_checkbox("trend_timeline", "Show trend")