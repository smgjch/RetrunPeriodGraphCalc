import numpy as np

from Countries import Countries
from Events import Events
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# from LossFreqCurve import LossFreqCurve
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

        print(22222222,os.getcwd())
        data_dir = "RetrunPeriodGraphCalc/data"

        country_path = country.value
        event_path = event.value

        data_CSV = f'{data_dir}/{country_path}/{event_path}s.csv'
        self.dataframe = pd.read_csv(data_CSV)

        os.chdir("../")

    def get_axis(self):
        columns: pd.Index = self.dataframe.columns

        return columns.get_loc(self.loss.value)

    def get_record_length(self):
        # print(self.dataframe.iloc[-1, 0])
        record_end = self.dataframe.iloc[-1, -1]
        record_start = self.dataframe.iloc[0, -3]
        start_date = datetime.strptime(record_start, '%Y-%m-%d')
        end_date = datetime.strptime(record_end, '%Y-%m-%d')
        delta: datetime.timedelta = end_date-start_date

        return delta.days/365

    def get_exceedance_period(self):
        total_record = self.get_record_length()
        # count = self.dataframe[self.loss.value].value_counts()
        # print("sort",sort_index)
        a= self.dataframe[self.loss.value].value_counts(ascending = True)
        print(1111111,a)
        b = self.dataframe[self.loss.value].value_counts(ascending = True).sort_index()[::-1]
        print("Sorted",b)
        mapView = self.dataframe[self.loss.value].map(b)
        print("mapView",mapView)
        loss_frequency = np.cumsum(self.dataframe[self.loss.value].value_counts(ascending = True).sort_index()[::-1])/total_record
        print ("exce",type(loss_frequency))
        counters = self.dataframe[self.loss.value].map(loss_frequency)
        print("Counters",counters)
        tmp = self.dataframe[self.loss.value].map(loss_frequency/total_record)
        print("tmp",tmp)
        
        return loss_frequency
        # print ("freq",self.dataframe["frequency"])

    def get_return_period(self):
        return 1/self.get_exceedance_period()


    def get_records_number(self):
        return int(self.dataframe.iloc[-1, 0]) - int(self.dataframe.iloc[0, 0]) +1

    def create_probability(self):
        total_events = self.get_records_number()
        probability = self.dataframe[self.loss.value].value_counts()/total_events
        self.dataframe["probability"] = self.dataframe[self.loss.value].map(probability)





    def calculate_return_period(self):
        ImpactReturnPeriodGraph = GraphPloter(self.dataframe)

        graph = self.get_return_period()
        graph.plot()
        plt.show()

        # exceedance_period = self.get_exceedance_period()
        
        # sort_index = np.argsort(exceedance_period)[::-1]
        # y = 1/exceedance_period[sort_index]
        # x = self.dataframe[self.loss.value][sort_index]

        # record_length = self.get_record_length()
        # self.dataframe["exceedance"] = (record_length-sort_index +1)/(record_length+1)
        # print (self.dataframe[" Deaths"])
        # self.create_probability()
        # x = 1/self.get_exceedance_period()[::-1]
        # y = self.dataframe[self.loss.value][::-1]
        # ImpactReturnPeriodGraph.set_graph(x,y)

        # exceedance_probability = self.dataframe["frequency"][sort_index] * self.dataframe["probability"][sort_index]
        # print( self.dataframe["frequency"])
        # print (exceedance_probability)
        #
        # ifc.return_period = 1 / exceedance_probability[::-1]
        # ifc.impact = self.dataframe[sort_index][::-1]
        # ifc.label = "Exceedance frequency curve"

        # return ImpactReturnPeriodGraph


class GraphPloter():
    def __init__(self, graph):
        # self.graph = graph
        self.x = None
        self.y = None

    def __set_x(self,x):
        self.x = x

    def __set_y(self,y):
        self.y = y

    def set_graph(self,x,y):
        self.__set_x(x)
        self.__set_y(y)


    def plot(self):
        # x = self.graph[]
        # y = self.graph.iloc[:, 1]
        plt.plot(self.x,self.y)
        plt.xlabel('Loss')
        plt.ylabel('Return period')
        # plt.title('Data Plot')
        plt.show()
