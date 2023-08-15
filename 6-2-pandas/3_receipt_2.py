import numpy as np
import pandas as pd


def cheque(pricelist, **goods):
    # product, price, number, cost
    prod_num = dict()
    for product, number in goods.items():
        prod_num[product] = prod_num.setdefault(product, 0) + number
    prod_num = {prod: prod_num[prod] for prod in sorted(prod_num)}
    ch = pd.DataFrame({'product': prod_num.keys(),
                       'price': [pricelist.loc[pos] for pos in prod_num.keys()],
                       'number': prod_num.values()})
    ch['cost'] = ch['price'] * ch['number']
    return ch.sort_values(['product'])


products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
print(result)
