from lib.table import Table
from lib.bar import bar_build
from lib.plot import plot_build


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
        "bar_0": [1, 2, 4, 2, 5, 2],
        "bar_1": [2, 2, 1, 5, 1, 3],
        "bar_2": [3, 2, 7, 1, 2, 4],
    }
    table = Table(legend)
    table.title_set("interface demonstration")
    table.xtitle_set("scale-x")
    table.ytitle_set("scale-y")
    for key, value in obj.items():
        table.object_add(key, value)
    table.stack = 2
    table.group = 3
    bar_build(table, "demo-bar.pdf")
    plot_build(table, "demo-plot.pdf")
