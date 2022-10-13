import makeDictionary
def Decode(txtFile):
    myTxtFile = open(txtFile)
    inputBin = myTxtFile.read()
    myKey = makeDictionary.getCodeMap('bin2char')
    binList = inputBin.split('.')
    inputBin = binList[1]
    print("bin:",inputBin)
    myDecode = ""
    lastIndex = 0
    for i in range(len(inputBin)):
        i = i + lastIndex
        if i >= len(inputBin):
            break
        if inputBin[i].startswith("1"):
            myDecode = myDecode + str(myKey.get(inputBin[i: (i + 7)]))
            lastIndex = 6 + lastIndex
        elif inputBin[i].startswith("0"):
            myDecode = myDecode + str(myKey.get(inputBin[i: (i + 5)]))
            lastIndex = 4 + lastIndex
    print("myDecode:",myDecode)
    out_file = open('TextOutput.txt', 'w+')
    out_file.write(myDecode)


Decode("bin_output.txt")
