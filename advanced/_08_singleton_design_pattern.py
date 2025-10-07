from abc import ABC, abstractmethod


class IPerson(ABC):

    @abstractmethod
    def get_data(self):
        """Interface method"""


class PersonSingleton(IPerson):
    __instance = None

    def __init__(self, name, age):
        if PersonSingleton.__instance is None:
            self.age = age
            self.name = name
            PersonSingleton.__instance = self
        else:
            raise Exception("This class is a singleton!")

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance is None:
            PersonSingleton("Default Name", -1)
        return PersonSingleton.__instance

    def get_data(self):
        return f"Person's name is {self.name} and age is {self.age}"


p1 = PersonSingleton("Alice", 30)
print(p1.get_data())
p2 = PersonSingleton.get_instance()
print(p2.get_data())
