import numpy as np

from Countries import Countries
from Events import Events
import os
import pandas as pd
import matplotlib.pyplot as plt

from LossFreqCurve import LossFreqCurve
from Loss import Loss


class GraphDataFrame():
    def __init__(self):
        self.period = -1
        self.country = None
        self.event = None
        self.loss = None
        self.dataframe: pd.DataFrame = None
        os.chdir("../")

    def _set_period(self, period):
        self.period = period

    def _set_loss(self, loss):
        self.loss = loss

    def _set_country(self, country):
        self.country = country

    def _set_event(self, event):
        self.event = event

    def read_in_data(self, period, country: Countries, event: Events, loss: Loss):
        self._set_period(period)
        self._set_event(event)
        self._set_country(country)
        self._set_loss(loss)

        data_dir = "data"

        country_path = country.value
        event_path = event.value

        data_CSV = f'{data_dir}/{country_path}/{event_path}.csv'
        self.dataframe = pd.read_csv(data_CSV)

        os.chdir("../")

    def get_axis(self):
        columns: pd.Index = self.dataframe.columns

        return columns.get_loc(self.loss.value)

    def get_record_length(self):
        # print(self.dataframe.iloc[-1, 0])
        return int(self.dataframe.iloc[-1, 1]) - int(self.dataframe.iloc[0, 1])

    def create_frequency(self):
        total_record = self.get_record_length()
        count = self.dataframe[self.loss.value].value_counts()/total_record
        self.dataframe["frequency"] = self.dataframe[self.loss.value].map(count)

    def get_records_number(self):
        return int(self.dataframe.iloc[-1, 0]) - int(self.dataframe.iloc[0, 0]) +1

    def create_probability(self):
        total_events = self.get_records_number()
        probability = self.dataframe[self.loss.value].value_counts()/total_events
        self.dataframe["probability"] = self.dataframe[self.loss.value].map(probability)





    def calculate_return_period(self):
        ifc = LossFreqCurve()
        sort_index = np.argsort(self.dataframe[self.loss.value])[::-1]
        record_length = self.get_record_length()
        # self.dataframe["exceedance"] = (record_length-sort_index +1)/(record_length+1)
        # print (self.dataframe[" Deaths"])
        self.create_probability()
        self.create_frequency()
        exceedance_probability = self.dataframe["frequency"][sort_index] * self.dataframe["probability"][sort_index]
        # print(exceedance_probability)
        # print (exceedance_probability)
        #
        # ifc.return_period = 1 / exceedance_probability[::-1]
        # ifc.impact = self.dataframe[sort_index][::-1]
        # ifc.label = "Exceedance frequency curve"

        return 0


class GraphPloter():
    def __init__(self, graph):
        self.graph = graph

    def plot(self):
        x = self.graph.iloc[:, 0]
        y = self.graph.iloc[:, 1]
        plt.plot(x, y)
        plt.xlabel('Loss')
        plt.ylabel('Return period')
        # plt.title('Data Plot')
        plt.show()
