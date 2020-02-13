# Variable Type

# Sequence Type: 1) String, 2) List, 3) Tuple
strName1 = 'James'
strName2 = "James"

print('strName1 = ', strName1);     print(type(strName1))
print('strName2 = ', strName2);     print(type(strName2))

strName_1st = strName1[0];          print(strName_1st)
strName_2nd = strName1[1];          print(strName_2nd)
strName_3rd = strName1[2];          print(strName_3rd)
strName_4th = strName1[3];          print(strName_4th)
strName_5th = strName1[4];          print(strName_5th)

strName3 = strName1[0] + strName1[1] + strName1[2] + strName1[3] + strName1[4]
print(strName3)

# List [] vs. Tuple ()
lstNumber = [1, 2, 3, 4, 5]
print(type(lstNumber))
print('The first element of ''lstNumber'' is ' + str(lstNumber[0]))

lstString = ['abc', 'def', 'ghi', 'jkl', 'mno']
print(type(lstString))
print(lstString[1])
print(lstString[2][2]) 

tplNumber = (1, 2, 3, 4, 5)
print(type(tplNumber))
print('The second element of ''tplNumber'' is ' + str(tplNumber[1]))

tplString = ('abc', 'def', 'ghi', 'jkl', 'mno')
print(type(tplString))
print(tplString[1])
print(tplString[2][2])

lstNumber[1] = lstNumber[1] * 10;       print(lstNumber)
tplNumber[1] = tplNumber[1] * 10;       print(tplNumber)
