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

def BinaryToGray(truthTable, nbOfVariable):
    """turns a binary truth table into a code gray one
    accepts a binary truth table and a number of variable to return a Gray table"""
    Table_Gray = truthTable
    for i in range(1,nbOfVariable):
        compteur = 0

        for j in range(0,len(Table_Gray),2**i):
            transitory = Table_Gray[(j-2**i)+2**i:j+(2)**i]

            if (compteur % 2 == 1):
                Table_Gray[(j-2**i)+2**i:j+(2)**i] = transitory[::-1]
            compteur += 1

    return(Table_Gray)

def display ():
    #todo make shit display
    JUST_FOR_COMPILING

TABLE_DE_VERITE = [
    [0,0,0,0],
    [0,0,1,1],
    [0,1,0,1],
    [0,1,1,1],
    [1,0,0,0],
    [1,0,1,0],
    [1,1,0,1],
    [1,1,1,0]]

TABLE_DE_VERITE2 = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,1]]

print ("le produit de somme est: " + str(BinaryToGray(TABLE_DE_VERITE, 3)))
print ("la somme de produit est: " + str(BinaryToGray(TABLE_DE_VERITE2, 2)))