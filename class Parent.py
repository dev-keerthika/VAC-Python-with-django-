class Parent:
    def add(a, b):
        return a + b
class Child(Parent):
    def add(a, b):
        return a * b
obj1 = Parent()
print(obj1.add(2, 3))
obj2 = Child()
print(obj2.add(2, 3))