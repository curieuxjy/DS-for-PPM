# While Loop

num = 0
count = 0
sum = 0

while num >= 0:
    num=int(input("enter any number .. -1 to exit\n"))
    
    if num >= 0:
#        count = count + 1 #this counts number of inputs 
        count += 1
        sum = sum + num # this adds input number cumulatively. 
        
        if count > 10:
            break            
        
avg = sum / count
print ("numbers input:",count, "average:",avg)

