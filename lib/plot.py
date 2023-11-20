from .table import Table
from .utils import plt_save_close
import matplotlib.pyplot as plt


def plot_build(table, output):
    fix, ax = plt.subplots()
    # build bar
    for idx, legend in enumerate(table.legend):
        ax.plot(
            table.obj_arange_get(),
            table.data_get_by_idx(idx),
            marker="o",
        )
    # label
    ax.set_title(table.title)
    ax.set_xticks(table.obj_arange_get(), table.obj_get())
    ax.set_ylabel(table.ytitle)
    ax.set_xlabel(table.xtitle)
    ax.legend(table.legend_get())
    plt_save_close(ax, output)
