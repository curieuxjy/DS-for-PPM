# if 구문

price = int(input("Enter Price: "))
qty = int(input("Enter Quantity: "))
amt = price * qty

if amt > 1000:
    print('10% discount is applicable')
    discount = amt * 10 / 100
    amt = amt - discount

print("Amount payable: ", amt)



