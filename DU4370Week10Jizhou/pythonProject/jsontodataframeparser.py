import json
from datetime import datetime
import pandas as pd
from jsonparser import jsonparser
import mplfinance as mpf

class jsontodataframeparser(jsonparser):
    def __init__(self, path, stockname, datalist, numOfShares):
        super().__init__(path, stockname, datalist, numOfShares)

    def parsejsonfrompath(self):
         # try:
            dataframeforplot = pd.read_json(self.path)
            return dataframeforplot
         # except:
         #    print('cant open file {0}'.format(self.path))

    def plotGraph(self):
        dataframeforplot = self.parsejsonfrompath()
        plottitle = "The stock detail price & volumn plot of " + self.stockname
        filename = ".\mplfinanceOutput\price&volumnplotOf" + self.stockname + ".png"
        #extract the records by stock name
        dataframeforplot = dataframeforplot[dataframeforplot['Symbol'] == self.stockname]

        # Clean the input with correct datatype
        dataframeforplot['Date'] = pd.to_datetime(dataframeforplot['Date'])
        dataframeforplot['Open'] = pd.to_numeric(dataframeforplot['Open'], errors='coerce')
        dataframeforplot['High'] = pd.to_numeric(dataframeforplot['High'], errors='coerce')
        dataframeforplot['Low'] = pd.to_numeric(dataframeforplot['Low'], errors='coerce')
        dataframeforplot['Close'] = pd.to_numeric(dataframeforplot['Close'], errors='coerce')
        #remove Nan records
        dataframeforplot = dataframeforplot.dropna()

        #print(dataframeforplot)
        df = dataframeforplot.set_index(dataframeforplot['Date'])
        mpf.plot(df,type='candle',mav=(3,6,9),volume=True,show_nontrading=True,datetime_format="%Y-%b-%d", title = plottitle,savefig=filename)

