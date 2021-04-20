""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""
import datetime
from model import data_manager, util


DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]



def new_id():
    tr_id = util.generate_id()
    return tr_id
def sale():
    sales = data_manager.read_table_from_file(DATAFILE)
    table = [HEADERS] + sales
    return table


def list_sale():
    sales = data_manager.read_table_from_file(DATAFILE)
    return sales





def create_sale(inputs_value):
    sales = list_sale()
    tr_id = new_id()
    random_id = "".join(tr_id)
    print(random_id)
    new_sale = [[random_id]]
    for element in inputs_value:

        new_sale[0].extend([element])

    sales.extend(new_sale)

    data_manager.write_table_to_file(DATAFILE, sales)



def uptade(input_id, inputs_value):
    sales = list_sale()
    separator = ";"
    for row in range(len(sales)):
        tr_id = "".join(sales[row][0])
        if tr_id == (input_id):

            sales[row][1] = inputs_value[0]
            sales[row][2] = inputs_value[1]
            sales[row][3] = inputs_value[2]
            sales[row][4] = inputs_value[3]
            print(sales)
            if sales[row][1] == inputs_value[0] and sales[row][4] == inputs_value[3]:
                # data_manager.read_table_from_file(DATAFILE, sales)
                with open(DATAFILE, "w") as file:
                    for record in sales:
                        row = separator.join(record)
                        file.write(row + "\n")



def delete(input_id):
    list_sale = sale()
    for element in list_sale:
        if element[0] == input_id:
            list_sale.remove(element)

        data_manager.write_table_to_file(DATAFILE, list_sale)


def get_biggest_product_revenue():
    list_sale = sale()
    price = []
    try:
        for element in list_sale:
            price.append(element[3])
            res_max = max(price, key=lambda x: float(x))
            for element in list_sale:
                try:
                    if element[3] == res_max:
                        max_id = element[0]
                        max_produkt = element[2]
                        return max_id, max_produkt
    except IndexError:
        print()
    # res_max = max(price, key=lambda x: float(x))
    # for element in list_sale:
    #     try:
    #         if element[3] == res_max:
    #             max_id = element[0]
    #             max_produkt = element[2]
    #             return max_id, max_produkt
    #     except IndexError:
    #         pass



def number_of_transactions(input_date_1, input_date_2):


    list_sale = sale()
    list_transaction = []
    list_of_date = []
    try:
        for element  in list_sale:
            list_of_date.append(element[4])
    except IndexError:
        print()
    # for x in list_of_date:
    #     if input_date_1 <= x and x >= input_date_2:
    for x in range(len(list_of_date)):
        if (input_date_1 <= list_of_date[x] and input_date_2 >= list_of_date[x]):
            list_transaction.append(list_of_date[x])
    number_tranaction = len(list_transaction)
    return str(number_tranaction)




def sum_transaction(input_date_1, input_date_2):
    list_sale = sale()
    list_price = []
    list_of_date = []
    try:
        for element  in list_sale:
            list_of_date.append(element[4])

    except IndexError:
        print()
    print(list_of_date)
    k = len(list_of_date) - 1
    try:
        for x in range(len(list_of_date)):
            if input_date_1 <= list_of_date[x] and input_date_2 >= list_of_date[x]:
                list_price.append(list_sale[x][3])

    except IndexError:
        print()

    print(list_price)
    sum_transaction = sum(map(float, list_price))
    return str(sum_transaction)


