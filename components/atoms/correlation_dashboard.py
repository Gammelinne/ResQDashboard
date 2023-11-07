from shiny import ui, Inputs, Outputs, Session
import utils.data_handler
from components.atoms.macros.plot_characteristics import plot_characteristics_ui, plot_characteristics_server

correlation_dashboard_ui = ui.layout_sidebar(
    ui.sidebar(
        ui.row(
            ui.column(
                8,
                plot_characteristics_ui("correlation")
            ),
        ),
        width=300,
        title="Correlation",
    )
)

def correlation_dashboard_server(input: Inputs, output: Outputs, session: Session, data_handler : utils.data_handler):
    plot_characteristics_server(input, output, session, data_handler, "Correlation")