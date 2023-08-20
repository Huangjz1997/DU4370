import csv
from datetime import datetime
import numpy as np
from tabulate import tabulate


class stock:

    def __init__(self, inputDict, name):
        self.inputDict = inputDict
        self.name = name

    # calcluate the earn/loss for a specific stock
    def calculateEarnLoss(self):
        for stock in self.inputDict:
            tempIncome = (np.float64(stock["currentValue"]) - np.float64(stock["purchasePrice"])) * np.float64(stock["shareNo"])
            stock.update({"el": round(tempIncome, 2)})
        return self.inputDict

    # calculate the yearlyE/L
    def calculateEarnLossYearly(self):
        for stock in self.inputDict:
            dPurchase = datetime.strptime(stock["purchaseDate"], "%m/%d/%Y")
            dNow = datetime.today()
            delta = dNow - dPurchase
            yearDiff = delta.days / 365.2425
            tempIncome = ((np.float64(stock["currentValue"]) - np.float64(stock["purchasePrice"])) / np.float64(stock["purchasePrice"])) / yearDiff * 100
            stock.update({"yearlyEL": str(round(tempIncome, 2)) + "%"})

        return self.inputDict

    # print out in a pretty format
    def printPretty(self, destinationPath):
        outputResult = [["Stock", "Shares#", "Earnings/Loss", "Yearly Earning/Loss"]]
        for stock in self.inputDict:
            stockPrint = []
            stockPrint.append(stock["stock"])
            stockPrint.append(stock["shareNo"])
            stockPrint.append(stock["el"])
            stockPrint.append(stock["yearlyEL"])
            outputResult.append(stockPrint)
        print("---------------")
        print("Print Result table to file path")
        print("---------------")
        with open(destinationPath, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(outputResult)