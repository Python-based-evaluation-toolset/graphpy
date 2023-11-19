# Table is object presents to input of graph builder


# TODO: DO NOT SUPPORT STACK BAR CHART NOW
class Table:
    """
    Table store data following legend orientation
    in order to keep graph builder code simple.
    """

    def __init__(self, legend: list):
        self.obj = []
        self.data = []
        self.legend = legend
        for i in range(len(self.legend)):
            self.data.append([])

    def object_add(obj, values: list):
        if len(values) != len(self.legend):
            raise Exception("Object value size is miss match with legend.")
        self.obj.append(obj)
        for i in range(len(self.legend)):
            self.data[i].append(values[i])
