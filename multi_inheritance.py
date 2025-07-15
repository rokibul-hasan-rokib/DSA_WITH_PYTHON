class Flying:
    def fly(self):
        print("I can fly")

class Swimming:
    def swim(self):
        print("I can swim")
        
        
class Duck(Flying, Swimming):
    def quack(self):
        print("Quack quack")
        
d = Duck()
d.fly()
d.swim()
d.quack()