import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Import both data tables into python using pandas. Set the index column to "MESS_DATUM" and parse the column values as dates. [1P]
garmisch  = pd.read_csv("C:/Users/Jasmin/Desktop/Sommersemester 2019/Python/exercise-4-jasminkofler/data/produkt_klima_tag_20171010_20190412_01550.txt", parse_dates=["MESS_DATUM"], index_col="MESS_DATUM", sep=";")
zugspitze = pd.read_csv("C:/Users/Jasmin/Desktop/Sommersemester 2019/Python/exercise-4-jasminkofler/data/produkt_klima_tag_20171010_20190412_05792.txt", parse_dates=["MESS_DATUM"], index_col="MESS_DATUM", sep=";")

# Clip the tables to the year 2018: [1P]
garmisch  = garmisch.loc["2018"]
zugspitze = zugspitze.loc["2018"]

# Resample the temperature data to monthly averages (" TMK") and store them in simple lists: [1P]
garmisch_agg  = garmisch.resample("1M").mean()
zugspitze_agg = zugspitze.resample("1M").mean()

garmisch_agg.head()
garmisch_agg[garmisch_agg[" TMK"]]

plt.plot(garmisch_agg.RSKF)
plt.plot(garmisch_agg. TKM) # Problem: es findet " TKM" nicht!!

# Define a plotting function that draws a simple climate diagram
# Add the arguments as mentioned in the docstring below [1P]
def create_climate_diagram(x):
    df = pd.DataFrame()
    temp_col = dtype = str
    prec_col = dtype = str
    title = dtype = str
    filename = dtype = str
    temp_min = dtype = float, int
    temp_max = dtype = float, int
    prec_min = dtype = float, int
    prec_max = dtype = float, int
    
    """
    Draw a climate diagram.
    
    Parameters
    ----------
    df : pd.DataFrame
        Dataframe with values to plot from
    temp_col : str
        Name of temperature column
    prec_col : str
        Name of precipitation column
    title : String
        The title for the figure
    filename : String
        The name of the output figure
    temp_min : Number
        The minimum temperature value to display
    temp_max : Number
        The maximum temperature value to display
    prec_min : Number
        The minimum precipitation value to display
    prec_max : Number
        The maximum precipitation value to display

    Returns
    -------
    The figure
    
    """

    fig = plt.figure(figsize=(10,8))
    plt.rcParams['font.size'] = 16

    ax2 = fig.add_subplot(111)
    ax1 = ax2.twinx()

# Set the default temperature range ("TMK") from -15°C to 20°C and the precipitation range ("RSKF") from 0mm to 370mm [1P]
    
    ax1.plot(x[-15:20, "TMK"], c="r", label="temperature range")
    ax2.plot(x[0:370, "RSKF"], c="b", label="precipitation range")
    
    return plt.plot(x)

    # Draw temperature values as a red line and precipitation values as blue bars: [1P]
    # Hint: Check out the matplotlib documentation how to plot barcharts. Try to directly set the correct
    #       x-axis labels (month shortnames).


    ax2.bar(x[0:370, "RSKF"], c="b")
    ax1.plot(x[-15:20, "TMK"], c="r")
    
    # Set appropiate limits to each y-axis using the function arguments: [1P]
    ax2.
    ax1.
    
    # Set appropiate labels to each y-axis: [1P]
    ax2.
    ax1.

    # Give your diagram the title from the passed arguments: [1P]
    plt.title("Temperature range and precipitation range")

    # Save the figure as png image in the "output" folder with the given filename. [1P]
    
    return fig
    plt.savefig("C:/Users/Jasmin/Desktop/Sommersemester 2019/Python/exercise-4-jasminkofler/klima_bsp_output.png")

# Use this function to draw a climate diagram for 2018 for both stations and save the result: [1P]
create_climate_diagram(garmisch_agg)
create_climate_diagram(zugspitze_agg)
