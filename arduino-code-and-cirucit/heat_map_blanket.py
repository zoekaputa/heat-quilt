"""
Zoe Kaputa
DXARTS 472 at the Univerisity of Washington 2021

Program running data analysis on Seattle crime data (collected June 5 2021) to
produce a heat map and tranfer that data into an ardinuo operated heat map
blanket representing this data.
"""
import pyfirmata
import time
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def setup(port_name):
    """
    Return the ardunio board plugged into the port specified by the port_name
    parameter. Performs analysis to produce a 3x3 heat map using the data from
    SPD_Crime_Data__2008-Present.csv, where the horizontal axis represents
    Neigborhoods in Seattle and the vertical axis represents Sexual Offense.
    The numeric values of each bucket in the heat map is then compared to the
    average number of values in a bucket. This information is returned as the
    2D array heat_map. Also produces and returns heat_pin_matrix, which is a 2D
    array of pins based on their corresponding positions on the blanket.
    """

    # data analysis variables
    file_name = \
        "/Users/zoekaputa/Desktop/DXARTS 472/SPD_Crime_Data__2008-Present.csv"
    plot_title = "Sexual Assult Related Offense by Seattle Neigborhood"
    plot_name = "heatmap_blanket.png"
    vertical_bins_column = "Offense"
    horizontal_bins_column = "MCPP"
    vertical_bins = ["Fondling", "Sexual Assault With An Object",
                     "Peeping Tom"]
    horizontal_bins = ["ROOSEVELT/RAVENNA", "WALLINGFORD", "UNIVERSITY"]

    # perform analysis and produce heat map png
    dataframe = pd.read_csv(file_name)
    plot_and_save_heat_map(dataframe, vertical_bins_column,
                           horizontal_bins_column, vertical_bins,
                           horizontal_bins, plot_title, plot_name)
    heat_map = create_heat_map(dataframe, vertical_bins_column,
                               horizontal_bins_column, vertical_bins,
                               horizontal_bins)

    # set up arduino and heat pin matrix
    board = pyfirmata.Arduino(port_name)
    heat_pin_matrix = set_up_arduino(board)

    return board, heat_pin_matrix, heat_map


def set_up_arduino(board):
    """
    Returns a 3x3 2D array of pins based on their corresponding positions on
    the blanket. In general, the pins range from 2-10 and increase downward
    and to the right.
    """
    it = pyfirmata.util.Iterator(board)
    it.start()

    # initalize all arduino pins
    top_left_heat_pin = board.digital[2]
    top_middle_heat_pin = board.digital[3]
    top_right_heat_pin = board.digital[4]
    middle_left_heat_pin = board.digital[5]
    middle_middle_heat_pin = board.digital[6]
    middle_right_heat_pin = board.digital[7]
    bottom_left_heat_pin = board.digital[8]
    bottom_middle_heat_pin = board.digital[9]
    bottom_right_heat_pin = board.digital[10]

    # produce matrix
    heat_pin_matrix = [[top_left_heat_pin, top_middle_heat_pin,
                        top_right_heat_pin],
                       [middle_left_heat_pin, middle_middle_heat_pin,
                        middle_right_heat_pin],
                       [bottom_left_heat_pin, bottom_middle_heat_pin,
                        bottom_right_heat_pin]]

    return heat_pin_matrix


