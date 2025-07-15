class A:
    def do_something(self):
        print("A")

class B(A):
    def do_something(self):
        print("B")
        super().do_something()

class C(B):
    def do_something(self):
        print("C")
        super().do_something()

c = C()
c.do_something()