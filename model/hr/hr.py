""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util
ID = 0
NAME = 1
DATE = 2
DEPARTAMENT = 3
CLEARANCE = 4
DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]
def get_employees():
    
    employess = data_manager.read_table_from_file(DATAFILE)
    table = [HEADERS] +employess
    return table

def list_employees():
    employee = data_manager.read_table_from_file(DATAFILE)
    return employee

     

def new_employee_id():
    new_id = "".join(util.generate_id())
    return new_id
    
#def create(table,record):
def create(record,new_employees):
    data_manager.write_table_to_file(DATAFILE, new_employees)
    table = [HEADERS] + new_employees
    new_employees.append(record)
    return table


def read(table, id_):
    """
    Get the record from the table by id
    Args:
        table (list): table to get from the record
        id_ (str): id of the record
    Returns:
        list: record
    """
    for record in table:
        if record[ID] == id_:
            return record


def update(table, id_, record):
    """
    Updates specified record in the table.
    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update
        record (list): updated record
    Returns:
        list: table with updated record
    """
    # for row in table:
    #     if row[ID] == id_:
    #         row = []
    #         row.append(id_)
    #         row.append("lala")       
    # return table

    # kopia ze store.py
    updated_table = []
    for row in table:
        if row[0] == id_:
            updated_record = []
            updated_record.append(row[0])
            updated_record = updated_record + record
            updated_table.append(updated_record)
        else:
            updated_table.append(row)

    table[:] = updated_table
    return table


def delete():
    """
    Removes a record with a given id from the table.
    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed
    Returns:
        list: Table without specified record.
    """
    for record_index in range(len(table)):
        if table[record_index][ID] == id_:
            table.pop(record_index)
    table = data_manager.write_table_to_file('model/hr/hr.csv', table)
    return table
    