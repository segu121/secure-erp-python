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
    print("DONE!"  + message)
    


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
def print_table(table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    
    list_len_records = []
    longest_length_of_word = []
    for i in range(len(table)):
        list_len_records.append([])
        for record in table[i]:
            list_len_records[i].append(len(record))
        longest_length_of_word.append((max(list_len_records[i])))
    for index, record in enumerate(table):
        line = '|'.join(str(x).ljust(max(longest_length_of_word)) for x in record)
        if index == 0:
            print("-" * len(line))
        print(line)
        if index == 0 or index + 1 == len(table):
            print("-" * len(line))

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
        user_inputs = input(elements)
        inputs.append(user_inputs)

    return inputs



def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message

    """
    print("ERROR: ", message)
    
