from shiny import ui, render, Inputs, Outputs, Session
import matplotlib.pyplot as plt
import utils.data_handler

dashboard_ui = ui.page_fluid(
    ui.h1('test'),
    ui.output_plot("a_scatter_plot"),
)

def dashboard_server(input: Inputs, output: Outputs, session: Session, data_handler : utils.data_handler):
    @output
    @render.plot
    def a_scatter_plot():
        return plt.scatter([1,2,3], [5, 2, 3])
    
