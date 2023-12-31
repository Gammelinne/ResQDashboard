from shiny import ui, Inputs, Outputs, Session, render
import utils.plot_handler
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
    ui.output_plot("timeline_plot"),
    ui.output_data_frame("timeline_table")
)

def timeline_dashboard_server(input: Inputs, output: Outputs, session: Session, data_handler : utils.data_handler, qi_value: utils.data_handler, plot_handler: utils.plot_handler, dataframe: utils.data_handler):
    @output
    @render.ui
    def y_qi_selector_timeline():
        return ui.tooltip(ui.input_select(id="qi_select_timeline", label="Select y-axis", choices=list(qi_value.keys()), selected=""), "", id="y_qi_tooltip_timeline")

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
    @render.data_frame
    def timeline_table():
        selected_columns = ["site_country", "site_name", "site_id", "YQ", "Value"]
        return dataframe[dataframe["QI"] == qi_value[input["qi_select_timeline"].get()]["referenceDataColumns"]][selected_columns].dropna()
    
    @output
    @render.ui
    def checkbox_error_bar_timeline():
        return ui.input_checkbox("error_bar_timeline", "Show error bars")
    
    @output
    @render.ui
    def checkbox_trend_timeline():
        return ui.input_checkbox("trend_timeline", "Show trend")
    
        

    @output
    @render.plot
    def timeline_plot():
        #data_csv = dataframe
        qi_name =  input["qi_select_timeline"].get() #String (referenceDataColumns) default: subject_id
        #site_names = input["list_site_timeline"].get() #Array (["General", "Hope", "Paradise", "Rose", "Angelvale", "Mercy"], ()) default: ()
        gender = input["list_gender_timeline"].get() #Array (["Male", "Female"] or ()) default: ["Male", "Female"] 
        # imagine_done= input["list_imagine_timeline"].get() #Array ([Done, "Not done"], ()) default: [Done, "Not done"]
        # prenotification = input["list_prenotifiction_timeline"].get() #Array (["Prenotified", "Not Prenotified"], ()) default: ["Prenotified", "Not Prenotified"]
        # discharge_mrs = input["list_mrs_timeline"].get() #Array (["1", "2","3","4","5","6"], ()) default: ["1", "2","3","4","5","6"]
        # year_quarter = input["slider_x_timeline"].get() #Array (["2018 Q1", "2018 Q2", ..., "2022 Q4"], ()) default: ["2018 Q1", "2018 Q2", ..., "2022 Q4"]
        # qi_error = input["checkbox_error_timeline"].get() #Bool default: False
        # qi_trend = input["checkbox_trend_timeline"].get() #Bool: default: False
        # compare_country = input["checkbox_compare_contry_timeline"].get() #Bool default: False
        # aggregation_type = input["aggregation_type_timeline"].get() #String "median", "mean", "standard derivation", "minimum", "maximum" default: median
        data = dataframe[dataframe["QI"] == qi_value[qi_name]["referenceDataColumns"]].dropna()
        data = data.groupby("YQ")["Value"].mean()
        x = data.index
        y = data.values 
        return plot_handler.plot_timeline(x, y)
