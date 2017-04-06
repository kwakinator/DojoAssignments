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

function doesTheStuff(obj){
  //get keys
   var keys = Object.keys(obj);
   //use key to get array of peeps
   for(var i=0; i<keys.length; i++){
     //set a new key for each category 'Students' and 'Instructors' and print
     var curKey = keys[i];
     console.log(curKey);
     //set a new variable for to print names in each category (first_name and last name)
     var peepList = obj[curKey];
    // console.log(peepList);
     //iterate the array to get student objects
     for (var j = 0; j < peepList.length; j++){
       //console.log(peepList[j]{
         var peep = peepList[j];
         console.log(peep.first_name + ' ' + peep.last_name);
       }
     }
       //print the student's information
   }


doesTheStuff(users);
