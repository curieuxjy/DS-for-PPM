# Dictionary vs. Set
# Dictionary
capitals = {"USA":"Washington", "France":"Paris", "India":"New Delhi"}
print(capitals.get('France'))
print(capitals.get('Paris'))

capitals['USA'] = 'Washington, D.C.'     
print(capitals.get('USA'))

del capitals['India']

for key in capitals:
    print("Key = " + key + ", Value = " + capitals[key])

print(capitals.keys())
print(capitals.values())

capitals.update({"India":"New Delhi"})
for key in capitals:
    print("Key = " + key + ", Value = " + capitals[key])


dict1 = {"Fruit":["Mango","Banana"], "Colour":["Blue", "Red"]}
print(dict1.get('Fruit'))           # ['Mango', 'Banana']
print(dict1.get('Fruit')[0])        # Mango
print(dict1.get('Fruit')[1])        # Banana

# Set
setStudent = {1, "Bill", 75.50}
print(setStudent)

setNumbers = {1, 2, 2, 3, 4, 4, 5, 5}
print(setNumbers)

a = 3 > 5

if a:
    print('True')
else:
    print('False')



























