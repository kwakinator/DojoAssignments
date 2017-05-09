class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.display_all()

    def tax(self):
        if self.price > 10000:
            tax = .15
        else:
            tax = .12
        print "Tax: {}".format(tax)
        return self

    def display_all(self):
        print "Price: {}".format(self.price)
        print "Speed: {} mph".format(self.speed)
        print "Fuel: {}".format(self.fuel)
        print "Mileage: {} mpg".format(self.mileage)
        self.tax()

car1= Car(20000, 35, "Full", 35)
car2= Car(15000, 62, "Kind of Full", 36549)
car3= Car(58220, 35, "Full", 105)
car4= Car(68221, 78, "Not Full", 56478)
car5= Car(1000, 215, "Empty", 90210)
car6= Car(5000, 95, "Kind of Full", 8675)
