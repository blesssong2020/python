# class inheritance

# super class/parent class
"""
class Vehicle:

    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print("manufacture: ", self.make)
        print("color: ", self.color)
        print("model: ", self.model)

    def setTopSpeed(self, speed):
        self.topSpeed = speed


veh1 = Vehicle("VW", "red", "1")
#veh1.printDetails()


# sub class/child class
# single inheritance (one to one)
class Car(Vehicle):

    def __init__(self, make, color, model, door):
        #Vehicle.__init__(self, make, color, model)
        super().__init__(make, color, model)
        # super() no need to write self. in parameters
        self.door = door

    def printCarDetails(self):
        #Vehicle.printDetails()
        self.printDetails()
        print("door: ", self.door)

# multiple levels class
class Hybrid(Car):
    def __init__(self, make, color, model, door, gas):
        #super().__init__(make, color, model, door)
        Car.__init__(self, make, color, model, door)
        #Vehicle.__init__(self, make, color, model)
        self.gas =gas
        #self.door = door

    def turnOnHybrid(self):
        print("Hybrid is on")

    def printHybridDetails(self):
        self.printCarDetails()
        print("gas: ", self.gas)

# hierarchy class
class Truck(Vehicle):

    def __init__(self, make, color, model, engine):
        Vehicle.__init__(self, make, color, model)
        self.engine = engine

    def printTruckDetails(self):
        self.printDetails()
        print("engine: ", self.engine)
"""


"""
class Engine:
    #def __init__(self):
    #    self.power = 0
    def SetPower(self, power):
        self.power = power

class CombustionEngine(Engine):
    def SetTankCap(self, cap):
        self.cap = cap

class Electrical(Engine):
    def SetCharge(self, chargeCap):
        self.chargeCap =chargeCap

class HybridEngine(CombustionEngine, Electrical):
    def SetPower(self, power):
        print("hybride set power")
        self.power = power + "AAA"
    def printDetails(self):
        print("power: ", self.power)
        print("cap: ", self.cap)
        print("chargeCap: ", self.chargeCap)

#car1 = Car("toyota", "white", "s1", "2")
#car1.printCarDetails()

#hyb1 = Hybrid("honda", "blue", "zz", "4", "electric")
#hyb1.printHybridDetails()

#truck1 = Truck("Ford", "yellow", "xx", "v6")
#truck1.printTruckDetails()

#eng1 = Engine()
#ceng1 = CombustionEngine()
#ele1 = Electrical()
hyb2 = HybridEngine()
hyb2.SetPower("111")
hyb2.SetTankCap("14gal")
hyb2.SetCharge("14v")
hyb2.printDetails()
"""

#abstract class
class Object:
    def __init__(self):
        pass
    def printDetails(self):
        print("empty object")
        pass

class Vehicle(Object):
    def __init__(self, color, model, year):
        super().__init__()
        self.color = color
        self.model = model
        self.year = year

    def printDetails(self):
        print("color: ", self.color)
        print("model: ", self.model)
        print("year: ", self.year)

class Car(Vehicle):
    def __init__(self, color, model, year, engine):
        super().__init__( color, model, year)
        #Vehicle.__init__( color, model, year)
        self.engine = engine

    def printDetails(self):
        print("color: ", self.color)
        print("model: ", self.model)
        print("year: ", self.year)
        print("engine: ", self.engine)

def my_print(object):
    print("#"*50)
    object.printDetails()

# abstract class


cv = []
#polymorphism: Overriding is about same method, same signature but different
# classes connected through inheritance.
v1 = Vehicle("blue", "zz", "1999")
c1 = Car("red", "Rogue", "2017", "l2")
o1 = Object()
#v1.printDetails()
#print("-")
#c1.printDetails()

cv.append(v1)
cv.append(c1)
cv.append(o1)


from abc import ABC, abstractmethod
class Shape(ABC):
    #@abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def get_area(self):
        pass

    def print_sth(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def get_area(self):
        return self.length * self.length

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        return 3.14 * self.radius * self.radius
s1 = Square(2)
circle_1 = Circle(10)

print(s1.get_area())
print(circle_1.get_area())

def print_area(object):
    object.get_area()




