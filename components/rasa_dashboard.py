from shiny import ui, Inputs, Outputs, Session, render
import matplotlib.pyplot as plt
import utils.data_handler


rasa_dashboard_ui = ui.page_fluid(
    ui.output_plot("rasa_plot")
)

def rasa_dashboard_server(input: Inputs, output: Outputs, session: Session, data_handler: utils.data_handler):
    @output
    @render.plot
    def rasa_plot():
        return plt.plot([1,2,3], [1,2,3])