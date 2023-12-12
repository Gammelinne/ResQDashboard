import matplotlib.pyplot as plt
import datetime
import seaborn
import pandas as pd
import numpy as np
# from . import globals

class PlotHandler:
    def __init__(self, save_plot=False):
        self._date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self._plot_name = None
        self._save = save_plot

    def plot_timeline(self, x, y, x_label: str = None, y_label: str = None):
        self._plot_name = "timeline"
        plot, ax = plt.subplots()
        if x_label is not None:
            ax.set_xlabel(x_label)
        if y_label is not None:
            ax.set_ylabel(y_label)
        ax.plot(x, y, marker="o")
        ax.tick_params(axis="x", rotation=90)
        for i in range(len(x)):
            ax.text(x[i], y[i] * 1.05, str(round(y[i])), color='black', fontsize=12, ha='center', va='bottom')
        plot.subplots_adjust(bottom=0.20)
        ax.tick_params(axis='both', which='both', color='b', grid_alpha=0.5, grid_linewidth=0.5)
        if self._save:
            self._save_plot_to_img(plot)
        return plot

    def plot_distribution(self, x, x_label: str = None, y_label: str = None):
        self._plot_name = "distribution"
        if x_label is not None:
            plt.xlabel(x_label)
        if y_label is not None:
            plt.ylabel(y_label)
        plot = seaborn.kdeplot(x).get_figure()
        plt.xlim(0, max(x))
        plt.tick_params(axis='both', which='both', color='b', grid_alpha=0.5, grid_linewidth=0.5)
        plt.grid(True)
        if self._save:
            self._save_plot_to_img(plot)
        return plot

    def plot_correlation(self, x, y, x_label: str = None, y_label: str = None):
        self._plot_name = "correlation"
        plot, ax = plt.subplots()
        if x_label is not None:
            ax.set_xlabel(x_label)
        if y_label is not None:
            ax.set_ylabel(y_label)
        ax.scatter(x, y)
        ax.tick_params(axis='both', which='both', color='b', grid_alpha=0.5, grid_linewidth=0.5)
        ax.grid(True)
        if self._save:
            self._save_plot_to_img(plot)
        return plot

    def plot_comparison(self, values_list: list, labels_list: list, x_label: str = None, y_label: str = None):
        self._plot_name = "comparison"
        plot, ax = plt.subplots()
        if x_label is not None:
            ax.set_xlabel(x_label)
        if y_label is not None:
            ax.set_ylabel(y_label)
        ax.boxplot(values_list, showfliers=False)
        ax.tick_params(axis='both', which='both', color='b', grid_alpha=0.5, grid_linewidth=0.5)
        ax.grid(True)
        ax.set_xticklabels(labels_list)
        if self._save:
            self._save_plot_to_img(plot)
        return plot