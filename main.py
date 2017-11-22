import possibility_gen as poss

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

x = poss.binaryToGray(TABLE_DE_VERITE,3)
for a in x:
    print (a)
print ("")

y = poss.grayToKarnaugh(x,3)

lenght = poss.genSideBar(y[0])
hight = poss.genSideBar(y)
print (lenght)
print (hight)
print ("")

for i in range(len(y)):
    print (y[i])
print ("")

z = poss.getGroupsKarnaugh(y,3)
print (z)

print (poss.letters(hight,z[0],poss.HIGHT))
print (poss.letters(lenght,z[0],poss.LENGHT))

print ("")
print(poss.karnaughProduct(y, z[0]))