import csv
import os
from data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('**' * 23)
    print('********** Real Estate Data miner  ***********')
    print('**' * 23)


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        purchases = []
        reader = csv.DictReader(fin)

        for row in reader:
            # print("Bed Count: {}".format(row['beds']),type(row['beds']))
            p = Purchase.create_from_dict(row)
            purchases.append(p)
        # print(purchases[0].__dict__)
        return purchases

#def get_price(p):
#    return p.price


def query_data(data):
    #data.sort(key=get_price);
    data.sort(key= lambda p: p.price)
    high_purchase = data[-1]
    low_purchase = data[0]

    print(high_purchase.price)
    print(low_purchase.price)


if __name__ == '__main__':
    main()
