class Person:
    """_summary_"""

    def __init__(self, name, age):
        self.name = name  # Public attribute
        self._age = age  # Protected attribute Still accessible, but considered “don’t touch unless you know what you’re doing.”
        self.__ssn = "123-45-6789"  # Private attribute This makes it harder (but not impossible) to access from outside

    @property
    def Ssn(self):
        return self.__ssn

    @Ssn.setter
    def set_ssn(self, ssn):
        self.__ssn = ssn

    @staticmethod
    def info():
        return "This is a Person class"


p1 = Person("Alice", 30)
print(p1.name)  # Accessing public attribute
print(p1._age)  # Accessing protected attribute (not recommended)
print(p1.Ssn)  # Accessing private attribute via getter

print(
    p1._Person__ssn
)  # Accessing private attribute via name mangling (not recommended)

p1.set_ssn = "987-65-4321"  # Modifying private attribute via setter
print(p1.Ssn)
# print(p1.__ssn)  # This will raise an AttributeError

print(Person.info())  # Calling static method
print(p1.info())  # Calling static method via instance (not recommended)
