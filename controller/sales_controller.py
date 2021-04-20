from model.sales import sales
from view import terminal as view




def list_transactions():
    view.print_table(sales.sale())

def add_transaction():
    list_sale = sales.sale()
    view.print_table(list_sale)


    inputs_value = view.get_inputs(["Customer ID: ", "Product: ", "Price: ", "Transaction Date: "])
    sales.create_sale(inputs_value)

    list_sale = sales.sale()
    view.print_table(list_sale)
def update_transaction():
    # view.print_error_message("Not implemented yet.")
    view.print_table(sales.sale())

    input_id = view.get_input("Transaction ID")
    inputs_value = view.get_inputs(["Customer ID: ", "Product: ", "Price: ", "Transaction Date: "])
    sales.uptade(input_id, inputs_value)
    view.print_table(sales.sale())


def delete_transaction():
    # view.print_error_message("Not implemented yet.")
    list_sale = sales.sale()
    view.print_table(list_sale)

    label = "Write: Transaction ID"
    transaction_id = view.get_input(label)

    sales.delete(transaction_id)

    list_sale = sales.sale()
    view.print_table(list_sale)


def get_biggest_revenue_transaction():
    # view.print_error_message("Not implemented yet.")
    list_sale = sales.sale()
    view.print_table(list_sale)

    message = "The transaction with biggest revenue"
    view.print_message(message)

    max_id, max_produkt = sales.get_biggest_product_revenue()
    view.print_message(max_id)
def get_biggest_revenue_product():
    # view.print_error_message("Not implemented yet.")
    list_sale = sales.sale()
    view.print_table(list_sale)

    message = "The transaction with biggest revenue"
    view.print_message(message)

    max_id, max_produkt = sales.get_biggest_product_revenue()
    view.print_message(max_produkt)

def count_transactions_between():
    # view.print_error_message("Not implemented yet.")
    list_sale = sales.sale()
    view.print_table(list_sale)

    message = "To count transaction write date"
    view.print_message(message)

    label = "Write: Date first transaction like Year, Month, Day"
    date_from = view.get_input(label)
    label1 = "Write: Date second transaction like Year, Month, Day"
    date_to = view.get_input(label1)
    number_tranaction = sales.number_of_transactions(date_from, date_to)

    view.print_message(number_tranaction)
def sum_transactions_between():
    # view.print_error_message("Not implemented yet.")

    list_sale = sales.sale()
    view.print_table(list_sale)

    message = "To count transaction write date"
    view.print_message(message)

    label = "Write: Date first transaction like Year, Month, Day"
    date_from = view.get_input(label)
    label1 = "Write: Date second transaction like Year, Month, Day"
    date_to = view.get_input(label1)
    sum_transaction = sales.sum_transaction(date_from, date_to)

    view.print_message(sum_transaction)

def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "1 --> List transactions",
               "2 --> Add new transaction",
               "3 --> Update transaction",
               "4 --> Remove transaction",
               "5 --> Get the transaction that made the biggest revenue",
               "6 --> Get the product that made the biggest revenue altogether",
               "7 --> Count number of transactions between",
               "8 --> Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
