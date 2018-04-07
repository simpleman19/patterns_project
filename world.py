from JsonIterator import MyJson
from countries import get_country_code
from world_population_chart import WorldPopulationChart
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS
from visualizer import Visualizer


class WorldVisualizer(Visualizer):
    """ Visualizes a world population map. The Visualizer interface
        defines the configure and style_render methods that this
        visualizer should implement. """

    def __init__(self):
        self.cc_pops_1 = {}
        self.cc_pops_2 = {}
        self.cc_pops_3 = {}

    def configure(self):
        filename = 'population_data.json'
        with open(filename) as f:
            # this is a custom iterator--the Iterator pattern
            pop_data = MyJson(f.read())
        cc_populations = {}
        pop_data_iterator = pop_data.get_iterator()
        while pop_data_iterator.has_next():
            pop_dict = pop_data_iterator.next()
            if pop_dict['Year'] == '2010':
                country_name = pop_dict['Country Name']
                # need an int value, but have to convert to
                # float first then truncate
                population = int(float(pop_dict['Value']))
                code = get_country_code(country_name)
                if code:
                    cc_populations[code] = population

        for cc, pop in cc_populations.items():
            if pop < 10000000:
                self.cc_pops_1[cc] = pop
            elif pop < 1000000000:
                self.cc_pops_2[cc] = pop
            else:
                self.cc_pops_3[cc] = pop
        print(len(self.cc_pops_1), len(self.cc_pops_2), len(self.cc_pops_3))

    def style_render(self):
        wm_style = RS('#336699', base_style=LCS)
        wm = WorldPopulationChart()
        wm.set_style(wm_style)
        wm.title = 'World Population in 2010, by Country'
        wm.add('0-10m', self.cc_pops_1)
        wm.add('10m-1bn', self.cc_pops_2)
        wm.add('>1bn', self.cc_pops_3)
        wm.render('world_population.svg')


if __name__ == "__main__":
    """ TDD: Test code """
    wv = WorldVisualizer()
    wv.configure()
    wv.style_render()
