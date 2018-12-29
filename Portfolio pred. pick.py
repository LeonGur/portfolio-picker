#Leon Gurtler
#Porftolio pick

import quandl
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import datetime


risk_number = input("Please enter your optimal risk level (1-10). Note that a high risk level has the potential of achieving higher return.")
while input_validation(risk_number) == False:
    risk_number = input("Please make ensure that the risk level you enter is an integer between 1 and 10")
# "return_risk_weights" is a list that contains the weights, adjusted accordingly to the user input
return_risk_weights = [(risk_number * 0.1), (1 - risk_number * 0.1)]


stock_list = []
#These are the tickers of all S&P500 share, which include 500 companies and 505 stocks
tickers = ['MMM', 'ABT', 'ABBV', 'ABMD', 'ACN', 'ATVI', 'ADBE', 'AMD', 'AAP', 'AES', 'AMG', 'AFL', 'A', 'APD', 'AKAM', 'ALK', 'ALB', 'ARE', 'ALXN', 'ALGN', 'ALLE', 'AGN', 'ADS', 'LNT',
            'ALL', 'GOOGL', 'GOOG', 'MO', 'AMZN', 'AEE', 'AAL', 'AEP', 'AXP', 'AIG', 'AMT', 'AWK', 'AMP', 'ABC', 'AME', 'AMGN', 'APH', 'APC', 'ADI', 'ANSS', 'ANTM', 'AON', 'AOS', 'APA',
            'AIV', 'AAPL', 'AMAT', 'APTV', 'ADM', 'ARNC', 'ANET', 'AJG', 'AIZ', 'T', 'ADSK', 'ADP', 'AZO', 'AVB', 'AVY', 'BHGE', 'BLL', 'BAC', 'BK', 'BAX', 'BBT', 'BDX', 'BRK-B', 'BBY',
            'BIIB', 'BLK', 'HRB', 'BA', 'BKNG', 'BWA', 'BXP', 'BSX', 'BHF', 'BMY', 'AVGO', 'BR', 'BF-B', 'CHRW', 'COG', 'CDNS', 'CPB', 'COF', 'CAH', 'KMX', 'CCL', 'CAT', 'CBOE', 'CBRE',
            'CBS', 'CELG', 'CNC', 'CNP', 'CTL', 'CERN', 'CF', 'SCHW', 'CHTR', 'CVX', 'CMG', 'CB', 'CHD', 'CI', 'XEC', 'CINF', 'CTAS', 'CSCO', 'C', 'CFG', 'CTXS', 'CLX', 'CME', 'CMS', 'KO',
            'CTSH', 'CL', 'CMCSA', 'CMA', 'CAG', 'CXO', 'COP', 'ED', 'STZ', 'COO', 'CPRT', 'GLW', 'COST', 'COTY', 'CCI', 'CSX', 'CMI', 'CVS', 'DHI', 'DHR', 'DRI', 'DVA', 'DE', 'DAL', 'XRAY',
            'DVN', 'FANG', 'DLR', 'DFS', 'DISCA', 'DISCK', 'DISH', 'DG', 'DLTR', 'D', 'DOV', 'DWDP', 'DTE', 'DRE', 'DUK', 'DXC', 'ETFC', 'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'EMR',
            'ETR', 'EOG', 'EFX', 'EQIX', 'EQR', 'ESS', 'EL', 'EVRG', 'ES', 'RE', 'EXC', 'EXPE', 'EXPD', 'ESRX', 'EXR', 'XOM', 'FFIV', 'FB', 'FAST', 'FRT', 'FDX', 'FIS', 'FITB', 'FE', 'FISV',
            'FLT', 'FLIR', 'FLS', 'FLR', 'FMC', 'FL', 'F', 'FTNT', 'FTV', 'FBHS', 'BEN', 'FCX', 'GPS', 'GRMN', 'IT', 'GD', 'GE', 'GIS', 'GM', 'GPC', 'GILD', 'GPN', 'GS', 'GT', 'GWW', 'HAL',
            'HBI', 'HOG', 'HRS', 'HIG', 'HAS', 'HCA', 'HCP', 'HP', 'HSIC', 'HSY', 'HES', 'HPE', 'HLT', 'HFC', 'HOLX', 'HD', 'HON', 'HRL', 'HST', 'HPQ', 'HUM', 'HBAN', 'HII', 'IDXX', 'INFO',
            'ITW', 'ILMN', 'IR', 'INTC', 'ICE', 'IBM', 'INCY', 'IP', 'IPG', 'IFF', 'INTU', 'ISRG', 'IVZ', 'IPGP', 'IQV', 'IRM', 'JKHY', 'JEC', 'JBHT', 'JEF', 'SJM', 'JNJ', 'JCI', 'JPM',
            'JNPR', 'KSU', 'K', 'KEY', 'KEYS', 'KMB', 'KIM', 'KMI', 'KLAC', 'KSS', 'KHC', 'KR', 'LB', 'LLL', 'LH', 'LRCX', 'LW', 'LEG', 'LEN', 'LLY', 'LNC', 'LIN', 'LKQ', 'LMT', 'L', 'LOW',
            'LYB', 'MTB', 'MAC', 'M', 'MRO', 'MPC', 'MAR', 'MMC', 'MLM', 'MAS', 'MA', 'MAT', 'MKC', 'MXIM', 'MCD', 'MCK', 'MDT', 'MRK', 'MET', 'MTD', 'MGM', 'KORS', 'MCHP', 'MU', 'MSFT',
            'MAA', 'MHK', 'TAP', 'MDLZ', 'MNST', 'MCO', 'MS', 'MOS', 'MSI', 'MSCI', 'MYL', 'NDAQ', 'NOV', 'NKTR', 'NTAP', 'NFLX', 'NWL', 'NFX', 'NEM', 'NWSA', 'NWS', 'NEE', 'NLSN', 'NKE',
            'NI', 'NBL', 'JWN', 'NSC', 'NTRS', 'NOC', 'NCLH', 'NRG', 'NUE', 'NVDA', 'ORLY', 'OXY', 'OMC', 'OKE', 'ORCL', 'PCAR', 'PKG', 'PH', 'PAYX', 'PYPL', 'PNR', 'PBCT', 'PEP', 'PKI',
            'PRGO', 'PFE', 'PCG', 'PM', 'PSX', 'PNW', 'PXD', 'PNC', 'RL', 'PPG', 'PPL', 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PEG', 'PSA', 'PHM', 'PVH', 'QRVO', 'PWR', 'QCOM', 'DGX', 'RJF',
            'RTN', 'O', 'RHT', 'REG', 'REGN', 'RF', 'RSG', 'RMD', 'RHI', 'ROK', 'ROL', 'ROP', 'ROST', 'RCL', 'CRM', 'SBAC', 'SCG', 'SLB', 'STX', 'SEE', 'SRE', 'SHW', 'SPG', 'SWKS', 'SLG',
            'SNA', 'SO', 'LUV', 'SPGI', 'SWK', 'SBUX', 'STT', 'SYK', 'STI', 'SIVB', 'SYMC', 'SYF', 'SNPS', 'SYY', 'TROW', 'TTWO', 'TPR', 'TGT', 'TEL', 'FTI', 'TXN', 'TXT', 'TMO', 'TIF', 'TWTR',
            'TJX', 'TMK', 'TSS', 'TSCO', 'TDG', 'TRV', 'TRIP', 'FOXA', 'FOX', 'TSN', 'UDR', 'ULTA', 'USB', 'UAA', 'UA', 'UNP', 'UAL', 'UNH', 'UPS', 'URI', 'UTX', 'UHS', 'UNM', 'VFC', 'VLO',
            'VAR', 'VTR', 'VRSN', 'VRSK', 'VZ', 'VRTX', 'VIAB', 'V', 'VNO', 'VMC', 'WMT', 'WBA', 'DIS', 'WM', 'WAT', 'WEC', 'WCG', 'WFC', 'WELL', 'WDC', 'WU', 'WRK', 'WY', 'WHR', 'WMB',
            'WLTW', 'WYNN', 'XEL', 'XRX', 'XLNX', 'XYL', 'YUM', 'ZBH', 'ZION', 'ZTS']

