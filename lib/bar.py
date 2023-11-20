from lib.table import Table
import matplotlib.pyplot as plt


def bar_build(table, output):
    fix, ax = plt.subplots()
    legend_idx = 0
    # build bar
    for group in range(table.group):
        ax.bar(
            table.obj_arange_get(group),
            table.data_get_by_idx(legend_idx),
            width=table.width,
        )
        legend_idx += 1
        for i in range(table.stack - 1):
            ax.bar(
                table.obj_arange_get(group),
                table.data_get_by_idx(legend_idx),
                width=table.width,
                bottom=table.data_get_by_idx(legend_idx - 1),
            )
            legend_idx += 1
    # label
    ax.set_title(table.title)
    ax.set_xticks(table.obj_arange_get(), table.obj_get())
    ax.set_ylabel(table.ytitle)
    ax.set_xlabel(table.xtitle)
    ax.legend(table.legend_get()[0:legend_idx])
    plt.show()
