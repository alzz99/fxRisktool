import logging
import datetime as dt
import math

from risktool.margin import margin
import risktool.parameters as parameters


class sq(object):

    def __init__(self, balance =  0.00):
        logging.basicConfig(level=logging.INFO, format = '%(asctime)s | %(levelname)s | %(message)s')
        self.logger = logging.getLogger(__name__)
        self.my_balance = float(balance)

    ##
    # margin level  = 30%
    # margin calculation: 
    # balance
    # currency pairs
    # Min_size = 0.01, 1 standard size = 100,000 base currency
    # Max_size = 200.0
    # Margin = 0.01         #i.e. 1%
    # EUR/USD Rate = 1.09   
    # 
