from lib.table import Table
import matplotlib.pyplot as plt


def bar_build(table, output):
    fix, ax = plt.subplots()
    obj = table.obj_get()
    legend = table.legend_get()
    data = table.data_get(legend[0])
    ax.bar(obj, data)
    plt.show()
