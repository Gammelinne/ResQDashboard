from shiny import App, ui
from components.dashboard import dashboard_ui
from components.custom_dashboard import custom_dashboard_ui
import utils.data_handler

app_ui = ui.page_navbar(
    ui.nav_spacer(),
    ui.nav("Dashboard", dashboard_ui), 
    ui.nav("Custom", custom_dashboard_ui),
    title="Res-Q Dashboard",
    window_title="Res-Q Dashboard",
)

# Server Part
def server(input, output, session):
    # Server logic (if necessary)
    pass

# Creating Shiny application
app = App(app_ui, server)