from datetime import datetime

import matplotlib.pyplot as plt

from Stocks import stock
from tabulate import tabulate
import csv
import json
import pymysql
import pandas as pd


from bond import bond
from jsontodataframeparser import jsontodataframeparser
from user import user
import mplfinance as mpf
from jsonparser import jsonparser

# Assignment 6
# Author Jizhou Huang
# 2023-07-22


if __name__ == '__main__':
    inputStockData = []
    inputBondsData = []
    stockplotinput = []

    userJay = user(1, 'Jay', '.\\Lesson6_Data_Stocks.csv', '.\\Lesson6_Data_Bonds.csv')

    try:
        with open(userJay.stockBookPath, 'r') as read_obj:
            # Return a reader object which will
            # iterate over lines in the given csvfile
            csv_reader = csv.reader(read_obj)

            # convert string to list
            list_of_csv = list(csv_reader)

        print("---------------")
        print("Show input stock table for user {0}".format(userJay.getName()))
        print("---------------")
        print(tabulate(list_of_csv, headers='firstrow', tablefmt='fancy_grid'))
        inputStockData = list_of_csv
        stockplotinput = list_of_csv
    except:
        print("Cannot read the input stock csv")

    # Create tables inputs into a list of dicts
    resultDictList = []
    for i in range(1, len(inputStockData)):
        tempDict = dict(stock=inputStockData[i][0],
                        shareNo=inputStockData[i][1],
                        purchasePrice=inputStockData[i][2],
                        currentValue=inputStockData[i][3],
                        purchaseDate=inputStockData[i][4],
                        coupon='',
                        yld='',
                        el=0.0,
                        yearlyEL=0.0)

        resultDictList.append(tempDict)

    stocks1 = stock(resultDictList, "stock")
    resultDictList = stocks1.calculateEarnLoss()
    resultDictList = stocks1.calculateEarnLossYearly()

    try:
        stocks1.printPretty('.\\stockOutput.csv')
    except:
        print("Cannot write to the output stock csv")

    try:
        with open(userJay.bondBookPath, 'r') as read_obj:
            # Return a reader object which will
            # iterate over lines in the given csvfile
            csv_reader = csv.reader(read_obj)

            # convert string to list
            list_of_csv = list(csv_reader)

        print("---------------")
        print("Show input bond table for user {0}".format(userJay.getName()))
        print("---------------")
        print(tabulate(list_of_csv, headers='firstrow', tablefmt='fancy_grid'))

        inputBondsData = list_of_csv
    except:
        print("Cannot read the input bond csv")

    resultDictList = []
    for i in range(1, len(inputBondsData)):
        tempDict = dict(stock=inputBondsData[i][0],
                        shareNo=inputBondsData[i][1],
                        purchasePrice=inputBondsData[i][2],
                        currentValue=inputBondsData[i][3],
                        purchaseDate=inputBondsData[i][4],
                        coupon=inputBondsData[i][5],
                        yld=inputBondsData[i][6],
                        el=0.0,
                        yearlyEL=0.0)

        resultDictList.append(tempDict)
    bonds1 = bond(resultDictList, "bonds")
    resultDictList = bonds1.calculateEarnLoss()
    resultDictList = bonds1.calculateEarnLossYearly()

    try:
        bonds1.printPretty('.\\bondOutput.csv')
    except:
        print("Cannot write to the output bond csv")

#Plot average price with matplotlib

    for i in range(1, len(stockplotinput)):
        stockName = stockplotinput[i][0]
        NumOfStock = stockplotinput[i][1]
        jsonparser1 = jsonparser('.\\AllStocks.json',stockName, [],NumOfStock)
        dataForPlot = jsonparser1.parsejsonfrompath()
        print(dataForPlot)
        if(len(dataForPlot[0]) > 10):
            plt.plot(dataForPlot[1], dataForPlot[2], label = dataForPlot[0][0])

    plt.legend()
    plt.savefig('.\\simplePlot.png')

# Plot detail price & stock with mplfinance
    for i in range(1, len(stockplotinput)):
        stockName = stockplotinput[i][0]
        jsonparser1 = jsontodataframeparser('.\\AllStocks.json', stockName, [], 0)
        jsonparser1.plotGraph()

