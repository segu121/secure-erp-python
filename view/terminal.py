def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(title)
    for options in list_options:
        print (options)

   


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """

    pass


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    print(label, ":\n", result)


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table,HEADERS):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    table.insert(0, HEADERS)
    maxlength = []
    for column in range(len(table[0])):
        length = 0
        for row in range(len(table)):
            if len(str(table[row][column])) > length:
                length = len(str(table[row][column]))
        maxlength.append(length)

    for row_i in range(len(table)):
        row = table[row_i]
        print()
        for cell_j in range(len(row)):
            cell = row[cell_j]
            width = maxlength[cell_j]
            print(" | " + cell.center(width) + " | ", end='')


def get_input(label):
    
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    
    user_input = input(label)
    return user_input

    
   


def get_inputs(labels):
    inputs = []

    for elements in labels:
        user_inputs= input(elements)
        inputs.append(user_inputs)

    return inputs



def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message

    """
    print("ERROR: ", message)
    
