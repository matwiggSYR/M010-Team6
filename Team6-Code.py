import makeDictionary
def Code(txtFile):
    myTxtFile = open(txtFile)
    myStr = myTxtFile.read()
    myKey = makeDictionary.getCodeMap('Char2Bin')
    binaryList = []
    for i in myStr:
        binaryList.append(myKey.get(i))
    binaryStr = ''.join(binaryList)
    myDec = 0
    for i in myStr:
        temp = str(myKey.get(i))
        myDec = str(myDec)
        myDec = bin(int(myDec,2) + int(temp,2))[2:]
    myDec = int(myDec,2)
    myDec = round(myDec/10)
    myDecStr = str(myDec)
    myOutput = myDecStr+"."+binaryStr
    out_file = open('bin_output.txt','w+')
    out_file.write(myOutput)
    print("word:",myStr)
    print("Decimal val:", myDecStr)
    print("Binary val:", binaryStr)
    print(myOutput)
#enter your file name below
Code("*INPUT_FILENAME_.txt")



