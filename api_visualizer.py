import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from visualizer import Visualizer


class APIVisualizer(Visualizer):
    """ Visualizes API data from GitHub.com.
        With minor tweaks, it could be used to
        Visualize data from other web APIs as well. """

    STR_REPR = 'api'

    def __init__(self):
        self.url = 'https://api.github.com/search/repositories?sort=stars&q=language:'
        self.language = 'python'
        self.names, self.plot_dicts = [], []

    def configure(self, language=None):
        if language is not None:
            self.language = language

        r = requests.get(self.url + self.language)
        print("Status Code: ", r.status_code)
        response_dict = r.json()
        print("Total Repositories: ", response_dict['total_count'])
        repo_dicts = response_dict['items']
        print("Number of items: ", len(repo_dicts))

        for repo_dict in repo_dicts:
            self.names.append(repo_dict['name'])
            plot_dict = {
                'value': repo_dict['stargazers_count'],
                # descriptions are not mandatory, so guard against the key returning None
                'label': repo_dict['description'] if repo_dict['description'] is not None else 'No description',
                'xlink': repo_dict['html_url'],
                }
            self.plot_dicts.append(plot_dict)

    def style_render(self):
        my_style = LS('#333366', base_style=LCS)
        my_config = pygal.Config()
        my_config.x_label_rotation = 45
        my_config.show_legend = False
        my_config.title_font_size = 24
        my_config.label_font_size = 14
        my_config.major_label_font_size = 18
        my_config.truncate_label = 15
        my_config.show_y_guides = False
        my_config.width = 1000
        chart = pygal.Bar(my_config, style=my_style)
        chart.title = 'Most-Starred Python Projects on GitHub'
        chart.x_labels = self.names
        chart.add('', self.plot_dicts)
        chart.render_to_file('{}_repos.svg'.format(self.language))
        chart.render_in_browser()


if __name__ == "__main__":
    """ TDD: Test Code """
    av = APIVisualizer()
    av.configure()
    av.style_render()
