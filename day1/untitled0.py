# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 10:05:49 2020

@author: LG
"""

str_message1 = "Hello World";   print(str_message1);    print(type(str_message1));
int_num = 1234;                 print(int_num);         print(type(int_num));
flt_num = 1234.5678;            print(flt_num);         print(type(flt_num));
is_true = True;                 print(is_true);         print(type(is_true));
cmp_num = 1 + 2j;               print(cmp_num);         print(type(cmp_num));

# 여러줄 공백없이 다음 줄로 예쁘게 indentation을 어떻게 넣지?
str_message2 = 'well..'

j = 0
for i in range(1,4):
  print('i = ', j)
  j += 1
  print('>> j = ', j)

# 여러줄 주석 처리는 ctrl + 숫자 1
#j = 0
#for i in range(1,4):
#  print('i = ', j)
#  j += 1
#  print('>> j = ', j)

'''
j = 0
for i in range(1,4):
  print('i = ', j)
  j += 1
  print('>> j = ', j)
'''
str_text = 'HELLO'
print(str_text)
print(str_text[1])

for i in range(len(str_text)):
  print(i)
  print(str_text[i])
  
# string -> array
lst_number = [1, 2, 3, 4]
print(lst_number)
print(type(lst_number))
lst_number[1] = lst_number[1] * 10
print(lst_number)

# numpy array를 많이 쓸것이지만 일단은 python 기본 자료형들 익히기
capitals = {'USA': 'Washington', 'France':'Paris', 'India':'New Delhi'}
print(capitals.get('France'))

capitals['USA'] = 'Washington D.C.'
del capitals['India']

# oh! 이건 몰랐네!! 대박 dictionary에서 유용할 듯
for key in capitals:
  print("Key = " + key + ", Value = " + capitals[key])

print(capitals.keys())
print(capitals.values())

capitals.update({'India':'New Delhi'})

set_num = {1, 2, 2, 3, 4, 4, 5, 5}
print(set_num)

# operator
if (3>4) != True:
  print('true')
  
a = 3>5
if a: # a=True
  print('True')
else:
  print('False')

# if
price = int(input("Enter Price: ")) #string을 integer로
qty = int(input("Enter Quantity: "))
amt = price * qty

if amt>1000:
  print('10% discount is applicable')
  discount = amt*10 / 100
  amt -= discount
print("Amount payable: ", amt)

# function
def is_discountable(inp_arg_amount):
  # global 선언해서 함수 안의 변수를 빼올 수 있긴 하다 !!return이 아닌 변수를!!
  if inp_arg_amount > 1000:
    rtn_discountable = True
    rtn_final_price = inp_arg_amount - inp_arg_amount*0.1
  else:
    rtn_discountable = False
    rtn_final_price = inp_arg_amount
  return rtn_discountable, rtn_final_price

[is_discountable, amt] = is_discountable(amt)
if is_discountable:
  print('10% discount is applicable.')
else:
  print('10% discount is not applicable.')
  
print('Amount payable: ', amt)

# while
num = 0
count = 0
sum = 0

while num >= 0:
  num = int(input("give me a number: "))
  
  if num >= 0:
    count += 1
    sum += num
    
    if count > 10:
      break
avg = sum/count
print("numbers input: ", count, "average: ", avg)

# 가독성 vs  효율성
###############################################################






















