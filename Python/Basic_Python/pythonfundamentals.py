student = {
    "first_name": "Randy",
    "last_name": "Ventura",
    "age": [67, 15, 25, 40, 67]
}


student["first_name"] = "Michelle"
print student["first_name"]
print student['age'][2]

for item in student:
    print student[item]

for item in student:
    print item, student[item]

def ourFunction(num):
    print "hello\n" * num
for number in range(10):
    ourFunction(1)

ourFunction(8)
