from model.hr import hr
from view import terminal as view


def list_employees():
    view.print_table(hr.get_employees())
    


def add_employee():
    view.print_error_message("Not implemented yet.")


def update_employee():
    view.print_error_message("Not implemented yet.")


def delete_employee():
    view.print_error_message("Not implemented yet.")


def get_oldest_and_youngest():
    view.print_error_message("Not implemented yet.")


def get_average_age():
    view.print_error_message("Not implemented yet.")


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    view.print_error_message("Not implemented yet.")


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


def run_operation(options):

     
    if options == 1:
        list_employees()
    elif options == 2:
        add_employee()
    elif options == 3:
        update_employee()
    elif options == 4:
        delete_employee()
    elif options == 5:
        get_oldest_and_youngest()
    elif options == 6:
        get_average_age()
    elif options == 7:
        next_birthdays()
    elif options == 8:
        count_employees_with_clearance()
    elif options == 9:
        count_employees_per_department()
    elif options == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options =["1 ---> List employees",
            "2 ---> Add new employee",
            "3 ---> Update employee",
            "4 ---> Remove employee",
            "5 ---> Oldest and youngest employees",
            "6 ---> Employees average age",
            "7 ---> Employees with birthdays in the next two weeks",
            "8 ---> Employees with clearance level",
            "9 ---> Employee numbers by department",
            "0 ---> Back to main menu"]
    view.print_menu("\n   ***ERP***\nHuman resources:", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation: ")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
