# if 구문

class FinPrice:
    IsDiscountable = False
    FinalPrice = 0.0
    
def isDiscountable(inpArg_Amount):
    rtn = []
    if inpArg_Amount > 1000:
        rtn.IsDiscountable = True
        rtn.FinalPrice = inpArg_Amount - inpArg_Amount * 0.1
    else:
        rtn.IsDiscountable = False
        rtn.FinalPrice = inpArg_Amount
        
    return rtn    

price = int(input("Enter Price: "))
qty = int(input("Enter Quantity: "))
amt = price * qty

rtn = isDiscountable(amt)
if rtn.IsDiscountable:
    print('10% discount is applicable.')
else:
    print('10% discount is not applicable.')
    
print("Amount payable: ", rtn.FinalPrice)





class Sample:
  name = ''
  average = 0.0
  values = None # list cannot be initialized here!


s1 = Sample()
s1.name = "sample 1"
s1.values = []
s1.values.append(1)
s1.values.append(2)
s1.values.append(3)

s2 = Sample()
s2.name = "sample 2"
s2.values = []
s2.values.append(4)

for v in s1.values:   # prints 1,2,3 --> OK.
  print v
print "***"
for v in s2.values:   # prints 4 --> OK.
  print v
  
  