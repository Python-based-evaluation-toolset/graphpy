from lib.table import Table
from lib.bar import bar_build
from lib.plot import plot_build
import lib.utils as utils


if __name__ == "__main__":
    legend = [
        "output",
        "stack",
        "g1-output",
        "g1-stack",
        "g2-output",
        "g2-stack",
    ]
    obj = {
        "bar_0": [1, 2, 4, 2, 5, 2, 4, 4],
        "bar_1": [2, 2, 1, 5, 1, 3, 2, 1],
        "bar_2": [3, 2, 7, 1, 2, 4, 5, 3],
    }
    table = Table(legend)
    table.ns_legend_create(
        "ns-demo",
        ["ns-output", "ns-stack"],
    )
    table.title_set("interface demonstration")
    table.xtitle_set("scale-x")
    table.ytitle_set("scale-y")
    for key, value in obj.items():
        table.object_add(key, value)
    table.stack = 2
    table.group = 3

    # bar demonstrate
    utils.plt_open(table)
    bar_build(table)
    utils.plt_save_close(table, "demo-bar.pdf")

    # plot demonstrate
    utils.plt_open(table)
    plot_build(table)
    utils.plt_save_close(table, "demo-plot.pdf")

    # bar-plot combine demonstrate
    utils.plt_open(table)
    plot_build(table, "ns-demo")
    bar_build(table)
    utils.plt_save_close(table, "demo-bar-plot.pdf")
