class Car:
    def __init__(self, engine, colour, brand, fuel):
        self.engine = engine
        self.colour = colour
        self.brand = brand
        self.fuel = fuel

    def getColour(self):
        print(self.colour)
    def setColour(self, newcolour):
        self.colour = newcolour
    
    def propertyys(self):
        print("My car engine is {} it is {} from {} powered by {}".format (self.engine, self.colour, self.brand, self.fuel))

class Suv(Car):
    def __init__(self, engine, colour, brand, fuel, owner, age):
        Car. __init__(self, engine, colour, brand, fuel)
        self.owner = owner
        self.age = age

    def propertyy(self):
        print("My car engine is {} it is {} from {} powered by {} owned by {} and is {} old".format (self.engine, self.colour, self.brand, self.fuel, self.owner, self.age))

#c1 - object
c1 = Suv("good engine","red","ferrari","petrol","Jaanvi", "1 year")
c1.getColour()
c1.propertyy()

