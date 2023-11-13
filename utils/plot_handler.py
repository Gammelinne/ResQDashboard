import matplotlib.pyplot as plt
import datetime
import seaborn
import pandas as pd
import numpy as np
# from . import globals


class PlotHandler:
    def __init__(self):
        self._date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    def plot_timeline(self, x, y, x_label: str = None, y_label: str = None):
            fig, ax = plt.subplots()
            if x_label is not None:
                ax.set_xlabel(x_label)
            if y_label is not None:
                ax.set_ylabel(y_label)
            ax.plot(x, y, marker="o")
            ax.tick_params(axis="x", rotation=90)
            for i in range(len(x)):
                ax.text(x[i], y[i] * 1.05, str(round(y[i])), color='black', fontsize=12, ha='center', va='bottom')
            fig.subplots_adjust(bottom=0.20)
            ax.tick_params(axis='both', which='both', color='b', grid_alpha=0.5, grid_linewidth=0.5)
            return fig
        
    
    # def plot_distribution(self, x, x_label: str = None, y_label: str = None):
    #     if x_label is not None:
    #         plt.xlabel(x_label)
    #     if y_label is not None:
    #         plt.ylabel(y_label)
    #     plot = seaborn.kdeplot(x)
    #     fig = plot.get_figure()
    #     plt.xlim(0, max(x))
    #     plt.tick_params(axis='both', which='both', color='b', grid_alpha=0.5, grid_linewidth=0.5)
    #     plt.grid(True)
    #     fig.savefig(f"{globals.PATH_SAVE_PLOT}/distribution_{self._date}.png")

    # def plot_correlation(self, x, y, x_label: str = None, y_label: str = None):
    #     if x_label is not None:
    #         plt.xlabel(x_label)
    #     if y_label is not None:
    #         plt.ylabel(y_label)
    #     plot = plt.scatter(x, y)
    #     plt.tick_params(axis='both', which='both', color='b', grid_alpha=0.5, grid_linewidth=0.5)
    #     plt.grid(True)
    #     return plot
    
    # def plot_comparison(self, values_list: list, labels_list: list, x_label: str = None, y_label: str = None):
    #     if x_label is not None:
    #         plt.xlabel(x_label)
    #     if y_label is not None:
    #         plt.ylabel(y_label)
    #     plt.boxplot(values_list, showfliers=False)
    #     plt.tick_params(axis='both', which='both', color='b', grid_alpha=0.5, grid_linewidth=0.5)
    #     plt.grid(True)
    #     plt.xticks(range(1, len(labels_list) + 1), labels_list)
    #     return plt