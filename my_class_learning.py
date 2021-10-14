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

class matrix:
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
                self.data[i][j] += c.data[i][j]
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
