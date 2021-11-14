#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# TFang, 2021-Nov-12, Updated script to add dictionaries as the inner data type
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replaced list of lists with list of dicts
dictRow = {}  # list of dictionary items
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('\n[l] Load inventory from file\n[a] Add CD\n[i] Display current inventory')
    print('[d] Delete CD from inventory\n[s] Save inventory to file\n[x] Exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # TODO added functionality for loading data from file with a response if no file exists
        if objFile == None:
            print('\nNo file exists. Please add new CD(s).')
        else:
            lstTbl.clear()
            objFile = open(strFileName, 'r')
            for row in objFile:
                lstRow = row.strip().split(',')
                dictRow = {'ID': lstRow[0], 'Artist': lstRow[1], 'Title': lstRow[2]}
                lstTbl.append(dictRow)
            objFile.close()
            print(lstTbl)
            print('\nData read from file.')
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        # arranged items to read as ID, artist, then title 
        strID = input('Enter an ID: ')
        intID = int(strID)
        strArtist = input('Enter the Artist\'s Name: ')
        strTitle = input('Enter the CD\'s Title: ')
        dictRow = {'ID': intID, 'Artist': strArtist, 'Title': strTitle}
        lstTbl.append(dictRow)
        print('\nCD added to inventory.')
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, Artist, CD Title')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
        print('\nCurrent inventory displayed.')
    elif strChoice == 'd':
        # TODO added functionality to delete entry with no response for invalid IDs
        delID = input('Enter ID you wish to delete: ')
        for row in lstTbl:
            if row['ID'] == 0 or None:
                continue
        for row in lstTbl:
            if row['ID'] == delID:
                lstTbl.remove(row)
                print('\nID removed.')
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        strRow = ''
        # 'a' mode used instead of 'w' to track entries over time
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
        objFile.write(strRow)
        objFile.close()
        print('\nInventory saved to file.')
    else:
        print('Please choose either l, a, i, d, s or x!')