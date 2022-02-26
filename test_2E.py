import matplotlib
import matplotlib.pyplot as plt

def test_plotting_graphs(): 
    name = "test station"
    dates=["2016","2017"]
    levels=[0.2, 0.7]
    plt.plot(dates, levels)

# Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(name)
    plt.show()
    assert plt.plot