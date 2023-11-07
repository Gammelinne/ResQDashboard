from shiny import ui, render, Inputs, Outputs, Session, reactive, req
import utils.data_handler
from components.atoms.timeline_dashboard import timeline_dashboard_ui, timeline_dashboard_server
from components.atoms.distribution_dashboard import distribution_dashboard_ui, distribution_dashboard_server
from components.atoms.correlation_dashboard import correlation_dashboard_ui, correlation_dashboard_server

custom_dashboard_ui = ui.navset_tab(
    ui.nav("Timeline", timeline_dashboard_ui),
    ui.nav("Distribution", distribution_dashboard_ui),
    ui.nav("Correlation", correlation_dashboard_ui),
    ui.nav("Sub-group comparaison"),
)

def custom_dashboard_server(input: Inputs, output: Outputs, session: Session, data_handler : utils.data_handler):
    timeline_dashboard_server(input, output, session, data_handler)
    distribution_dashboard_server(input, output, session, data_handler)
    correlation_dashboard_server(input, output, session, data_handler)