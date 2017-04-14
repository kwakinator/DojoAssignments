def type_list(list):
        if all (isinstance(element, int) for element in list):
            print "The array you entered is of integer type"
            print "Sum: ",sum(list)
        elif all (isinstance(element, str) for element in list):
            print "The array you enetered is of string type"
            print "String: " + ' '.join(list)
        else:
            print "The array you entered is of mixed type"
            print "String: " + " ".join(filter(lambda element: isinstance(element, str), list))
            print "Sum: ", sum(filter(lambda element: isinstance(element, int), list))


l = ['magical unicorns',19,'hello',98.98,'world', 'happy', 'joy', 'thing1', 'thing2', 58, 21, 93]

type_list(l)
