class Farmer:
    def __init__(self, crop_type, land_size):
        self.crop_type = crop_type
        self.land_size = land_size

    # Python does not support method overloading by default as shown below.
    # When we define multiple functions with the same name,
    # the later one always overrides the prior and thus,
    # in the namespace, there will always be a single entry
    # against each function name.
    def yam_farmer(self):
        print("Samuel is a", self.crop_type, "farmer \n and he cultivates it on a", self.land_size, "acre of land")

    def yam_farmer(self):
        print("Peter is a", self.crop_type, "farmer; \nand he has a small piece of land;", self.land_size, "km in size")


farming = Farmer("yam", 2)
farming.yam_farmer()


# Attempting to write two methods with the same name but
# different number of parameters of different
# data type and call the methods.
# Python still does not support this by default.
class MethodOverload(object):
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        return self.fn(*args, **kwargs)

    def key(self, *args):
        print("My name is", args)

    def key(self, *args):
        for arg in args:
            print(arg + arg + arg)


arguments = [1, 2, 3]
method = MethodOverload("Reeves")
method.key()