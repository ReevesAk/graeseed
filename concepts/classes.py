# Program class for default constructors
class TechClass:
    # Default constructor.
    def __int__(self):
        self.num = 100

    def __init__(self, height):
        self.height = height

    def __init__(self, stack, users):
        # initializing instance variable
        self.stack = stack
        self.users = users

    def tech_class(self):
        # Python does not explicitly support multiple class constructors.
        # Although classes methods could be called from __init__ using
        # one constructor.
        # print("There are more than", self.num, "self taught developers in Nigeria")
        print("His stack is", self.stack, "and his name is", self.users)
        # print("The height of the Nephilims was over", self.height, "meters high")


# Applying private, protected, public and default
# access modifiers to constructors
class AccessModifiersClass:
    def __int__(self):
        pass

    # A default constructor
    def __init__(self):
        self._boy = "boy"

    # Private access modifier in constructor
    def __init__(self, boy, girl, woman):
        self.__boy = boy
        self.__girl = girl
        self.__woman = woman

    # Public access modifier in constructor
    def __init__(self, man, animal):
        self.man = man
        self.animal = animal


# The above constructors of code in the AccessModifiersClass
# cannot be called because python des nt support it.


# A simple class to demonstrate the concept of constructor attributes.
class Developer:
    def __init__(self, name, stack, yearsOfExp):
        self.name = name
        self.id = stack
        self.age = yearsOfExp


# Creates the object of the class Developer.
s = Developer("John", "Python", 3)

# Prints the attribute name of the object s
print(getattr(s, 'name'))

# Reset the value of attribute yearsOfExp to 4
setattr(s, "yearsOfExp", 4)

# Prints the modified value of years of experience.
print(getattr(s, 'yearsOfExp'))

# Prints true if the Developer contains the attribute with name python.
print(hasattr(s, 'Python'))

# Deletes the attribute yearsOfExp.
delattr(s, 'yearsOfExp')

# This will give an error since the attribute yearsOfExp has been deleted.
print(s.age)


class MainClass:

    def main_class(self):
        techie = TechClass("Backend", "Reeves")
        techie.tech_class()


class Student:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

        # creates the object of the class Student


s = Student("Reeves", 101, 22)

# prints the attribute name of the object s
print(getattr(s, 'name'))

# reset the value of attribute age to 23
setattr(s, "age", 23)

# prints the modified value of age
print(getattr(s, 'age'))

# prints true if the student contains the attribute with name id

print(hasattr(s, 'id'))
# deletes the attribute age
delattr(s, 'age')

# This returns an error since the attribute age has been deleted.
print(s.yearsOfExp)

if __name__ == "__main__":
    call = MainClass()
    call.main_class()