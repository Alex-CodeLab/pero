#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

import numpy
import pero

# prepare data
x_data = numpy.linspace(-1.5*numpy.pi, 1.5*numpy.pi, 100)
y1_data = numpy.sin(x_data)
y2_data = 0.75*y1_data - 1
x_data /= numpy.pi

# init plot
plot = pero.plot.Plot()
plot.x_axis.title = "pi"
plot.y_axis.title = "f(x)"

# add series
series = pero.plot.Band(
    x = x_data,
    y1 = y1_data,
    y2 = y2_data,
    title = "Band",
    show_points = True,
    marker_line_color="white")

plot.plot(series)

# show plot
plot.zoom()
plot.view("Band Series")
