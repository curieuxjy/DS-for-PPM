# if 구문

def isDiscountable(inpArg_Amount):
    if inpArg_Amount > 1000:
        rtnIsDiscountable = True
        rtnFinalPrice = inpArg_Amount - inpArg_Amount * 0.1
    else:
        rtnIsDiscountable = False
        rtnFinalPrice = inpArg_Amount
        
    return rtnIsDiscountable, rtnFinalPrice    

price = int(input("Enter Price: "))
qty = int(input("Enter Quantity: "))
amt = price * qty

[isDiscountable, amt] = isDiscountable(amt)
if isDiscountable:
    print('10% discount is applicable.')
else:
    print('10% discount is not applicable.')
    
print("Amount payable: ", amt)

