# Scope of Variables


def SayHello():
#    global userName

    userName = 'Steve'
    print("userName after modified = ", userName)
    
    return

userName = 'John'           # global variable

print("userName before called = ", userName)




SayHello()
print("userName after called = ", userName)   
