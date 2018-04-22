from JsonIterator import MyJson
from countries import get_country_code
from world_population_chart import WorldPopulationChart
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS
from visualizer import Visualizer


class WorldVisualizer(Visualizer):
    """ Visualizes a world population map. The Visualizer interface
        defines the configure and style_render methods that this
        visualizer should implement. """

    STR_REPR = 'world'

    def __init__(self):
        self.cc_pops_1 = {}
        self.cc_pops_2 = {}
        self.cc_pops_3 = {}
        self.split1 = 10000000
        self.split2 = 1000000000
        self.scale = 1000000

    def configure(self, split1=None, split2=None):
        if split1 is not None and split2 is not None:
            self.split2 = int(split2)
            self.split1 = int(split1)
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
            if pop < self.split1:
                self.cc_pops_1[cc] = pop
            elif pop < self.split2:
                self.cc_pops_2[cc] = pop
            else:
                self.cc_pops_3[cc] = pop
        print(len(self.cc_pops_1), len(self.cc_pops_2), len(self.cc_pops_3))

    def style_render(self):
        wm_style = RS('#336699', base_style=LCS)
        wm = WorldPopulationChart()
        wm.set_style(wm_style)
        wm.title = 'World Population in 2010, by Country'
        wm.add('0-{}m'.format(self.split1/self.scale), self.cc_pops_1)
        wm.add('{}m-{}m'.format(self.split1/self.scale, self.split2/self.scale), self.cc_pops_2)
        wm.add('>{}m'.format(self.split2/self.scale), self.cc_pops_3)
        wm.render('world_population.svg', browser=True)


if __name__ == "__main__":
    """ TDD: Test code """
    wv = WorldVisualizer()
    wv.configure()
    wv.style_render()
