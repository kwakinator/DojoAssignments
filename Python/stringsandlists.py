str = "It's thanksgiving day. It's my birthday, too!"
print str
print str.find("day")

new_str = str.replace("day","month", 1)
print new_str

x = [2,54,-2,7,12,98]
print "min value element: ", min(x)
print "max value element: ", max(x)

y = ["Hello","hello",2,54,-2,7,12,98,"world","World"]
z = []
z.append(y[0])
z.append(y[-1])
print z

w = [19,2,54,-2,7,12,98,32,10,-3,6]
list.sort(w)
print w
first_list = w[0:len(w)/2]
print "first list", first_list
second_list = w[len(w)/2:len(w)]
print "second list", second_list
second_list.insert(0, first_list)
print second_list
