var students = [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
]

function outputStudents(arr){
  for(var i in students){
    console.log(students[i].first_name + " " + students[i].last_name)
  }
}

outputStudents(students);
