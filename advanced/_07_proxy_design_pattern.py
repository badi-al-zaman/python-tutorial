from abc import ABC, abstractmethod


class IPerson(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def person_method(self):
        """Interface method"""


class Student(IPerson):
    def __init__(self, name):
        self.name = name

    def person_method(self):
        print(f"I am a student and my name is {self.name}")


class StudentProxy(IPerson):
    def __init__(self, name):
        self.student = Student(name)

    def person_method(self):
        print("Proxy: Logging access to student method. pre conditions")
        self.student.person_method()


s1 = StudentProxy("John")
s1.person_method()
