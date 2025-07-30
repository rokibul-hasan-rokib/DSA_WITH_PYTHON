class Rokib:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        for child in self.children:
            print(f"  Child Name: {child.name}, Age: {child.age}")


# Example usage
rokib = Rokib("Rokib", 40)
child1 = Rokib("Child 1", 10)