import csv
from matplotlib import pyplot as plt
from datetime import datetime
from visualizer import Visualizer


class TemperatureVisualizer(Visualizer):
    """ Visualizes a .csv of weather data """

    def __init__(self):
        self.filename = 'death_valley_2014.csv'
        self.dates = []
        self.highs = []
        self.lows = []

    def configure(self):
        with open(self.filename) as f:
            reader = csv.reader(f)
            # read in the header row and do nothing with it
            header_row = next(reader)
            for row in reader:
                try:
                    current_date = datetime.strptime(row[0], "%Y-%m-%d")
                    high = int(row[1])
                    low = int(row[3])
                except ValueError:
                    # check for missing data and print out affected day
                    print(current_date, 'missing data')
                else:
                    self.dates.append(current_date)
                    self.highs.append(high)
                    self.lows.append(low)

    def style_render(self):
        fig = plt.figure(dpi=128, figsize=(10, 6))
        plt.plot(self.dates, self.highs, c='red')
        plt.plot(self.dates, self.lows, c='blue')
        plt.fill_between(self.dates, self.highs, self.lows, facecolor='blue', alpha=0.1)
        plt.title("Daily High & Low Temperatures - 2014\nDeath Valley, CA", fontsize=20)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()


if __name__ == "__main__":
    """ TDD: Test Code """
    tv = TemperatureVisualizer()
    tv.configure()
    tv.style_render()
