import math

def corrected(num, top):
    """adds 0s in front of your binary number to make it a cenrtain lenght
    accepts a binary number in a list and a lenghts to return a list """
    raw = []
    for i in range(int(math.log2(top)) - int(len(num)/2)):
        raw += ["0", ";"]
    return(raw + num)

def toBin(num, top):
    """transforms a exadecimal number to its binary conterpart.
    accepts a number and a lenght to returns a list"""
    output = []
    raw = (bin(num))[2:]

    for i in raw:
        output += [i] + [";"]

    return(corrected(output, top))

def allPossibilities (nbOfVariables):
    """makes a list of all the binary possibilities of a certain number of variables (2^x)
    accepts a number of variables to return a list"""
    nbOfPossibilty = 2**int(nbOfVariables)
    arrayFinal = []

    for j in range(nbOfPossibilty):
        arrayFinal.append(toBin(j,nbOfPossibilty))

    return arrayFinal

def makeListOfX (answers, Z):
    """makes a list of the positions of a numbers in a list
    accept a list and a number to return a list"""
    listOf = []
    placeInList = 0
    for x in answers[:-1]:
        if x == Z:
            listOf.append(placeInList)
        placeInList += 1
    return listOf

def sumOfProducts (answersList, nbOfVariables):
    """makes a sum of products of the truth table given to it
    accepts a truth table and a number of varriables to return a string"""
    sumOfProduct = "F = "
    for answers in answersList:
        if answers[nbOfVariables] == 0:
            product = returnProduct(makeListOfX(answers, 0), nbOfVariables)
            sumOfProduct += "(" + str(product) + ")"

    return sumOfProduct

def returnProduct(listof1, nbofVariables):
    """makes the product part of the sum of product with the positions of the 0s
    accepts a list and a number of varriables to return a string"""
    product = ""
    for i in range(nbofVariables):
        check = False
        for j in listof1:
            if i == j:
                check = True
                break
        if check == True:
            product += str(chr(65+i))
        else:
            product += str(chr(65 + i)) + "'"
        if i != (nbofVariables-1):
            product += "+"

    return product

def ProductOfSums (answersList, nbOfVariables):
    """makes a product of sums of the truth table given to it
    accepts a truth table and a number of varriables to return a string"""
    productOfSum = "F = "
    for answers in answersList:
        if answers[nbOfVariables] == 1:
            sum = returnSum(makeListOfX(answers, 1), nbOfVariables)
            if productOfSum != "F = ":
                productOfSum += "+"
            productOfSum += "(" + str(sum) + ")"


    return productOfSum

def returnSum(listof1, nbofVariables):
    """makes the sun part of the product of sums with the positions of the 1s
        accepts a list and a number of varriables to return a string"""
    Sum = ""
    for i in range(nbofVariables):
        check = False
        for j in listof1:
            if i == j:
                check = True
                break
        if check == True:
            Sum += str(chr(65 + i))
        else:
            Sum += str(chr(65 + i)) + "'"

    return Sum

def binaryToGray(truthTable, nbOfVariable):
    """turns a binary truth table into a code gray one
    accepts a binary truth table and a number of variable to return a Gray table"""
    Table_Gray = truthTable[:]
    for i in range(1,nbOfVariable):
        compteur = 0

        for j in range(0,len(Table_Gray),2**i):
            transitory = Table_Gray[(j-2**i)+2**i:j+(2)**i]

            if (compteur % 2 == 1):
                Table_Gray[(j-2**i)+2**i:j+(2)**i] = transitory[::-1]
            compteur += 1

    return(Table_Gray)

def grayToKarnaugh(grayTable, nbOfVariable):
    """turns a gray Truth table into a karnaugh table
    accepts a gray table and a number of variable to return a karnaugh table"""
    nbposPerLine = 2**(int(nbOfVariable/2)+ nbOfVariable%2)
    nbLines = 2**int(nbOfVariable/2)

    karnaugh = [ [0]*nbposPerLine for _ in range(nbLines)]

    for i in range(nbLines):
        for j in range(nbposPerLine):
            karnaugh[i][j] = grayTable[i*nbposPerLine + j][nbOfVariable]
    return karnaughCorrected(karnaugh,nbLines)

def karnaughCorrected(rawKarnaughTable, nbOfLines):
    """corrects the raw Karnaugh Table
    accepts a raw Karnaugh Table and a nb of lines to return a corrected Karnaugh Table"""
    cTableKarnaugh = rawKarnaughTable[:]
    for i in range(nbOfLines):
        if i%2 == 1:
            cTableKarnaugh[i] = rawKarnaughTable[i][::-1]
    return cTableKarnaugh

