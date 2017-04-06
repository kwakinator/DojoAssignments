import random

def coin_tosses(num):
    print "Starting the Program..."
    heads = 0
    tails = 0
    result = ''
    for tries in range(1, num):
        random_num = random.random()
        coin = round(random_num)
        if coin < 1:
            heads +=1
            result = "head"
        elif coin == 1:
            tails +=1
            result= "tail"
        print "Attempt #{}: Throwing a coin... It's a {}!... Got {} head(s) so far and {} tail(s) so far".format(tries, result, heads, tails)
    print "Ending the program, thank you!"

coin_tosses(5001)
