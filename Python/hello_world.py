x = "Hello Python"
print x
y=42
print y

z="Zen"
aa="Coder"
print "My name is", z
print "My name is " + z

num1 = 12
print "this number is", num1

print "My name is {} {}". format(z, aa)

for count in range (0, 5):
    print "looping -", count

count = 0
while count < 5:
    print 'looping -', count
    count +=1

for val in "string":
    if val =="i":
        break
    print(val)
