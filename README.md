# Chartpy

***WARN***: threading safety is not supported

A small project to create an abstract interface to work with chart.
We use matplotlib to render the chart.
There are multiple type of charts and they are flexible to use.
But our requirement is simple and we want to have a simple API to move one.

The problem is that the chart has lots of small detail need to be carried.
They are good to customize but bad to use and reuse.
It is better for us to have a simple and automate interface to draw the chart
which hide away small detail of design and present a straightforward render.
Then we create this project to build a data oriented interface for chart building
that is intentional to avoid all fancy API of matplotlib
and focus on simple and fast experience.

One small note that we do not want to use dataframe in this project
since this library is too overkill for a small task like build graph.

## Quickstart

To use library, firstly, we define list of legends.
Each legend is representation of an attributes of object.
Noting that all objects share same amount of attributes.
```python
import graphpy

legend = [
    "attr-0", "attr-1",
    "attr-2", "attr-3",
    "attr-3", "attr-4",
]
```

Then we create Table structure
which is used to construct data in form of table.
We need to predefine legends as fixed schema of structure.
```python
table = graphpy.Table(legend)
```

We could also configure meta information relating to figure.
```python
table.title_set("interface demonstration")
table.xtitle_set("scale-x")
table.ytitle_set("scale-y")
```

Finally we insert object to table.
Each object is represented of row in table form.
The interface requires two parameters:
First is object name (key)
and second is list of data (attributes) referred to object.
```python
obj = {
    "bar_0": [1, 2, 4, 2, 5, 2],
    "bar_1": [2, 2, 1, 5, 1, 3],
    "bar_2": [3, 2, 7, 1, 2, 4],
}
for key, value in obj.items():
    table.object_add(key, value)
```

In advance, we could control amount of stack and group of chart bar
in table structure.
```python
# NOTE: each column is a legend attribute.
table.stack = 2 # two stacks per column
table.group = 3 # three column per object
```

Finally, we could open, build and render data as preferred chart type.
For example of building plot chart:
```python
graphpy.utils.plt_open(table)
graphpy.plot_build(table)
graphpy.utils.plt_save_close(table, "demo-plot.pdf")
```

Or building bar chart:
```python
graphpy.utils.plt_open(table)
graphpy.bar_build(table)
graphpy.utils.plt_save_close(table, "demo-bar.pdf")
```

## Multi-namespace usage

Notice that there is demand to build different type of chart in single graph.
We extend our interface to support it.
From our perspective,
the different chart of graph
is different representation of attributes (legends) of object,
while the object interface is not change.
Therefore, in this extension,
we propose an isolation mechanism to split legends into multiple namespace.
We support to plot each legend namespace in different type of chart.

To illustrate, our way to build graph starts by defined different legends.
```python
import graphpy

legend = [
    "attr-0", "attr-1",
    "attr-2", "attr-3",
    "attr-3", "attr-4",
]

legend_namespace = [
    "attr-ns-0", "attr-ns-1"
]
```

Then we create table with a root legend and namespace legend called "demo".
```python
table = graphpy.Table(legend)
table.ns_legend_create("demo", legend_namespace)
```

After that, we insert object to table.
```python
obj = {
    # root legend values + namespace legend values
    "bar_0": [1, 2, 4, 2, 5, 2] + [2, 3],
    "bar_1": [2, 2, 1, 5, 1, 3] + [1, 5],
    "bar_2": [3, 2, 7, 1, 2, 4] + [3, 1],
}
for key, value in obj.items():
    table.object_add(key, value)
```

Configuring meta information of table.
```python
table.title_set("interface demonstration")
table.xtitle_set("scale-x")
table.ytitle_set("scale-y")
table.stack = 2
table.group = 3
```

Finally, we draw graph with different chart for each namespace.
```python
graphpy.utils.plt_open(table)
graphpy.bar_build(table)
graphpy.plot_build(table, "demo") # specify namespace to build chart
graphpy.utils.plt_save_close(table, "demo-bar-plot.pdf")
```
