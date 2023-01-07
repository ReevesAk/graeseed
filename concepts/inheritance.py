"""
    This code section covers an overview of what I have learnt 
    about Inheritance in python.
"""   

class A():
    '''Parent class'''

    def __init__(self):
        self.firstname = "Reeves"
        self.lastname = "Akwa"
        self.age = 27

    def first_name(self):
        print("Hi, my name is:" + self.firstname)

    def last_name(self):
        print("Hi, my surname is:", self.lastname)

    def get_age(self):
        print("I am", self.age, "years old")


class B(A):
    '''First filial child class'''

    def __init__(self):
        super().__init__()
        self.color = "Dark"
        self.weight = 140

        # Calling overriden parent class method.
        A.get_age(self)
        print("I am", self.age + 10, "years old")

    def col(self):
        print("Wisdom is " + self.color, " in complexion")

    def get_size(self):
        print("MY size in weight is:", self.weight, "lbs")


class C(B):
    '''First filial child class'''

    def __init__(self):
        super().__init__()
        self.height = 20
        self.stack = "Python"

        # Calling overriden parent class method.
        A.get_age(self)
        print("I am", self.age + 20, "years old")

    def get_stack(self):
        print("I am a " + self.stack, "developer")

    def get_height(self):
        print("I am ", self.height, "feet tall")


# Implementing polymorphism in inheritance.
class Example:
    def main(self):
        parent_class_object = A()
        parent_class_object.first_name()
        parent_class_object.last_name()
        parent_class_object.get_age()
        first_subclass_element = B()
        first_subclass_element.get_age()
        first_subclass_element.col()
        first_subclass_element.get_size()
        sec_subclass_element = C()
        sec_subclass_element.get_age()
        sec_subclass_element.get_stack()
        sec_subclass_element.get_height()


if __name__ == '__main__':
    read_all_classes = Example()
    read_all_classes.main()