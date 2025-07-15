class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class JSONPerson(Person, JSONMixin):
    pass

p = JSONPerson("Alice", 30)
print(p.to_json()) 
