from GraphDataFrame import GraphDataFrame, GraphPloter
from Countries import Countries
from Events import Events
def main():
    test = GraphDataFrame()
    test.read_in_data(-1, Countries.TestCountry,Events.FLOOD)
    plt = GraphPloter(test.dataframe)
    plt.plot()

main()