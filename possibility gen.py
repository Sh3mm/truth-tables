import math

def corrected(num, top):
    raw = []
    for i in range(int(math.log2(top)) - int(len(num)/2)):
        raw += ["0", ";"]
    return(raw + num)

def toBin(num, top):
    output = []
    raw = (bin(num))[2:]

    for i in raw:
        output += [i] + [";"]

    return(corrected(output, top))

def allPossibilities (nbOfVariables):
    nbOfPossibilty = 2**int(nbOfVariables)
    arrayFinal = []

    for j in range(nbOfPossibilty):
        arrayFinal.append(toBin(j,nbOfPossibilty))

    return arrayFinal

def sumOfProducts (answersList, nbOfVariables):
    sumOfProduct = "F = "
    for answers in answersList:
        if answers[nbOfVariables] == 1:
            product = returnProduct(makeListOfX(answers, 1), nbOfVariables)
            sumOfProduct += "(" + str(product) + ")"

    return sumOfProduct

def makeListOfX (answers, Z):
    listOf1 = []
    placeInList = 0
    for x in answers[:-1]:
        if x == Z:
            listOf1.append(placeInList)
        placeInList += 1
    return listOf1

def returnProduct(listof1, nbofVariables):
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



def display ():
    #todo make shit display
    JUST_FOR_COMPILING

print (sumOfProducts([[0,0,1],[0,1,1],[1,0,1],[1,1,0]], 2))