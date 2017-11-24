import possibility_gen as poss
from math import log2
N_DE_VARRIABLE = 4
TABLE_DE_VERITE = [
    [0,0,0,0,1],
    [0,0,0,1,0],
    [0,0,1,0,1],
    [0,0,1,1,0],
    [0,1,0,0,1],
    [0,1,0,1,0],
    [0,1,1,0,1],
    [0,1,1,1,0],
    [1,0,0,0,1],
    [1,0,0,1,1],
    [1,0,1,0,1],
    [1,0,1,1,1],
    [1,1,0,0,1],
    [1,1,0,1,0],
    [1,1,1,0,0],
    [1,1,1,1,0]
]

TABLE_DE_VERITE2 = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,1]]

x = poss.binaryToGray(TABLE_DE_VERITE,N_DE_VARRIABLE)
for a in x:
    print (a)
print ("")

y = poss.grayToKarnaugh(x,N_DE_VARRIABLE)

lenght = poss.genSideBar(y[0])
hight = poss.genSideBar(y)
print (lenght)
print (hight)
print ("")

for i in range(len(y)):
    print (y[i])
print ("")

z = poss.getGroupsKarnaugh(y,N_DE_VARRIABLE,1)
x2 = poss.getGroupsKarnaugh(y,N_DE_VARRIABLE,0)
print (z)
print (x2)


print ("")
print(poss.karnaughSumOfProduct(y,z))
print(poss.karnaughProductOfSum(y,x2))
