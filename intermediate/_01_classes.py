class Person:
    count = 0
    def __init__(self, name= None, age = None):
        Person.count +=1
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __del__(self):
        Person.count -=1
        print(f"Person object with name {self.name} is being deleted.")

# Example usage
if __name__ == "__main__":
    person = Person("Alice", 30)
    person.name = "Bob"
    print(person.greet())
    person2 = Person()
    print(person2.greet())
    del person2
    print(Person.count)

