from GraphDataFrame import GraphDataFrame, GraphPloter
from Countries import Countries
from Events import Events
from Loss import Loss


def main():
    test = GraphDataFrame()
    test.read_in_data([1,10], Countries.TestCountry,Events.FLOOD,Loss.Death)

    test.calculate_return_period()
    plt = GraphPloter(test.dataframe)

    plt.plot()

main()