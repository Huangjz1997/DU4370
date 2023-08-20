from Stocks import  stock
from tabulate import tabulate

class bond(stock):
    def __init__(self, inputDict, name):
        super().__init__(inputDict, name)

    def calculateEarnLoss(self):
        super().calculateEarnLoss()


    def calculateEarnLossYearly(self):
        super().calculateEarnLossYearly()

    def printPretty(self,  destinationPath):
        super().printPretty(destinationPath)
