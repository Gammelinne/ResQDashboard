from shiny import App, ui, Inputs, Outputs, Session
from components.dashboard import dashboard_ui, dashboard_server
from components.custom_dashboard import custom_dashboard_ui, custom_dashboard_server
import utils.data_handler

app_ui = ui.page_bootstrap(
    ui.navset_bar(
        ui.nav("Dashboard", dashboard_ui), 
        ui.nav("Custom", custom_dashboard_ui),
        title="Res-Q Dashboard",
    ),
    ui.div(ui.HTML("<script src='https://unpkg.com/@rasahq/rasa-chat' type='application/javascript'></script><div id='rasa-chat-widget' data-websocket-url='https://your-rasa-url-here/'></div>")),
    window_title="Res-Q Dashboard",
)

# Server Part
def server(input: Inputs, output: Outputs, session: Session):
    # Import CSV
    data_handler = utils.data_handler.DataHandler()
    
    # Call dashboard_server function
    dashboard_server(input, output, session, data_handler)
    custom_dashboard_server(input, output, session, data_handler)

# Creating Shiny application
app = App(app_ui, server)
