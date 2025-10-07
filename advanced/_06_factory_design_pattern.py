from abc import ABCMeta, abstractmethod


class IPerson(metaclass=ABCMeta):
    @abstractmethod
    def person_method(self):
        """Interface method"""


class Student(IPerson):
    def person_method(self):
        print("I am a student")


class Teacher(IPerson):
    def person_method(self):
        print("I am a teacher")


class PersonFactory:
    @staticmethod
    def build_person(person_type: str) -> IPerson:
        if person_type == "student":
            return Student()
        elif person_type == "teacher":
            return Teacher()
        else:
            raise ValueError(f"Unknown person type: {person_type}")


if __name__ == "__main__":
    # build person based on user input at runtime we used factory design pattern
    student = PersonFactory.build_person(
        input("Enter person type (student/teacher): ").strip()
    )
    student.person_method()  # Output: I am a student

    teacher = PersonFactory.build_person("teacher")
    teacher.person_method()  # Output: I am a teacher
