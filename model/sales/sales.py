""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]

LIST_SALES = data_manager.read_table_from_file(DATAFILE)
new_id = util.generate_id




def sale():
    list_sale = data_manager.read_table_from_file(DATAFILE)
    return list_sale
def create_sale(sale):
    list_sale = sale()
    sale.insert(0, util.generate_id())
    list_sale.append(sale)

    data_manager.write_table_to_file(DATAFILE, list_sale)


def uptade(input_id, input_customer, input_product, price, transaction_date):
    list_sale = sale()
    for element in list_sale:
        if element[0] == input_id:
            element[1] = input_customer
            element[2] = input_product
            element[3] = price
            element[4] = transaction_date

            list_sale.append(element)

    data_manager.write_table_to_file(DATAFILE, list_sale)

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
    except IndexError:
        print()
    res_max = max(price, key=lambda x: float(x))
    for element in list_sale:
        try:
            if element[3] == res_max:
                max_id = element[0]
                max_produkt = element[2]
                print(max_id)
                print(max_produkt)
        except IndexError:
            print()



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
    return number_tranaction




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
    return sum_transaction
(LIST_SALES)




def sale():
    list_sale = data_manager.read_table_from_file(DATAFILE)
    return list_sale
def create_sale(sale):
    list_sale = sale()
    sale.insert(0, util.generate_id())
    list_sale.append(sale)

    data_manager.write_table_to_file(DATAFILE, list_sale)


def uptade(input_id, input_customer, input_product, price, transaction_date):
    list_sale = sale()
    for element in list_sale:
        if element[0] == input_id:
            element[1] = input_customer
            element[2] = input_product
            element[3] = price
            element[4] = transaction_date

            list_sale.append(element)

    data_manager.write_table_to_file(DATAFILE, list_sale)

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
    except IndexError:
        print()
    res_max = max(price, key=lambda x: float(x))
    for element in list_sale:
        try:
            if element[3] == res_max:
                max_id = element[0]
                max_produkt = element[2]
                print(max_id)
                print(max_produkt)
        except IndexError:
            print()



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
    return number_tranaction




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
    return sum_transaction
