import matplotlib.pyplot as plt
print "Hey"

myFile = open('RawData.txt','r')

next(myFile)
next(myFile)
myArrayX =  []
myArrayY =  []
for row in myFile: 
    row = row.split()
    print (row)
    myArrayX.append(row[4])
    myArrayY.append(row[5])
    
# print (myArrayX)
# print (myArrayY)

plt.scatter(myArrayX, myArrayY, c = "pink")
plt.show()
