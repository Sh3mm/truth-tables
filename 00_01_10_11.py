import math

def corrected(num, top):
    raw = []
    for i in range(int((math.log(top)/math.log(2))) - int(len(num)/2)):
        raw += ["0", ";"]
    return(raw + num)

def tobin(num, top):
    output = []
    raw = (bin(num))[2:]

    for i in raw:
        output += [i] + [";"]

    return(corrected(output, top))

file = open("possibility.txt", "w")

num = input("combien de variables voulez-vous? ")
print "Loading"
num = 2**int(num)
for j in range(num):
    str1 = ''.join(tobin(j,num))
    file.write(str1 + "\n")
 
