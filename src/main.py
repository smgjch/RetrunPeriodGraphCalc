from GraphDataFrame import GraphDataFrame, GraphPloter
from Countries import Countries
from Events import Events
from Loss import Loss


def main():
    test = GraphDataFrame()
    test.read_in_data([1,10], Countries.Argentina_arg,Events.FLOOD,Loss.Houses_Destroyed)

    plt = test.calculate_return_period()
    # plt = GraphPloter(test.dataframe)
    print(type(plt))
    plt.plot()

main()