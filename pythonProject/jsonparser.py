import json
from datetime import datetime


class jsonparser():
    def __init__(self, path, stockname, datalist, numOfShares):
        self.path = path
        self.stockname = stockname
        self.datalist = datalist
        self.numOfShares = numOfShares

    def parsejsonfrompath(self):
         try:
            with open(self.path, 'r') as f:
                portfolio = json.load(f)
                dates = []
                dates = []
                prices = []
                stockname = []
                for stock in portfolio:
                    if (stock['Symbol'] == self.stockname):
                        dates.insert(0,datetime.strptime(stock['Date'], "%d-%b-%y"))
                        prices.insert(0,stock['Close'] * (float(self.numOfShares)))
                        stockname.append(self.stockname)
                self.datalist.append(stockname)
                self.datalist.append(dates)
                self.datalist.append(prices)

            return self.datalist
         except:
            print('cant open file {0}'.format(self.path))

