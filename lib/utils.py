# List of reusable functions
from .table import Table
import matplotlib.pyplot as plt


def plt_open(table):
    table.fig, table.ax = plt.subplots()


def plt_save_close(table, file):
    plt.legend(
        loc="lower center",
        bbox_to_anchor=(0, -0.1, 1, 2),
        ncol=(len(table.legend) + 1) / 2,
        bbox_transform=plt.gcf().transFigure,
    )
    table.fig.savefig(
        file,
        transparent=True,
        bbox_inches="tight",
    )
    plt_close(table)


def plt_close(table):
    table.fig.clf()
    plt.close()
    table.fig = None
    table.ax = None
