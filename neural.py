#!/usr/bin/env python

import csv

class UserData:
    data = []

    def __init__(self, data):
        self.data = data
        self.c_RowNum = data[0].index('Rownum')
        #ToDo: Remove hard coding of target cell and other cells
        self.c_Target_x = data[0].index('L1547777_x')
        self.c_Target = data[0].index('L1547777')
        self.c_CandidateArr_x = [
            data[0].index('L1022212_x'),
            data[0].index('L1100545_x'),
            data[0].index('L1132034_x'),
            data[0].index('L1132035_x'),
            data[0].index('L1143298_x'),
            data[0].index('L1384705_x'),
            data[0].index('L264453_x'),
            data[0].index('L264454_x') ]
        self.c_CandidateArr = [
            data[0].index('L1022212'),
            data[0].index('L1100545'),
            data[0].index('L1132034'),
            data[0].index('L1132035'),
            data[0].index('L1143298'),
            data[0].index('L1384705'),
            data[0].index('L264453'),
            data[0].index('L264454') ]

    #Sets target cell string column parameters
    def setTarget(self, newTarget):
        self.c_Target = self.data[0].index(newTarget)
        self.c_Target_x = self.data[0].index('%s_x' % newTarget)
        return 1;

    #Sets candidate cells column parameters
    def setCandidates(self, newCadidateArr):
        return 1;
    
    def getRow(self, rowNum):
        for index, row in enumerate(self.data):
            if row[self.c_RowNum] == rowNum:
                return row;

    def printSampleData(self):
        maxCount = 2
        for index, row in enumerate(self.data):
            label = "Header" if index == 0 else "Data"
            print("%s Row : %s" % (label, index))
            print(row)
            if index >= maxCount:
                break

def readFile(fileName):
    with open(fileName, newline='') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        retArr = []
        for row in readCSV:
            retArr.append(row)
        return retArr;
        
        
            


def main():
    neural = UserData(readFile('users.csv'))
    neural.printSampleData()
    neural.setTarget('L1547777')
    print("Target value x columns : %s" % neural.c_Target_x)
    print("Target user# columns : %s" % neural.c_Target)
    print("candidate value x columns : %s" % neural.c_CandidateArr_x)
    print("candidate user# columns : %s" % neural.c_CandidateArr)
    print("\nTesting testing\n-------------------")
    print("row 1 %s" % neural.getRow('1'))
    print("row 499 %s" % neural.getRow('499'))

main()
