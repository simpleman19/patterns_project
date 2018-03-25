import pygal

from RefactoredCharts.chart_super_class import ChartSuperClass


class DiceHistogram(ChartSuperClass):

    def __init__(self):
        self.chart = pygal.Bar()

    def set_style(self, style):
        self.chart.style = style
