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

    def get_frequency(self):
        total_record = self.get_records_number()
        self.dataframe["frequency"] = pd.value_counts(self.dataframe[self.loss.value])/total_record

    def get_records_number(self):
        return int(self.dataframe.iloc[-1, 0]) - int(self.dataframe.iloc[0, 0])


    def test(self):
        test = GraphDataFrame()
        test.read_in_data([1, 10], Countries.TestCountry, Events.FLOOD, Loss.Death)

        print(test.dataframe[Loss.Death.value])

        test.calculate_return_period()

    def calculate_return_period(self):
        ifc = LossFreqCurve()
        sort_index = np.argsort(self.dataframe[self.loss.value])[::-1]
        # print (sort_index)
        # print (sort_index[::-1])
        record_length = self.get_record_length()
        self.dataframe["exceedance"] = (record_length-sort_index +1)/(record_length+1)
        # print (self.dataframe["exceedance"])
        self.get_frequency()
        print(self.dataframe["frequency"])

        exceedance_probability = np.cumsum(self.dataframe["frequency"][sort_index]/record_length)
        # print(exceedance_probability)
        # print (exceedance_probability)
        #
        # ifc.return_period = 1 / exceedance_probability[::-1]
        # ifc.impact = self.dataframe[sort_index][::-1]
        # ifc.label = "Exceedance frequency curve"

        return 0



test = GraphDataFrame()
test.test()