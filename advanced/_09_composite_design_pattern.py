from abc import ABC, abstractmethod


class IDepartment(ABC):
    def __init__(self, employees):
        pass

    @abstractmethod
    def print_department_info(self):
        """Interface method"""


class AccountingDepartment(IDepartment):
    def __init__(self, employees):
        self.employees = employees

    def print_department_info(self):
        print(f"Accounting Department Employees: {self.employees}")


class DevelopmentDepartment(IDepartment):
    def __init__(self, employees):
        self.employees = employees

    def print_department_info(self):
        print(f"Development Department Employees: {self.employees}")


class ParentDepartment(IDepartment):
    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.departments = []

    def add_department(self, department: IDepartment):
        self.departments.append(department)
        self.employees += department.employees

    def print_department_info(self):
        print(f"Parent Department Employees: {self.base_employees}")
        for department in self.departments:
            department.print_department_info()
        print(f"Total Employees in Parent Department: {self.employees}")


d1 = AccountingDepartment(10)
d2 = DevelopmentDepartment(25)
parent_department = ParentDepartment(5)
parent_department.add_department(d1)
parent_department.add_department(d2)
parent_department.print_department_info()
