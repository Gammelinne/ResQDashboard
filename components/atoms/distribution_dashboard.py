from shiny import ui, Inputs, Outputs, Session, render
import utils.data_handler
import utils.plot_handler
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
    ),
    ui.output_plot("distribution_plot"),
    ui.output_data_frame("distribution_table")
)

def distribution_dashboard_server(input: Inputs, output: Outputs, session: Session, data_handler : utils.data_handler, qi_value: utils.data_handler,plot_handler: utils.plot_handler,  dataframe: utils.data_handler):
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

    @output
    @render.ui
    def distribution_plot():
        #data_csv = dataframe
        qi_name =  input["qi_select_distribution"].get() 
        #site_names = input["list_site_distribution"].get() 
        gender = input["list_gender_distribution"].get() 
        # imagine_done= input["list_imagine_distribution"].get()
        # prenotification = input["list_prenotifiction_distribution"].get()
        # discharge_mrs = input["list_mrs_distribution"].get()
        # year_quarter = input["slider_x_distribution"].get()
        # qi_error = input["checkbox_error_distribution"].get()
        # qi_trend = input["checkbox_trend_distribution"].get()
        # compare_country = input["checkbox_compare_contry_distribution"].get()
        # aggregation_type = input["aggregation_type_distribution"].get()
        data = dataframe[dataframe["QI"] == qi_value[qi_name]["referenceDataColumns"]].dropna()
        data = data.groupby("YQ")["Value"].mean()
        x = data.index
        y = data.values 
        return plot_handler.plot_distribution(x, y)
    
    @output
    @render.data_frame
    def distribution_table():
        selected_columns = ["site_country", "site_name", "site_id", "YQ", "Value"]
        return dataframe[dataframe["QI"] == qi_value[input["qi_select_timeline"].get()]["referenceDataColumns"]][selected_columns].dropna()