# Chartpy

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
