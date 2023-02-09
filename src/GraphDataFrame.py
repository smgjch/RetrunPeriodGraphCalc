from Countries import Countries
from Events import Events
import os
import pandas as pd
import matplotlib.pyplot as plt


class GraphDataFrame():
    def __init__(self):

        self.period = -1
        self.country = None
        self.event = None
        self.dataframe = None
        os.chdir("../")

    def __set_period(self,period):
        self.period = period

    def __set_country(self,country):
        self.country = country

    def __set_event(self,event):
        self.event = event

    def read_in_data(self,period, country: Countries, event: Events):
        self.__set_period(period)
        self.__set_event(event)
        self.__set_country(country)

        data_dir = "data"

        country_path = country.value
        event_path = event.value

        data_CSV = f'{data_dir}/{country_path}/{event_path}.csv'
        self.dataframe = pd.read_csv(data_CSV)
        os.chdir("../")

    def calculate_return_period(self):
        pass


class GraphPloter():
    def __init__(self,graph):
        self.graph = graph

    def plot(self):
        x = self.graph.iloc[:, 0]
        y = self.graph.iloc[:, 1]
        plt.plot(x, y)
        plt.xlabel('Loss')
        plt.ylabel('Retrun period')
        # plt.title('Data Plot')
        plt.show()