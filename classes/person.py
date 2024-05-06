class Person:
    def __init__(self, name, age, gender):
        self.name =name
        self.age = age
        self.gender = gender
    def introduce(self):
        print(f"Hi, my name is {self.name}.I am {self.age} years old and am {self.gender}.")  
  #creating an instance of the person      
person1 = Person ("John", 30, "male")
#calling the introduce method
person1.introduce()        
          