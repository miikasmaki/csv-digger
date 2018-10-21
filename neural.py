#!/usr/bin/env python

import csv
from decimal import *
import locale

getcontext().prec = 7
locale.setlocale(locale.LC_ALL, '')


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
        #Find column indexes and check that both are found. .index() throws if not found
        target = self.data[0].index(newTarget)
        target_x = self.data[0].index('%s_x' % newTarget)
        #Store new values
        self.c_Target = target
        self.c_Target_x = target_x
        return 1

    #Sets candidate cells column parameters
    def setCandidates(self, newCandidateArr):
        newArr = []
        newArr_x = []
        #Find column indexes
        for item in newCandidateArr:
            newArr.append(self.data[0].index(item))
            newArr_x.append(self.data[0].index('%s_x' % item))
        #Store new values if all found
        self.c_CandidateArr = newArr
        self.c_CandidateArr_x = newArr_x
        return 1
    
    def getRow(self, rowNum):
        for index, row in enumerate(self.data):
            if row[self.c_RowNum] == rowNum:
                return row

    #Returns Decimal string sum of average userAmount of candidate list 
    def getSumCandidateUsers(self, rowNum):
        candidateValues = ['0.1', '0.2', '0.3']
        targetRow = self.getRow(rowNum)
        rawCand = [targetRow[i] for i in self.c_CandidateArr] #Filter candidate data
        candidateValues = [locale.format_string(x.replace(',','.'), x) for x in rawCand]
        decData = list(map(Decimal, candidateValues))
        return sum(decData)

    def printSampleData(self):
        print("Sample first two rows of data array")
        print("***")
        for index, row in enumerate(self.data[:2]):
            label = "Header" if index == 0 else "Data"
            print("%s Row : %s" % (label, index))
            print(row)
        print("***")

def readFile(fileName):
    with open(fileName, newline='') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        retArr = []
        for row in readCSV:
            retArr.append(row)
        return retArr
        
def printUsersFromRow(row, instance):
    rowIndex = instance.data.index(instance.getRow(row))
    targetUsers = instance.data[rowIndex][instance.c_Target]
    testMessage = "Row %s Target users: %s, Candidate users sum: %s"
    print(testMessage % (row, targetUsers, instance.getSumCandidateUsers(row)))

def testingTesting(neural):
    print("\nTesting testing.\n-------------------")
    print("row 1 %s" % neural.getRow('1'))
    print("row 163 %s" % neural.getRow('163'))
    print("row 331 %s" % neural.getRow('331'))
    print("row 499 %s" % neural.getRow('499'))

    print("Try to adjust candidate list")
    org_c_CandidateArr = neural.c_CandidateArr
    org_c_CandidateArr_x = neural.c_CandidateArr_x
    neural.setCandidates(['L264453','L264454'])
    print("candidate value x columns : %s" % neural.c_CandidateArr_x)
    print("candidate user# columns : %s" % neural.c_CandidateArr)
    testRow = '163'; print("test sum %s : %s" % (testRow, neural.getSumCandidateUsers(testRow)))
    testRow = '331'; print("test sum %s : %s" % (testRow, neural.getSumCandidateUsers(testRow)))
    testRow = '499'; print("test sum %s : %s" % (testRow, neural.getSumCandidateUsers(testRow)))
    
    print("Revert original candidate list")
    neural.c_CandidateArr_x = org_c_CandidateArr_x
    neural.c_CandidateArr = org_c_CandidateArr
    print("candidate value x columns : %s" % neural.c_CandidateArr_x)
    print("candidate user# columns : %s" % neural.c_CandidateArr)

def main():
    neural = UserData(readFile('users.csv'))
    neural.printSampleData()
    neural.setTarget('L1547777')
    print("Target value x columns : %s" % neural.c_Target_x)
    print("Target user# columns : %s" % neural.c_Target)
    print("candidate value x columns : %s" % neural.c_CandidateArr_x)
    print("candidate user# columns : %s" % neural.c_CandidateArr)
    printUsersFromRow('163', neural)
    printUsersFromRow('331', neural)
    printUsersFromRow('499', neural)
    printUsersFromRow('164', neural)
    printUsersFromRow('332', neural)
    printUsersFromRow('500', neural)
    printUsersFromRow('165', neural)
    printUsersFromRow('333', neural)
    printUsersFromRow('501', neural)

    #After this is mixed testing of functions. Remove or move to tests.
    # testingTesting(neural) # Mixed test set

main()
