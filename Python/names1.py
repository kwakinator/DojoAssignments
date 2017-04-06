students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

##Method 1:
##for idx in range(len(students)):
##    print students[idx]['first_name'], students[idx]['last_name']

##Method 2:
##for item in students:
##    print item['first_name'], item['last_name']

##Method 3:
for item in students:
    print " ".join(item.values())

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for key in users:
    print key
    counter = 0
    for name in users[key]:
        fullName= " ".join(name.values())
        length = len(fullName)-1
        counter +=1
        print counter, '-', fullName.upper(), '-', length



## add numbers
##capitalize
##length of names
