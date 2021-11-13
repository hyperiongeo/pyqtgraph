#!/usr/bin/python
# -*- coding: utf-8 -*-
# Add path to library (just for examples; you do not need this)
import initExample
import numpy as np

import pyqtgraph as pg
from pyqtgraph.Qt import QtGui

app = pg.mkQApp()
mw = QtGui.QMainWindow()
mw.resize(800, 800)
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")

mpw = pg.MultiAxisPlotWidget()

mw.setCentralWidget(mpw)
mw.show()

# LEGEND
mpw.addLegend(offset=(450, 50))
# TITLE
mpw.setTitle("MultiAxisPlotWidget Example")
# AXYS
ax1 = mpw.addAxis("bottom", name="sx1", text="Samples1", units="sx1")
ax2 = mpw.addAxis("bottom", name="sx2", text="Samples2", units="sx2")
ax3 = mpw.addAxis("bottom", name="sx3", text="Samples3", units="sx3")
ay1 = mpw.addAxis("left", name="sy1", text="Data1", units="sy1")
ay2 = mpw.addAxis("left", name="sy2", text="Data2", units="sy2")
ay3 = mpw.addAxis("left", name="sy3", text="Data3", units="sy3")
# CHARTS
c1, pi1 = mpw.addChart("Dataset 1", x_axis="sx1", y_axis="sy1")
c2, pi2 = mpw.addChart("Dataset 2", x_axis="sx2", y_axis="sy1")
c3, pi3 = mpw.addChart("Dataset 3", x_axis="sx2", y_axis="sy2")
c4, pi4 = mpw.addChart("Dataset 4", x_axis="sx3", y_axis="sy3")
# make and display chart
mpw.makeLayout()

data1 = np.array(np.sin(np.linspace(0, 2 * np.pi, num=1000)))
c1.setData(data1, pen=pg.mkPen('r', width=2))
data2 = data1 * 2
c2.setData(data2, pen=pg.mkPen('g', width=2))
data3 = np.array(np.sin(np.linspace(0, 4 * np.pi, num=500))) * 3
c3.setData(data3, pen=pg.mkPen('k', width=2))
data4 = np.array(np.sin(np.linspace(0, 4 * np.pi, num=500))) * 5
c4.setData(data4, pen=pg.mkPen('b', width=2))

# mpw.update()


# Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    pg.mkQApp().exec_()
