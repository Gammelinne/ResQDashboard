from shiny import ui, Inputs, Outputs, Session
import utils.data_handler
from components.atoms.timeline_dashboard import timeline_dashboard_ui, timeline_dashboard_server
from components.atoms.distribution_dashboard import distribution_dashboard_ui, distribution_dashboard_server
from components.atoms.correlation_dashboard import correlation_dashboard_ui, correlation_dashboard_server
from components.atoms.comparison_dashboard import comparison_dashboard_ui, comparison_dashboard_server

custom_dashboard_ui = ui.navset_tab(
    ui.nav("Timeline", timeline_dashboard_ui),
    ui.nav("Distribution", distribution_dashboard_ui),
    ui.nav("Correlation", correlation_dashboard_ui),
    ui.nav("Sub-group comparaison", comparison_dashboard_ui),
)

def custom_dashboard_server(input: Inputs, output: Outputs, session: Session, data_handler : utils.data_handler):
    qi_value = data_handler.get_filter_data()
    plot_handler = utils.plot_handler.PlotHandler()
    dataframe = data_handler.get_data()
    timeline_dashboard_server(input, output, session, data_handler, qi_value, plot_handler, dataframe)
    distribution_dashboard_server(input, output, data_handler, session, qi_value, plot_handler, dataframe)
    correlation_dashboard_server(input, output, session,data_handler, qi_value, plot_handler, dataframe)
    comparison_dashboard_server(input, output, session,data_handler, qi_value,plot_handler, dataframe)