"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

To draw all the lines and data in order to show the rank of the name and its trend in different decades.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    space_to_drawline = width - 2*GRAPH_MARGIN_SIZE       # the range to draw lines
    x_coordinate = GRAPH_MARGIN_SIZE + (space_to_drawline / len(YEARS)) * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')                                  # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # the upper line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    # the lower line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    # draw vertical lines and the year according to the YEARS
    for i in range(len(YEARS)):
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, i)  # to get the x coordinate for the line of the year
        year_text = YEARS[i]                              # the year this loop should be put on the canvas
        canvas.create_line(x_coordinate, 0,
                           x_coordinate, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x_coordinate + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=year_text,
                           anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    ################################
    for j in range(len(lookup_names)):
        list_rank = []                                        # contain the rank of the name in different years in order
        color = COLORS[j % len(COLORS)]                       # get color according to the number of names entered
        for year in YEARS:                                    # YEARS are all int
            if str(year) in name_data[lookup_names[j]]:       # check if the rank of name appear in the year
                rank = name_data[lookup_names[j]][str(year)]  # the year in name_data are string
                list_rank.append(rank)
            else:                                             # the rank isn't high enough to get in the first 1000
                list_rank.append('*')

        # get the first rank dot of the name (rank in first year)
        x1 = get_x_coordinate(CANVAS_WIDTH, 0)
        if list_rank[0] == '*':
            y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
        else:
            y1 = int(list_rank[0])*(CANVAS_HEIGHT - 2*GRAPH_MARGIN_SIZE)//MAX_RANK + GRAPH_MARGIN_SIZE
        canvas.create_text(x1+TEXT_DX, y1, text=lookup_names[j] + ' ' + list_rank[0], anchor=tkinter.SW, fill=color)

        # get the dot of rank in the every next year
        for i in range(len(YEARS)-1):
            x2 = get_x_coordinate(CANVAS_WIDTH, i+1)
            rank = list_rank[i+1]
            if list_rank[i+1] == '*':
                y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            else:
                y2 = int(rank)*(CANVAS_HEIGHT - 2*GRAPH_MARGIN_SIZE)//MAX_RANK + GRAPH_MARGIN_SIZE
            canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)
            canvas.create_text(x2 + TEXT_DX, y2, text=lookup_names[j] + ' ' + rank,
                               anchor=tkinter.SW, fill=color)
            (x1, y1) = (x2, y2)                               # reassign the dot to be connected with the next rank dot


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
