from GraphDataFrame import GraphDataFrame, GraphPloter
from Countries import Countries
from Events import Events
from Loss import Loss
import os


def main():
    print(11111,os.getcwd())
    test = GraphDataFrame()
<<<<<<< HEAD
    test.read_in_data([1,10], Countries.Mexico,Events.FLOOD,Loss.Deaths)
=======
    test.read_in_data([1,10], Countries.TestCountry,Events.FLOOD,Loss.Deaths)
>>>>>>> a7f5180 (fix)

    test.calculate_return_period()
    # plt = GraphPloter(test.dataframe)
    # print(type(plt))
    # plt.plot()

main()