def getGroupsKarnaugh(karnaughTable, nbOfVariables):
    used = []
    groups = []
    for i in range(len(karnaughTable)):
        for j in range(len(karnaughTable[i])):
            if (karnaughTable[i][j] == 1) and (isInUse(i,j, used) == False):
                group = groupsofKarnaugh(karnaughTable, [i, j], [i, j])
                updateUsed(used, group, karnaughTable)
                groups.append(group)
    return (groups)

def isInUse(i,j, used):
    if used == []:
        return False
    for coordo in used:
        if (i == coordo[0]) and (j == coordo[1]):
            return True
    return False

def updateUsed(used, new, table):
    for i in range(new[0][0], new[1][0]+1):
        for j in range(new[0][1], new [1][1]+1):
            used.append(correctedTile([i, j], table))
    return used

def groupsofKarnaugh(karnaughTable, start, end):
    hight = abs(end[0] - start[0]) + 1
    lenght = abs(end[1] - start[1]) + 1

    if areX("H", hight, karnaughTable, start, end, 1):
        end[0] += hight
        groupsofKarnaugh(karnaughTable, start, end)

    elif areX("L", lenght, karnaughTable, start, end, 1):
        end[1] += lenght
        groupsofKarnaugh(karnaughTable, start, end)

#    if areX("-H", -hight, karnaughTable, start, end, 1):
#        start[0] -= hight
#        groupsofKarnaugh(karnaughTable, start, end)

    elif areX("-L", -lenght, karnaughTable, start, end, 1):
        start[1] -= lenght
        groupsofKarnaugh(karnaughTable, start, end)

    return [start, end]

def areX(side,lenght, karnaughTable, start, end, x):
    if side == "L":
        possibleEnd = [end[0],end[1]+lenght]
        possibleStart = start[:]
    if side == "H":
        possibleEnd = [end[0] + lenght, end[1]]
        possibleStart = start[:]
    if side == "-L":
        possibleStart = [start[0] , start[1]+ lenght]
        possibleEnd = end[:]
    if side == "-H":
        possibleStart = [start[0] + lenght, start[1]]
        possibleEnd = end[:]

    try:
        if possibleStart[0] > possibleEnd [0]:
            smallestHight = possibleEnd[0]
            bigestHight = possibleStart[0]
        else:
            smallestHight = possibleStart[0]
            bigestHight = possibleEnd[0]
        if possibleStart[1] > possibleEnd [1]:
            smallestLenght = possibleEnd[1]
            bigestLenght = possibleStart[1]
        else:
            smallestLenght = possibleStart[1]
            bigestLenght = possibleEnd[1]

        for i in range(smallestHight, bigestHight+1):
            for j in range(smallestLenght, bigestLenght+1):
                if karnaughTable[i][j] != x:
                    return False
    except IndexError:
        return False
    return True

def correctedTile(tile, karnaughTable):
    if tile[0] < 0:
        tile[0] += len(karnaughTable)
    if tile[1] < 0:
        tile[1] += len(karnaughTable[0])
    return tile

def SoPKarnaugh(listOfGroups):
    for group in listOfGroups:
        begin = group[0]
        end = group[1]
        if begin[0] > end[0]:
            smallestHight = end[0]
            bigestHight = begin[0]
        else:
            smallestHight = begin[0]
            bigestHight = end[0]
        if begin[1] > end [1]:
            smallestLenght = end[1]
            bigestLenght = begin[1]
        else:
            smallestLenght = begin[1]
            bigestLenght = end[1]

        for i in range(smallestHight, bigestHight):
            for j in range(smallestLenght, bigestLenght):
                product = "(" + char(65+graytodec)

def display ():
    #todo make shit display
    JUST_FOR_COMPILING

TABLE_DE_VERITE = [
    [0,0,0,1],
    [0,0,1,0],
    [0,1,0,1],
    [0,1,1,0],
    [1,0,0,1],
    [1,0,1,0],
    [1,1,0,1],
    [1,1,1,0]]

TABLE_DE_VERITE2 = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,1]]

x = binaryToGray(TABLE_DE_VERITE,3)
for a in x:
    print (a)
print ("")

y = grayToKarnaugh(x,3)

for a in y:
    print (a)
print ("")

z = getGroupsKarnaugh(y,3)
print (z)