### Class: Object Oriented programming
# Attributes: last_name and first_name are attributes to class employee
"""class employee:
    def __init__(self, first_name, last_name, pay=100):
        self.last = last_name
        self.first = first_name
        self.payment = pay
        self.email = first_name + "." + last_name + "@gmail.com"

    def get_email(self):
        return self.email

    def change_email(self, new_email):
        self.email = new_email

emp1 = employee("jones", "wood")
emp2 = employee("laney", "B", 4000)
str1 = "hello w"
print(str1.__dir__())
#print(emp1.__dict__)
#print(emp2.__dir__())
print(emp1.get_email())
emp1.change_email("archer@gmail.com")
print(emp1.get_email())
"""
# variable: class variable vs instance variable
# method: instance method vs class method vs static method
"""
class employee:
    company_name = "Microsoft"
    employee_list = []

    @classmethod
    def get_company_name(cls):
        return cls.company_name

    @classmethod
    def reset_company_name(cls, name):
        cls.company_name = name

    @staticmethod
    def print(message):
        print(message)


    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name + last_name + "@gmail.com"
        self.employee_list.append(first_name+" "+last_name)
        #company_name = first_name + " " + "Amazon"

    def get_salary(self):
        return self.salary
    def set_salary(self, new_salary):
        self.salary = new_salary
tom = employee("Tom", "Wood", 20)
jack = employee("jack", "johnson", 10000)
jack.set_salary(1000000)
#print(jack.employee_list)
#print(tom.employee_list)
#print(jack.company_name)
print("1111------")
#print(jack.get_company_name())
#employee.reset_company_name("Facebook")
#print(employee.get_company_name())
employee.print("hello world")
tom.print("print tom")
"""

"""
class complex:
    def __init__(self, real=0, img=0):
        self.real = real
        self.img = img

    def get_real(self):
        return self.real

    def get_img(self):
        return self.img

    def add_op(self, c):
        self.real = c.real + self.real
        self.img = c.img + self.img

    def multiplier_(self, c):
        self.real = c.real*self.real - c.img*self.img
        self.img = c.real*self.img + c.img*self.real

c1 = complex(1.33, 99)
c2 = complex(1, 3)
#c1.add_op(c2)
c1.multiplier_(c2)
print(c1.get_img())
print(c2.get_real())
"""

"""class matrix:
    def __init__(self, data=[]):
        self.data = data

    def get_row(self, i):
        return self.data[i]

    def get_column(self, i):
        new_list = []
        for r in self.data:
            new_list.append(r[i])

        return new_list

    def add_matrix(self, c):
        m = len(self.data)
        n = len(self.data[0])
        for i in range(m):
            for j in range(n):
                self.data[i][j] += c.data[i][j]"""
"""
c1 = matrix([[1,2],[3,4],[5,6]])
c2 = matrix([[99,100],[1,1],[-3,-4]])
for i in range(3):
    print(c1.get_row(i))
print(50*"-")
c1.add_matrix(c2)
for i in range(3):
    print(c1.get_row(i))

#if __name__ == '__main__':

"""


# Access Control

class employee_2:
    company_name = "Amazon"

    def __init__(self, salary, name):
        self.salary = salary
        self.name = name

    def display_name(self):
        print(self.name)

    def name2(self):
        print(self.name)

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name


emp1 = employee_2(10000, "Jack")
emp3 = employee_2(8888, "Jenny")
print(emp1.company_name)
emp1.change_company_name("FB")
print(employee_2.company_name)
emp2 = employee_2(999, "Tom")
print(emp2.company_name)
print(emp3.company_name)
