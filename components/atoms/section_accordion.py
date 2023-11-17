from shiny import ui, Inputs, Outputs, Session, render, module
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
csv = pd.read_csv("assets/filter.csv")
@module.ui
def section_ui():
    return ui.output_plot("plott")

@module.server
def section_server(input: Inputs, output: Outputs, session: Session):
    filtered_data = csv[csv['QICategory'] == output._ns]
    def height():
        return len(filtered_data['aggregatedGroupsName'].unique()) * 200
    @output
    @render.plot(height=height())
    def plott(): 
        if len(filtered_data['aggregatedGroupsName'].unique()) > 1: 
            fig, axs = plt.subplots(math.ceil(len(filtered_data['aggregatedGroupsName'].unique())/2), 2)
            left = 0
            right = 0
            for i, aggregated_name in enumerate(filtered_data['aggregatedGroupsName'].unique()):
                if i % 2 == 0 :
                    axs[left, 0].plot([1,2,3],[1,2,3])
                    left += 1
                elif i % 2 != 0 :
                    axs[right, 1].plot([3,2,1],[3,2,1])
                    right += 1
            return fig
        else : 
            return plt.plot([1,2,3],[1,2,3])