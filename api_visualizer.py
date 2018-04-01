import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from visualizer import Visualizer


class APIVisualizer(Visualizer):
    """ Visualizes API data from GitHub.com.
        With minor tweaks, it could be used to
        Visualize data from other web APIs as well. """

    def __init__(self):
        self.url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        self.r = requests.get(self.url)
        print("Status Code: ", self.r.status_code)
        self.response_dict = self.r.json()
        print("Total Repositories: ", self.response_dict['total_count'])
        self.repo_dicts = self.response_dict['items']
        print("Number of items: ", len(self.repo_dicts))
        self.names, self.plot_dicts = [], []

    def configure(self):
        for repo_dict in self.repo_dicts:
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
        chart.render_to_file('python_repos.svg')


if __name__ == "__main__":
    """ Test Code """
    av = APIVisualizer()
    av.configure()
    av.style_render()
