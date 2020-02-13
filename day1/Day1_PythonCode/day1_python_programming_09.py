# By Reference

def myFunction(input_arg):
    print('Value received:',input_arg,'id:',id(input_arg))
    
    input_arg = input_arg * 10
    print('Value multipied:',input_arg,'id:',id(input_arg))
    
    return True, 0, 1


x = 10

print('Value before being passed:',x, 'id:',id(x))
myFunction(x)
print('Value after being passed:',x, 'id:',id(x))

#a = myFunction(x)
#
#a[0]