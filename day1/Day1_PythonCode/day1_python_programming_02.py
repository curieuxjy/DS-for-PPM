# Basic Syntax

# 변수 Type - string, integer, float, boolean, complex number
# type(***) 함수를 이용하여 각 변수의 type을 확인한다.
#strMessage1 = 'Hello World'
#print(strMessage1)
#print(type(strMessage1))



#intNum = 1234;                  print(intNum);          print(type(intNum))
#fltNum = 1234.5678;             print(fltNum);          print(type(fltNum))
#isTrue = True;                  print(isTrue);          print(type(isTrue))
#aaa = isTrue == True

#cmpNum = 1 + 2j;                print(cmpNum);          print(type(cmpNum))



## Multiple lines - back slash (\)
#strMessage2 = 'Python is an easy to learn, powerful programming \
#               language. It has efficient high-level data structures \
#               and a simple but effective approach to object-oriented \
#               programming. Python’s elegant syntax and dynamic typing, \
#               together with its interpreted nature, make it an ideal \
#               language for scripting and rapid application development \
#               in many areas on most platforms.'
#
## 한 줄에 여러 문장을 쓸 때 - semicolon (;) 
#strMessage1 = "Hello World"; intNum = 1234; fltNum = 1234.5678
#
## 들여쓰기 (Indentation)
#j = 0
#for i in range(1, 4):
#    print('i = ', i) 
#    j = j + 1
#    print('>> j = ', j)
#   
#j = 0
#for i in range(1, 4):
#    print('i = ', i)
#    
#    j = j + 1
#print('>> j = ', j)

## 주석 처리 (comment/uncomment), ctrl + 1
#print('# Case 1')
#j = 0
#for i in range(1, 4):
#    print('i = ', i)
#    j = j + 1
#    print('>> j = ', j)
#
#'''
#print('# Case 2')    
#j = 0
#for i in range(1, 4):
#    print('i = ', i)
#    
#    j = j + 1
#print('>> j = ', j)
#'''


strText = 'HELLO'
print(strText)

print(strText[0])

for i in range(0, len(strText)):
    print(strText[i])


























