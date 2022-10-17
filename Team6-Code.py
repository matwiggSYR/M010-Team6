import xlrd
def Code(txtFile):
    # Opens and stores what is in the txtfile in the string "myStr"
    myTxtFile = open(txtFile)
    myStr = myTxtFile.read()

    # Creating and storing the key for the dictionary Char2Bin, because Code converts characters to binary
    wb = xlrd.open_workbook('Team6-Table.xls')
    sh = wb.sheet_by_index(0)
    Char2Bin = {}
    for i in range(2,18):
        char = sh.cell(i, 0).value
        binVal = sh.cell(i, 1).value


        # Add the binary value and character to the dictionary.
        Char2Bin[char] = binVal

    for i in range(2,59):
        char = sh.cell(i, 5).value
        binVal = sh.cell(i, 6).value

        Char2Bin[char] = binVal


    myKey = Char2Bin

    # for loop that iterates over each char in the string and uses the dictionary to get the coresponding binary number. Binary number is then appended to the list
    binaryList = []
    for i in myStr:
        binaryList.append(myKey.get(i))

    # converts the list into a string
    binaryStr = ''.join(binaryList)


    # for loop that calculates the bit value. iterates over each binary number and tallies the shorts and longs
    # converts the sum to integer and rounds it to base
    lastIndex = 0
    numShorts = 0
    numLongs = 0
    for i in range(len(binaryStr)):
        i = i + lastIndex
        if i >= len(binaryStr):
            break
        if binaryStr[i].startswith("1"):
            numLongs = numLongs + 1
            lastIndex = 6 + lastIndex
        elif binaryStr[i].startswith("0"):
            numShorts = numShorts + 1
            lastIndex = 4 + lastIndex
    # calculates the bit value
    myDec = (numLongs*7) + (numShorts*5)

   #rounds the bit value
    myDec = str(myDec)
    if len(myDec) > 2:
        if int(myDec[2]) > 5:
            temp = int(myDec[1]) + 1
            myDec = myDec[:1] + str(temp)
        myDec = myDec[:2]
    myDecStr = str(myDec)

    # creates the output format of D.B
    myOutput = myDecStr+"."+binaryStr

    # creates output file and writes the output in the file
    out_file = open('bin_output.txt','w+')
    out_file.write(myOutput)


# enter your file name below
Code("allChars.txt")



