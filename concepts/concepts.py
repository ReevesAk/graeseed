"""
    This code section covers an overview of what I have learnt 
    about access_modifiers in python.
"""

# Creating a parent class with private fields.
class Employee:
    # Initializing private fields.
    def __init__(self, name, pay, company):
        self.__name = name
        self.__pay = pay
        self.__company = company

    def __access(self):
        # Accessing a private data members.
        print(self.__name + " is my name")
        print("I work for " + self.__company)
        print("I am paid", self.__pay, "naira monthly")

    def main(self):
        # Accessing private member method.
        self.__access()


class Engineer(Employee):
    def subclass(self, name, pay, company):
        super().__init__(name, pay, company)
        self.__main()


# Creating  parent class of protected fields.
class AccessProtected:
    # Initializing protected fields.
    def __init__(self, name, pay, company):
        self._name = name
        self._pay = pay
        self._company = company

    def _access_protected(self):
        # Accessing a protected data members.
        print(self._name + " is my name")
        print("I work for " + self._company)
        print("I am paid", self._pay, "naira monthly")

    def call_protected(self):
        # Accessing private member method.
        self._access_protected()


# Creating a parent class with publix fields.
class Worker:
    # Initializing public fields.
    def __init__(self, name, pay, company):
        self.name = name
        self.pay = pay
        self.company = company

    def access_worker(self):
        # Accessing a public data members/fields.
        print(self.name + " is my name")
        print("I work for " + self.company)
        print("I am paid", self.pay, "naira monthly")


class AccessWorker:
    def call_public(self):
        # Calling public member method in the same package.
        worker = Worker("Skippy", 12, "Vete")
        worker.access_worker()


if __name__ == '__main__':
    class_modifier = Employee("Reeves", 10, "graeseed Technologies")
    class_modifier.main()

    access = AccessWorker()
    access.call_public()

    # Attempting to call a private method from
    # another subclass. This is protected methods
    # are only called by subclasses of the parent
    # class of protected members. 
    # It throws this error: AttributeError: 'Engineer' object has no attribute '_Engineer__main'.
    protected_members = AccessProtected("Reeves", 10, "graeseed")
    protected_members.call_protected()

    # Attempting to call a private method from
    # a subclass fails. This is because subclasses
    # are only able to call protected and public 
    # method of parent class.
    # It throws this error: AttributeError: 'Engineer' object has no attribute '_Engineer__main'.
    subclass_obj = Engineer("Victor", 1000, "Raedahgroup")
    subclass_obj.subclass("Victor", 1000, "Raedahgroup")

