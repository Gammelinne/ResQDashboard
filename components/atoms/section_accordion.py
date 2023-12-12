from shiny import ui, Inputs, Outputs, Session, render, module
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
csv = pd.read_csv("assets/filter.csv")
@module.ui
def section_ui(categorie):
    QICategory = csv[csv['QICategory'] == categorie]
    if len(QICategory['aggregatedGroupsName'].unique()) > 1: 
        return ui.output_plot("output_plot", height=(len(QICategory['aggregatedGroupsName'].unique()))*300)
    else:
        return ui.output_plot("output_plot")

@module.server
def section_server(input: Inputs, output: Outputs, session: Session):
    QICategory = csv[csv['QICategory'] == output._ns]

    @output
    @render.plot
    def output_plot(): 
        if len(QICategory['aggregatedGroupsName'].unique()) > 1: 
            fig, axs = plt.subplots(math.ceil(len(QICategory['aggregatedGroupsName'].unique())/2), 2)
            
            left = 0
            right = 0
            for i, aggregated_name in enumerate(QICategory['aggregatedGroupsName'].unique()):
                # Check if there are subcategory
                has_subcategory = not QICategory[(QICategory['aggregatedGroupsName'] == aggregated_name) & (QICategory['QiSubCategory'].notnull())].empty
                
                if i % 2 == 0 :
                    axs[left, 0].set_title(aggregated_name)
                    if has_subcategory:
                        axs[left, 0].plot([1,2,3],[1,2,3]) #Or : return one_plot_function(name=aggregated_name, has_subcategory=True) ect..
                    else:
                        axs[left, 0].plot([3,4,5],[4,5,6])  #Or : return one_plot_function(name=aggregated_name, has_subcategory=False) ect..
                    left += 1
                elif i % 2 != 0 :
                    axs[right, 1].set_title(aggregated_name) 
                    if has_subcategory:
                        axs[right, 1].plot([1,2,3],[1,2,3])
                    else:
                        axs[right, 1].plot([3,4,5],[4,5,6])
                    right += 1
       
            if len(QICategory['aggregatedGroupsName'].unique()) % 2 == 1: 
                fig.delaxes(axs[-1, -1])
            return fig
        else : 
            return plt.plot([1,2,3],[1,2,3])
