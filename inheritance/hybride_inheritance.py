class A:
    def methodA(self):
        print("A")

class B(A):
    def methodB(self):
        print("B")

class C(A):
    def methodC(self):
        print("C")

class D(B, C):  # Hybrid
    def methodD(self):
        print("D")

d = D()
d.methodA()  # Comes from A
