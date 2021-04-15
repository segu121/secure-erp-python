from model.crm import crm
from view import terminal as view


def list_customers():
    view.print_error_message("Not implemented yet.")


def add_customer():
    view.print_error_message("Not implemented yet.")


def update_customer():
    view.print_error_message("Not implemented yet.")


def delete_customer():
    view.print_error_message("Not implemented yet.")


def get_subscribed_emails():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["1 ---> List customers",
               "2 ---> Add new customer",
               "3 ---> Update customer",
               "4 ---> Remove customer",
               "5 ---> Subscribed customer emails",
               "6 ---> Back to main menu"]
    view.print_menu("  ***ERP***\nCustomer Relationship Management:", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation: ")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
