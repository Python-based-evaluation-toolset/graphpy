from lib.table import Table
from lib.bar import bar_build


if __name__ == "__main__":
    legend = ["output"]
    obj = {"bar_0": [1], "bar_1": [2], "bar_2": [3]}
    table = Table(legend)
    for key, value in obj.items():
        table.object_add(key, value)
    bar_build(table, "demo.png")
