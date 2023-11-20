# Table is object presents to input of graph builder


class Table:
    """
    Table store data following legend orientation
    in order to keep graph builder code simple.
    """

    def __init__(self, legend: list):
        # extra
        self.width = 0.25
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
        for i in range(len(self.legend)):
            self.data.append([])

    def object_add(self, obj, values: list):
        if len(values) != len(self.legend):
            raise Exception("Object value size is miss match with legend.")
        self.obj.append(obj)
        for i in range(len(self.legend)):
            self.data[i].append(values[i])

    def legend_get(self):
        return self.legend

    def data_get(self, legend):
        return self.data[self.legend.index(legend)]

    def data_get_by_idx(self, idx):
        return self.data[idx]

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
