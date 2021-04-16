""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]


def get_customers():
    customers = read_file(DATAFILE)
    return customers


def read_file(file_name): #+(sep="\t")
    lines = []
    with open(file_name, 'r') as file_hanlde:
        for line in file_hanlde.readlines():
            line = line.replace("\n","").replace("\r","")
            line = line.split(";") #(sep)   uzywamy do  ;
            lines.append(line)

    return lines
