# For Loop

mylist=[10, 20, 30, 40, 50]
for i in mylist:
    print(i)

# 1부터 10까지의 합
tmpSum = 0
for i in range(1, 11):
    tmpSum = tmpSum + i
    print(tmpSum)

# dictionary
dictVar = { 1:100, 2:200, 3:300 }
for k,v in dictVar.items():
    print("key=" + str(k) + ", value=" + str(v))
    
    