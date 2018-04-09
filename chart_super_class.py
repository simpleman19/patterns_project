class ChartSuperClass(object):
    chart = None
    title = ""
    x_labels = []
    x_title = []
    y_labels = []
    y_title = []

    def __init__(self):
        raise NotImplementedError()

    def add(self, title, values):
        self.chart.add(title, values)

    def render(self, filename, browser=False):
        self.chart.title = self.title
        if len(self.x_labels) != 0:
            self.chart.x_labels = self.x_labels
        self.chart.x_title = self.x_title
        if len(self.y_labels) != 0:
            self.chart.y_labels = self.y_labels
        self.chart.y_title = self.y_title
        self.chart.render_to_file(filename)
        if browser:
            self.chart.render_in_browser()

    def set_style(self, style):
        raise NotImplementedError()
