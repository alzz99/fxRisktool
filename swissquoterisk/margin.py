
# All values are displayed for 1,000 FX (or) 1 Contract CFD.

from traceback import format_exc


margin_0 = {
    'Effective_Until': '2022-02-28',
    'Margin_Level': '400:1',
    # Currency
    'AUD/USD': 2.00,
    'EUR/USD': 3.25,
    'USD/JPY': 2.50,
    'GBP/USD': 3.75,
    'USD/CAD': 2.50,
    #Index
    'AUS200': 1.40,
    'ESP35': 2.65,
    'NAS100': 8.00,
    'SPX500': 24.30,
    'US2000': 5.63,

    #metal
    'XAUUSD': 10.15,
    'XAGUSD': 13.20
}


margin = {
    'Effective_Until': '2022-02-28',
    'Margin_Level': '400:1',

    #strucute{instrument: {'margin','type',}}
    #forex
    'AUD/USD': {'margin': 2.00, 'type': 'forex', 'minisize':0.01,'bippostion': 0.0001,'bipvalue': 10.0},
    'EUR/USD': {'margin': 3.25, 'type': 'forex', 'minisize':0.01,'bippostion': 0.0001, 'bipvalue': 10.0},
    'USD/JPY': {'margin': 2.50, 'type': 'forex', 'minisize':0.01,'bippostion': 0.0001, 'bipvalue': 10.0},
    'GBP/USD': {'margin': 3.75, 'type': 'forex', 'minisize':0.01,'bippostion': 0.0001, 'bipvalue': 10.0},
    'USD/CAD': {'margin': 2.50, 'type': 'forex', 'minisize':0.01,'bippostion': 0.0001, 'bipvalue': 10.0},
    
    #indicies
    'AUS200': {'margin': 1.40, 'type': 'indices', 'minisize':0.01,'bippostion': 1.0, 'bipvalue': 1.0},
    'ESP35' : {'margin': 2.65, 'type': 'indices','minisize':0.01,'bippostion': 1.0, 'bipvalue': 1.0},
    'NAS100': {'margin': 8.00, 'type': 'indices','minisize':0.01,'bippostion':1.0, 'bipvalue': 1.0},
    'SPX500': {'margin': 24.30, 'type': 'indices','minisize':1.0,'bippostion':0.1, 'bipvalue': 1.0},
    'US2000': {'margin': 5.63, 'type': 'indices','minisize':0.01,'bippostion':0.1, 'bipvalue': 1.0},
    'UK100' : {'margin': 5.63, 'type': 'indices','minisize':0.01,'bippostion':1.0, 'bipvalue': 1.0},

    #metal
    'XAU/USD': {'margin': 10.15, 'type': 'metal','minisize':0.01,'bippostion':0.01, 'bipvalue': 1.0},
    'XAG/USD': {'margin': 13.20, 'type': 'metal','minisize':0.01,'bippostion':0.01, 'bipvalue': 1.0},

    #crypto
    'BTC/USD': {'margin': 10.15, 'type': 'metal','minisize':0.01,'bippostion':1.0, 'bipvalue': 1.0},
    'ETH/USD': {'margin': 13.20, 'type': 'metal','minisize':0.01,'bippostion':1.0, 'bipvalue': 1.0},
}


#Swiss quote
#Margin Level Calculation
#
#((Account Balance + Unrealized P&L)/Margin requirement on net open position) x 100 = Margin Level
#
#Example: Trader X has a USD 10'000 balance with an unrealized P&L of + USD 1'000. The open positions include long USDCHF 300'000 and short USDCHF 200'000. Net open position is USDCHF 100'000
#
#((USD 10'000 + USD 1'000)/ USD 1'000) x 100 = 1100% Margin Level
#
#Stop Out Level
#Subject to the limitations set forth in the General Terms and Conditions, the Risk Disclosure Statement and the Special Terms and Conditions for Forex, when the Margin Level falls below 30%, positions with the largest loss (regardless of their size) will be liquidated first, until the margin level is back to 30% or more.
#
#Please note that, in the case of aggregated positions exceeding the maximum transaction size on MetaTrader 5, such positions will first be liquidated up to the maximum transaction size. If the margin level is back to 30% or more after this first liquidation, no further liquidation takes place.