from .table import Table
from .utils import plt_save_close
import matplotlib.pyplot as plt


def plot_build(table, namespace: str = None):
    fix = table.fig
    ax = table.ax
    legends = table.legend_get(namespace)
    # build bar
    for legend in legends:
        lns = ax.plot(
            table.obj_arange_get(),
            table.data_get(legend),
            marker="o",
            label=legend,
        )
    # label
    ax.set_title(table.title)
    ax.set_xticks(table.obj_arange_get(), table.obj_get())
    ax.set_ylabel(table.ytitle)
    ax.set_xlabel(table.xtitle)
