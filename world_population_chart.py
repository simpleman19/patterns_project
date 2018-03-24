import pygal

from chart_super_class import ChartSuperClass


class WorldPopulationChart(ChartSuperClass):
    def __init__(self):
        self.chart = pygal.maps.world.World()

    def set_style(self, style):
        self.chart.style = style
