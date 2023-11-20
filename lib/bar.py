from .table import Table
from .utils import plt_save_close
import matplotlib.pyplot as plt


def bar_build(table, output, namespace: str = None):
    fix, ax = plt.subplots()
    legends = table.legend_get(namespace)
    pre_legend = None
    bottom = [0 for i in range(len(table.obj_get()))]
    group = 0
    stack = 1
    # build bar
    for legend in legends:
        ax.bar(
            table.obj_arange_get(group),
            table.data_get(legend),
            width=table.width,
            bottom=bottom,
        )
        if stack < table.stack:
            stack += 1
            data = table.data_get(legend)
            for i in range(len(bottom)):
                bottom[i] += data[i]
        elif group < table.group:
            stack = 1
            group += 1
            bottom = [0 for i in bottom]

    # label
    ax.set_title(table.title)
    ax.set_xticks(table.obj_arange_get(), table.obj_get())
    ax.set_ylabel(table.ytitle)
    ax.set_xlabel(table.xtitle)
    ax.legend(legends)
    plt_save_close(ax, output)
