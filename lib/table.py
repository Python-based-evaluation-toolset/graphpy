# Table is object presents to input of graph builder
from collections import OrderedDict
import matplotlib.pyplot as plt


class Table:
    """
    Table store data following legend orientation
    in order to keep graph builder code simple.
    """

    def __init__(self, legend: list):
        # extra
        self.width = 0.25
        # matplotlib figure
        self.ax = None
        self.fig = None
        # label
        self.title = None
        self.xtitle = None
        self.ytitle = None
        # group
        self.stack = 1
        self.group = 1
        # data
        self.obj = []
        self.data = []
        self.legend = legend
        self.legend_root = legend.copy()
        self.legend_ns = OrderedDict()
        for i in range(len(self.legend_root)):
            self.data.append([])

    def object_add(self, obj, values: list):
        if len(values) != len(self.legend):
            raise Exception("Object value size is miss match with legend.")
        self.obj.append(obj)
        for i in range(len(self.legend)):
            self.data[i].append(values[i])

    def ns_legend_create(self, name: str, legend: list):
        """
        namespace is used to create isolated legend out of root.
        Each namespace legends could be drawn differently.
        """
        if len(self.obj) > 0:
            raise Exception("Legend namespace is allowed only without any object.")
        self.legend_ns[name] = legend
        self.legend += legend
        for i in range(len(legend)):
            self.data.append([])

    def legend_get(self, namespace: str = None):
        if namespace is None:
            return self.legend_root
        else:
            return self.legend_ns[namespace]

    def data_get(self, legend, namespace: str = None):
        return self.data[self.legend.index(legend)]

    def obj_get(self):
        return self.obj

    def obj_arange_get(self, group=None):
        x = [i for i in range(len(self.obj))]
        if group is None:
            return x
        delta = self.width * ((self.group - 1) / 2)
        x = [i + self.width * group - delta for i in x]
        return x

    def title_set(self, title):
        self.title = title

    def xtitle_set(self, title):
        self.xtitle = title

    def ytitle_set(self, title):
        self.ytitle = title
