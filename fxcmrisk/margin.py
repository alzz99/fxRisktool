
# All values are displayed for 1,000 FX (or) 1 Contract CFD.

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