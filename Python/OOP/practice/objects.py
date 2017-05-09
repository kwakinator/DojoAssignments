# class card(object):
#     def __init__(self, suit, val):
#         self.suit="Hearts"
#         self.value = 10
#         self.color = "red"
#
# card1= card()
# print card1
# print card1.suit


##Utilize base class for other cards
class basecard(object):
    def __init__(self, color, value):
        self.height = 5
        self.width = 3
        self.color = color
        self.value = value

class unocard(basecard):
    def __init__(self, color=None, value=None):
        super(unocard, self).__init__(color, value)
        self.face = "Uno"

class playingcard(basecard):
    def __init__(self, suit="Hearts", color = None, value = None):
        ##need to call on super method to elicit the method
        super(playingcard,self).__init__(color, value)
        self.suit= suit
        #below are now eliminated because of the creation of basecard
        #self.value = value
        #self.color = "red"
    def check_color(self):
        if (self.suit == "Hearts" or self.suit == "Diamonds"):
            self.color = "Red"
        elif(self.suit == "Clubs" or self.suit == "Spades"):
            self.color = "Black"
        else:
            self.color = "None"
        print self.color, self.suit, self.value

card1= playingcard("Clubs", "Black", 3)
print card1.color
# card2= card("Hearts", 3)
# card3= card("Diamonds", 3)
# card4= card("Spades", 3)
# card5= card("Clubs", 3)
# card6= card("Hearts", 3)
# card7= card("Diamonds", 3)
# card8= card() ## will return error unless you insert default values in __init__
# card9=card("Spades")##will replace suit
# card10=card(10) ##will still only replace suit

# print card1.suit
# print card2.suit
# print card3.suit
# print card4.suit
# print card9.suit
# card5.check_color()
# card6.check_color()
# card7.check_color() ##so we don't have to pass through a parameter