def plot_and_save_heat_map(dataframe, vertical_bins_column,
                           horizontal_bins_column, vertical_bins,
                           horizontal_bins, plot_title, plot_name):
    """
    Plots and saves a heat map based on the data from dataframe where the
    horizontal axis contains the values horizontal_bins from the
    horizontal_bins_column column of the data and the vertical axis represents
    vertical_bins from the vertical_bins_column of the data. Plots this graph
    with the title plot_title and saves it as plot_name.
    """

    # produce mask so the data just contains rows that have the desired
    # information for the vertical axis
    vertical_mask = None
    for vertical_value in vertical_bins:
        current_mask = dataframe[vertical_bins_column] == vertical_value
        if vertical_mask is None:
            vertical_mask = current_mask
        else:
            vertical_mask = vertical_mask | current_mask

    # produce mask so the data just contains rows that have the desired
    # information for the horizontal axis
    horizontal_mask = None
    for horizontal_value in horizontal_bins:
        current_mask = dataframe[horizontal_bins_column] == horizontal_value
        if horizontal_mask is None:
            horizontal_mask = current_mask
        else:
            horizontal_mask = horizontal_mask | current_mask

    # masks the data to just have the needed rows and columns
    columns_of_interest = dataframe[[vertical_bins_column,
                                     horizontal_bins_column]]
    filtered_data = columns_of_interest[vertical_mask & horizontal_mask]

    # adjust and plot data
    plt.figure(figsize=(15, 10))
    sns.histplot(
        filtered_data, x=horizontal_bins_column, y=vertical_bins_column,
        discrete=(False, False),
        cbar=True,
    )
    plt.gcf().subplots_adjust(left=0.2)
    plt.xlabel("Micro-Community Policing Plans (Neigborhood)")
    plt.title(plot_title)
    plt.savefig(plot_name)


def create_heat_map(dataframe, vertical_bins_column, horizontal_bins_column,
                    vertical_bins, horizontal_bins):
    """
    Returns a 3x3 2D array representing the heat map based on the data from
    dataframe where the horizontal axis contains the values horizontal_bins
    from the horizontal_bins_column column of the data and the vertical axis
    represents vertical_bins from the vertical_bins_column of the data.
    """
    heat_map = []  # 2D array representing the heat map
    total_count = 0  # total number of rows encompassing all the desired data

    for vertical_value in vertical_bins:
        # produce mask to just contains the rows from the current vertical
        # column
        vertical_mask = dataframe[vertical_bins_column] == vertical_value
        heat_map_row = []  # current row of the matrix
        for horizontal_value in horizontal_bins:
            # produce mask to just contains the rows from the current
            # horizontal column
            horizontal_mask = dataframe[horizontal_bins_column] \
                == horizontal_value

            # find how many rows of the data have the current horizontal and
            # vertical column
            number_of_rows = len(dataframe[vertical_mask & horizontal_mask])

            # add to the current row
            heat_map_row.append(number_of_rows)

        total_count += sum(heat_map_row)
        # add row to the matrix
        heat_map.append(heat_map_row)

    number_of_bins = len(vertical_bins)  # 3
    # average number of data values per bucket
    average_count = total_count / (number_of_bins * number_of_bins)

    # 2D array of booleans representing which heat map values are greater than
    # average
    boolean_heat_map = []

    # build up boolean heat map array
    for row in heat_map:
        current_row = []
        for value in row:
            current_row.append(value > average_count)
        boolean_heat_map.append(current_row)

    return boolean_heat_map


def loop(board, heat_pin_matrix, heat_map):
    """
    Infinite loop that uses the given arduino board to heat the pins in
    heat_pin_matrix corresponding heat map buckets that are higher than
    average (which is indicated by the heat_map parameter),
    """
    while True:
        for i in range(len(heat_pin_matrix)):
            for j in range(len(heat_pin_matrix[i])):
                heat_pin = heat_pin_matrix[i][j]  # current heat pin
                is_hot = heat_map[i][j]  # whether this pin should be heated
                # only heat this pin if is_hot, if not, don't heat
                heat_pin.write(1) if is_hot else heat_pin.write(0)

        # pauses execution for 3 seconds
        time.sleep(3)

        # turns off all pins
        for row in heat_pin_matrix:
            for heat_pin in row:
                heat_pin.write(0)

        # pauses execution for 3 seconds
        time.sleep(3)


def main():
    """
    Runs heat map arduino program.
    """
    port_name = '/dev/cu.usbmodem14201'
    board, heat_pin_matrix, heat_map = setup(port_name)

    for i in heat_map:
        print(i)

    loop(board, heat_pin_matrix, heat_map)


if __name__ == "__main__":
    main()
