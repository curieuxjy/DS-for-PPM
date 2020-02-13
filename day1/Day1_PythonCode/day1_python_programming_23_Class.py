# Class 예제

class person:
    def __init__(self, name="Guest", age=25, energy_level=100):
        self.name = name
        self.age = age
        self.energy_level = energy_level

    def power_up(self):
        self.energy_level = self.energy_level + 5
        
    def power_down(self):
        self.energy_level = self.energy_level - 5
        
    def display_all_attributes(self):
        print('Name: ', self.name)
        print('Age: ', self.age)
        print('Power level: ', self.energy_level)
        

person1 = person()                  # instance 생성
person1.name = 'James'              # 속성(attribute) 정의

person1.display_all_attributes()    # method (action) 실행
person1.power_down()


person2 = person()                  # instance 생성
        
        
        