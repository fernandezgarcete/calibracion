# coding:utf-8
from chart import DataTable, AreaChart, DialogViewer

__author__ = 'Juanjo'

import sys
from PyQt4.QtGui import QApplication, QWidget

def grafico():

    table = DataTable()
    table.addColumn('Time')
    table.addColumn('Site 1')
    table.addColumn('Site 2')
    table.addRow([ 4.00, 120,   500])
    table.addRow([ 6.00, 270,   460])
    table.addRow([ 8.30, 1260, 1120])
    table.addRow([10.15, 2030,  540])
    table.addRow([12.00,  520,  890])
    table.addRow([18.20, 1862, 1500])

    chart = AreaChart(table)
    chart.setHorizontalAxisColumn(0)
    chart.haxis_title = 'Time'
    chart.haxis_vmin = 0.0
    chart.haxis_vmax = 20.0
    chart.haxis_step = 5

    view = DialogViewer()
    view.setGraph(chart)
    view.resize(400, 240)
    view.exec_()

def main():
    app = QApplication(sys.argv)
    grafico()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
