##Multiples
##Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.
for num in range(0,1001):
    if num %2 != 0:
        print num
        num +=1

##Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.
for num1 in range(5, 1000001,5):
    ##if num1 %5 == 0:
        print num1
    ##  num1 +=1

##Sum List
##Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
print sum(a)

##Average List
##Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
print sum(a)/len(a)
