var users = {
 'Students': [
     {first_name: 'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 }

 function outputUsers(array){
   console.log('Students');
   for (var i = 0; i < array['Students'].length; i++){
     console.log((i+1) + " - " + users['Students'][i].first_name + " " + users['Students'][i].last_name + " - " + (users['Students'][i].first_name.length + users['Students'][i].last_name.length));
   }
   console.log('Instructors');
     for (var i = 0; i<array['Instructors'].length; i++){
       console.log((i+1) + " - " + users['Instructors'][i].first_name + " " + users['Instructors'][i].last_name + " - " + (users['Instructors'][i].first_name.length + users['Instructors'][i].last_name.length));
   }
 }

 outputUsers(users);
