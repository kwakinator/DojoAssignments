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
   for (var {first_name: f, last_name: l} of users['Students']){
     console.log((Object.keys(users['Students'])) + " - " + f + " " + l + " - " + (f.length + l.length));
   }
   console.log('Instructors');
   for (var {first_name: f, last_name: l} of users['Instructors']){
    console.log((Object.keys(users['Instructors'])) + " - " + f + " " + l + " - " + (f.length + l.length));
   }
 }

 outputUsers(users);
