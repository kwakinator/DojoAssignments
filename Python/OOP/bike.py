class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print "The specs on this bike are: ${}, {} mph, {} total miles.".format(self.price, self.max_speed, self.miles)
        return self
    def ride(self):
        self.miles +=10
        print "Riding..."
        return self
    def reverse(self):
        if self.miles > 0:
            self.miles -=5
            print "Reversing.."
        else:
            print "Cannot go negative!"
        return self
bike1= Bike(200, 25)
bike1.ride().ride().ride().reverse().displayInfo()
bike1.ride().ride().reverse().reverse().displayInfo()
bike1.reverse().reverse().reverse().displayInfo()


bike2 = Bike(200, 20)
bike2.reverse().displayInfo()
