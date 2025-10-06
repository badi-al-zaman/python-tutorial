from _01_classes import Person

class Employee(Person):
    count = 0
    def __init__(self, name=None, age=None, employee_id=None, position=None, salary=None):
        Employee.count += 1
        super(Employee, self).__init__(name, age)
        self.employee_id = employee_id
        self.position = position
        self.salary = salary

    def __del__(self):
        super().__del__()
        Employee.count -= 1
        print(f"Employee object with name {self.name} is being deleted.")

    def work(self):
        return f"{self.name} is working as a {self.position}. with salary {self.salary}"

    def __str__(self):
        return f"Employee(name={self.name}, age={self.age}, employee_id={self.employee_id}, position={self.position}), salary={self.salary})"

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented # Indicate unsupported operation

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)) and scalar != 0:
            return Vector(self.x / scalar, self.y / scalar)
        return NotImplemented

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Example usage
if __name__ == "__main__":
    employee = Employee("Charlie", 28, "E123", "Developer", 70000)
    print(employee.greet())
    print(employee.work())
    print(employee)
    del employee
    v1 = Vector(2, 3)
    v2 = Vector(4, 5)
    print(v1 + v2)  # Vector addition
    print(v1 - v2)  # Vector subtraction


