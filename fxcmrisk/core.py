#
# core.py -- a python wrapper class for the FXCM risk control tool
#

#import sys
from distutils.log import info
import logging
import datetime as dt
import math

from termcolor import colored 
# (pending enhance) please add an exception handling process for termcolor import
#termcolor is not default python package.

from fxcmrisk.margin import margin
import fxcmrisk.parameters as parameters

fontColor = {
    'green': '\033[92m',
    'red': '\033[93m',
    'black': '\033[0m'
    }

class rt(object):

    def __init__(self, balance =  0.00):
        logging.basicConfig(level=logging.INFO, format = '%(asctime)s | %(levelname)s | %(message)s')
        self.logger = logging.getLogger(__name__)
        self.my_balance = float(balance)
        
        msg = '*** start __init() ***'
        self.logger.info(msg)

        if self.my_balance <= 0.0:
            msg = 'no enough balance: ' + str(self.my_balance)
            self.logger.warn(msg)

        self.max_loss_per_deal = parameters.max_loss_percent_per_deal
        self.max_loss_per_day = parameters.max_loss_percent_per_day
        self.max_loss_bips = parameters.max_loss_bips_per_deal

        msg = 'max loss%       = ' + '{:.1%}'.format(self.max_loss_per_deal) + ', $' + str(self.my_balance * self.max_loss_per_deal)
        self.logger.info(msg)
        msg = 'daily max loss% = ' + '{:.1%}'.format(self.max_loss_per_day) + ', $' + str(self.my_balance * self.max_loss_per_day)
        self.logger.info(msg)
        self.my_margin = self.get_margin()

    def get_margin(self):

        """get_margin() function gets margin from margin.py
        margin.py file need regular maitenance.
        check FXCM website for most updated margin requirements
        """
        msg = '*** start get_margin() ***'
        self.logger.info(msg)

        m = margin.copy()
        
        ef_dt = dt.date.fromisoformat(m['Effective_Until'])
        if ef_dt >= dt.date.today():
            msg = 'Margin effective until: ' + m['Effective_Until'] + colored(' (Green)', 'green')
            self.logger.info(msg)
        else:
            msg = 'Margin effective until: ' + m['Effective_Until'] + colored(' (Expired. Please update margin.py)','red')
            self.logger.warn(msg)
        msg = 'Margin Level          : ' + m['Margin_Level']
        self.logger.info(msg)
        
        keys_to_remove = ['Effective_Until', 'Margin_Level']
        
        for r in keys_to_remove:
            del(m[r])
        
        msg = ''
        for s in m:
            m_1 = m[s]['margin']
            msg += s + ': ' + '{:.2f}'.format(m_1) + ', '
        self.logger.info(msg)
        return m

    def my_balance(self):
        return self.my_balance

    def cal_max_size(self, instrument = '', today_loss= 0, loss_bips = ''):
        
        #check max loss bips
        if loss_bips == '':
            loss_bips = self.max_loss_bips
            msg = 'loss bips per deal is set to default value: ' + '{:.1f}'.format(loss_bips)
            self.logger.info(msg)
        elif loss_bips <= 0:
            msg = 'loss bips per deal cannot <= 0, pls reset:' + colored('{:.1f}'.format(loss_bips),'red')
            self.logger.warn(msg)
            loss_bips = 0
            msg = 'loss bips per deal is set to default value: ' + colored('{:.1f}'.format(loss_bips),'red')
            self.logger.warn(msg)
        elif loss_bips > self.max_loss_bips:
            msg = '{:.1f}'.format(loss_bips) + colored(' exceeds max allowed loss bips per deal, please put a lower value','red')
            self.logger.warn(msg)
            loss_bips = self.max_loss_bips
            msg = 'loss bips per deal is set to default value: ' + colored('{:.1f}'.format(loss_bips),'red')
            self.logger.warn(msg)
        else:
            msg = 'loss bips per deal is set to: ' + '{:.1f}'.format(loss_bips)
            self.logger.info(msg)

        #check instrument
        if instrument == '':
            self.my_instrument = 'SPX500'
            msg = 'default instrument: ' + self.my_instrument
            self.logger.info(msg)
        elif instrument.upper() in self.my_margin:
            self.my_instrument = instrument.upper()
            msg = 'instrument: ' + self.my_instrument
            self.logger.info(msg)
        else:
            msg = 'instrument NOT in margin.py' + colored(' (please re-input instrument or update margin.py','red')
            self.logger.warn(msg)
            self.my_instrument = 'SPX500'
            msg = 'already set to default instrument: ' + colored(self.my_instrument, 'green')
            self.logger.warn(msg)
        
        # how to calculate max lots:
        # All margin values are displayed for 1,000 FX (or) 1 Contract CFD.
        # -- FX --
        # 1 standard lot (size) = $ 100,000
        # instrument minimum size, e.g. EUR/USD = 1,000 / 100,000 = 0.01
        # gain/loss for 1 bip change of 1 standard size = $100,000 * 0.0001 = $10
        # gain/loss for 1 bip change of 1 minimum size = $10 * 0.01 = $0.1


        # a = instrument minmum size: e.g. EUR/USD = 1,000 / 100,000 = 0.01. price change of 1 bip = 1,000 * 0.0001 = 
        # -max_size = max_margin / margin_required_by_symbol
        # --max_margin = min(max_loss_each_deal, max_loss_per_day - loss occured today)
        # ----max loss each deal = balance * max loss percentage each deal (this is a parameter)
        # ----max loss per day = balance * max loss percentage per day (this is a parameter)
        # --margin required by symbol: defined in margin.py
        
        instrument_margin  = self.my_margin[self.my_instrument]['margin']
        instrument_bipvalue = self.my_margin[self.my_instrument]['bipvalue']
        instrument_miniszie = self.my_margin[self.my_instrument]['minisize']
        #msg = 'margin level: ' + '${:.2f}'.format(instrument_margin)
        #self.logger.info(msg)\\\\\\\\\
        max_loss = min(self.my_balance * self.max_loss_per_deal, (self.my_balance * self.max_loss_per_day - today_loss))
        msg = 'max loss    : ' + '${:.2f}'.format(max_loss)
        self.logger.info(msg)
        
        # loss=max_size * max_bips * 10 <= max_loss
        # margin=max_size * margin_level <= balance - max_loss
        # so max_size = min (max_loss/max_bips/0.1, (balance-max_loss) / margin_level)
        max_size_1 = max_loss / loss_bips / instrument_bipvalue
        max_size_2 = (self.my_balance - max_loss) / instrument_margin
        print(max_size_1,max_size_2)

        max_size = min(max_size_1, max_size_2)
        print(max_size)
        if max_size < instrument_miniszie:
            max_size = 0.0
            print(
                self.my_instrument,
                '| Max Size: ', 
                colored(max_size, attrs=['bold']),
                colored(' (< instrument minisize)', 'red')
            )
        else:
#            max_size= max_size // 0.01 / 100 #some bug here, if max_size=1.0, the result will be 0.99...
            max_size = math.floor(max_size*100) / 100
            print(
                self.my_instrument,
                '| Max Size: ', 
                colored(max_size,'green', attrs=['bold']),
                '| Max Loss: ',
                colored('${:.2f}'.format(max_loss),'red',attrs=['bold'])
            )

        
        return max_size
    
