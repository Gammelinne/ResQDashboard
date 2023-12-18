from shiny import App, ui, Inputs, Outputs, Session
from components.dashboard import dashboard_ui, dashboard_server
from components.custom_dashboard import custom_dashboard_ui, custom_dashboard_server
from components.rasa_dashboard import rasa_dashboard_ui, rasa_dashboard_server
import utils.data_handler

app_ui = ui.page_bootstrap(
    ui.navset_bar(
        ui.nav("Dashboard", dashboard_ui), 
        ui.nav("Custom", custom_dashboard_ui),
        ui.nav('Rasa', rasa_dashboard_ui),
        title="Res-Q Dashboard",
    ),
    ui.div(ui.HTML("<div id='rasa-chat-widget' data-websocket-url='http://localhost:5005/socket.io'></div><script src='https://unpkg.com/@rasahq/rasa-chat' type='application/javascript'></script>")),
    window_title="Res-Q Dashboard",
)
# Server Part
def server(input: Inputs, output: Outputs, session: Session):
    # Import CSV
    data_handler = utils.data_handler.DataHandler()

    # !! there is also a variable quarter_choice in value_filter.py !!
    quarter_choice = ["2018 Q1","2018 Q2","2018 Q3","2018 Q4","2019 Q1","2019 Q2","2019 Q3","2019 Q4","2020 Q1","2020 Q2","2020 Q3","2020 Q4","2021 Q1","2021 Q2","2021 Q3","2021 Q4","2022 Q1","2022 Q2","2022 Q3","2022 Q4"]
    
    # Call dashboard_server function
    dashboard_server(input, output, session, data_handler, quarter_choice)
    custom_dashboard_server(input, output, session, data_handler)
    rasa_dashboard_server(input, output, session, data_handler)

# Creating Shiny application
app = App(app_ui, server)
