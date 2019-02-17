import CSVreformatter as csv

import numpy as np
formatter = csv.Formatting()
locationData = formatter.formatPickup()

class Select(object):
    def __init__(self, location_id, date, startingTime, endingTime):
        self.loc = location_id
        self.date = date
        self.startingTime = int(startingTime)
        self.endingTime = int(endingTime)

    def getPickupTime(self):
        calculationList = []
        for quadruple in locationData:
            if(quadruple[0] == self.loc):
                if(str(quadruple[1]) == str(self.date)):
                    def startingPoint():
                        start = int(quadruple[2][:2])
                        return start
                    def endingPoint():
                        end = startingPoint() + 1
                        if( end > 24):
                            end = end - 24
                        return end
                        
                    if(startingPoint() >= self.startingTime and endingPoint() <= self.endingTime):
                        calculationList.append(quadruple[3])
        def carefulMedian(inputList):
            inputList = [int(string) for string in inputList]
            if (len(inputList) > 0):
                return np.median(inputList)
            else:
                print(inputList)
                return -10000000
        return carefulMedian(calculationList)
        
                    
