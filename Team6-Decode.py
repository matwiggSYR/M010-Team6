import xlrd
def Decode(txtFile):
    # opens and stores what is in the bin_output.txt file in the string "inputBin"
    myTxtFile = open(txtFile)
    inputBin = myTxtFile.read()

    # storing the key for the dictionary Char2Bin, because Code converts binary to characters
    wb = xlrd.open_workbook('Team6-Table.xls')
    sh = wb.sheet_by_index(0)
    Bin2Char = {}
    for i in range(2,18):
        char = sh.cell(i, 0).value
        binVal = sh.cell(i, 1).value

        # Add the binary value and character to the dictionary.
        Bin2Char[binVal] = char

    for i in range(2,59):
        char = sh.cell(i, 5).value
        binVal = sh.cell(i, 6).value


        Bin2Char[binVal] = char

    myKey = Bin2Char


    # converts the input string into a list and then splits the decimal value from the binary value
    binList = inputBin.split('.')

    # stores the decimal value in inputBin
    inputBin = binList[1]

    # for loop that iterates over binary numbers and uses the dictionary to convert it to the corresponding character
    # uses 0 and 1 as flags to see if the binary number is a short or long
    # stores the characters in myDecode
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

    # creates output file and writes the decoded word in the file
    out_file = open('TextOutput.txt', 'w+')
    out_file.write(myDecode)


Decode("bin_output.txt")
