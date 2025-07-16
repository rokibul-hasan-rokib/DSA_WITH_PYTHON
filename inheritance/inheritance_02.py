class Animal: 
    def speak2(self): 
        print("Animal Speaking")

class Dog(Animal): 
   def speak1(self): 
       print("Dog Barking")
    
class Main(Dog, Animal): 
    pass

m = Main()
m.speak1()
m.speak2()