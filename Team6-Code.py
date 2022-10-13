import makeDictionary
def Code(txtFile):
    # opens and stores what is in the txtfile in the string "myStr"
    myTxtFile = open(txtFile)
    myStr = myTxtFile.read()

    # storing the key for the dictionary Char2Bin, because Code converts characters to binary
    myKey = makeDictionary.getCodeMap('Char2Bin')

    # for loop that iterates over each char in the string and uses the dictionary to get the coresponding binary number. Binary number is then appended to the list
    binaryList = []
    for i in myStr:
        binaryList.append(myKey.get(i))

    # converts the list into a string
    binaryStr = ''.join(binaryList)

    # for loop that calculates the bit value. iterates over each char in the string and adds it to the total sum
    myDec = 0
    for i in myStr:
        temp = str(myKey.get(i))
        myDec = str(myDec)
        myDec = bin(int(myDec,2) + int(temp,2))[2:]

    # converts the sum to integer and rounds it to base
    myDec = int(myDec,2)
    myDec = round(myDec/10)

    # converts decimal bit to string
    myDecStr = str(myDec)

    # creates the output format of D.B
    myOutput = myDecStr+"."+binaryStr

    # creates output file and writes the output in the file
    out_file = open('bin_output.txt','w+')
    out_file.write(myOutput)


# enter your file name below
Code("*INPUT_FILENAME_.txt")



