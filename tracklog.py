#!/usr/bin/env python3

import os
import sys
import pandas as pd
import csv

def addToData(args):
    # Add a new entry to the data file
    if len(args) < 6:
        print("Not enough arguments")
    else:
        addData = [args[2].upper(), args[3], args[4].title(), args[5]]
        writer = csv.writer(open("data.csv", "a"), delimiter=",")
        writer.writerow(addData)
        print("New data added")

def deleteRow(args, df):
    if len(args) < 3:
        print("no row number found")
    else:
        num = int(args[2])
        if isinstance(num, int):
            outDf = df.drop(df.index[num])
            outDf.to_csv('data.csv', sep=',', index=False)
            print("Row deleted")
        else:
            print("Row number supplied is not a whole number")
            print(str(type(args[2])))

def editRow(args, df):
    # edit a row of data
    # command: edit rowNum colName newValue
    if len(args) < 5:
        print("Not enough arguments found\n")
        print("Arguments required are:\n")
        print("edit rowNumber columnName newValue")
    else:
        rowNum = int(args[2])
        cols = ['Platform','Name','Completed','PlayTime']
        colName = args[3]
        if colName in cols:
            newVal = args[4]
            if colName == 'Platform':
                newVal = newVal.upper()
            if colName == 'Completed':
                newVal = newVal.title()
            df.at[rowNum, colName] = newVal
            df.to_csv('data.csv', sep=',', index=False)
            print("Row edited")
        else:
            print("Column name is not valid")

def printHelp():
    print('Tracklog - keep track of your gaming backlog\n')
    print('When typing commands, if the item has spaces in it then surround it in ""\n')
    print('Available commands:\n')
    print('help    Print this help page\n')
    print('add     Add a new game to your list')
    print('        add platform gameName isCompleted playtime')
    print('        add pc "The Witcher 3" no 0h00m\n')
    print('edit    Edit an existing record')
    print('        edit rowNum columnName newValue')
    print('        edit 2 Completed yes\n')
    print('delete  Delete an existing record')
    print('        delete rowNumber')
    print('        delete 3')

if __name__ == "__main__":
    inDf = pd.read_csv('data.csv')
    df = inDf.sort_values(by=['Platform', 'Name'], ascending=True)
    df = df.reset_index(drop=True)
    args = sys.argv
    if len(args) > 1:
        if args[1] == "add":
            addToData(args)
        elif args[1] == "delete":
            deleteRow(args, df)
        elif args[1] == "edit":
            editRow(args, df)
        elif args[1] == "help":
            printHelp()
        else:
            print("Input command not recognised")
            print("Showing help screen\n")
            printHelp()
    else:
       print(df)


