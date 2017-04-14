my_list = [41, 23]
my_second_list = [
    42,
    24
]

try:
    print my_list[1] + 'hello'
except (IndexError, TypeError):
    print my_list[0] + my_second_list[1]

i, j = (1,2), [3,4]
j[1]=42
print j

num = 1,2,3
print num
num1, num2, num3 = 1,3,5
print num2
##prints


##i,j = 1,2,3
##print j
##(i,j),k = (1,2,3)
##print j
##go over tuples again

our_list =  ['Martin', "Michael"]
for val in enumerate (our_list):
    print val

for idx, value in enumerate(our_list):
    #print value, idx
    print value + ' {}'.format(idx)

name = {"sw": "Sara Wong", "mp": "Martin Puryear", 'mk': "Michael Kors"}
for key, value in name:
    print key, value
##unpacking like a tuple but NOT a tuple

for key, bacon in name.items():
    print key, bacon

##name.items() packages it, and then unpacks in when we declare key and bacon