#the build in .sort() funktion provided is not working, as this is a 2D array, this is why I implemented a bubble sort function that takes
#the xth value in each element of the array as an input for the comparison
def bubble_sort(list, x):
    for passnum in range(len(list) -1, 0, -1):
        for i in range(passnum):
            if list[i][x] < list[i+1][x]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

def input_validation(Var):
    check = True
    try:
        int(Var)
    except TypeError:
        check = False
    if Var > 10 and Var < 1:
        check = False

#in the following lines comp_data and a_comp_data are created as pandas DataFrames that will be able to hold the data loaded from yahoo finance
comp_data = pd.DataFrame()
a_comp_data = pd.DataFrame()

count_up = 1
#append the relevant data of each s&P500 stock into the comp_data data frame. The historical data dates back 5 years and is taken form the yahoo finance API
print('loading the historical data:')
start_time = (datetime.datetime.now()).timestamp()
#print(start_time)
for t in tickers:
    comp_data[t] = wb.DataReader(t, data_source = 'yahoo', start = '2015-01-01')['Adj Close']
    a_comp_data[t] = wb.DataReader(t, data_source = 'yahoo', start = '2018-01-01')['Adj Close']
    #print(str(count_up) + '/' + str(len(tickers)))
    #The next line calculates a prediction for the amount of time it will take to read in all tickers, and prints it after 10 tickers have been read in
    if count_up % 10 == 0:
        print(str(round((((datetime.datetime.now()).timestamp() - start_time)/count_up) * ((len(tickers)) - count_up), 2)) + " seconds remaining")
    count_up += 1


#calculate the avarage rate of return of each stock on yearly basis
comp_returns = (comp_data / comp_data.shift(1))-1
comp_annual_returns = comp_returns.mean() * 250

a_comp_returns = (a_comp_data / a_comp_data.shift(1))-1
a_comp_annual_returns = a_comp_returns.mean() * 250

#calculate the avarage share variance
share_variance = comp_returns.var() * 250

a_share_variance = a_comp_returns.var() * 250


#append to the stock_list array with the structure: ticker, avg. annual returns, variance, last years avg. return, last years variance, balance_score
for t in tickers:
    stock_list.append( [t, comp_annual_returns[t], share_variance[t], a_comp_annual_returns[t], a_share_variance[t],
     ((comp_annual_returns[t] + 0.5 * a_comp_annual_returns[t]) * return_risk_weights[0] +
     (share_variance[t] - share_variance[t] * 10 *return_risk_weights[1]) +
     0.5 *(a_share_variance[t] - a_share_variance[t] * 10 * return_risk_weights[1])) ])


#-------------the above code is necessary to lead the relevant data and get it into the right
#format to make meaningful decisions based on it--------------------------------------------#

#-------------The following code will pick the best fitting portfolio based on the user input-----------#
bubble_sort(stock_list, 5)
for x in range(1, ((11 - risk_number) * 3)+1):
    print(str(x) + "." + str(stock_list[x][0]))
