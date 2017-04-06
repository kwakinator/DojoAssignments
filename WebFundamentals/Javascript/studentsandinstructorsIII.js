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

 function outputUsers(obj){
   //get keys
    var keys = Object.keys(obj);

    //use key to get array of categories
    for(var i=0; i<keys.length; i++){ //loops a new key for individual category-- 'Students' and 'Instructors'
      var category = keys[i]; //makes keys into individual category in index
      console.log(category);
      var namesList = obj[category];  //set a new variable for each name in category (first_name and last_name)

      //iterate the array to get objects within category
      for (var j = 0; j < namesList.length; j++){
          var name = namesList[j]; //individualizes each object within category
          
      //print the student's information
            name = ((j+1) + " - " + name.first_name + " " + name.last_name + " - " + (name.first_name.length + name.last_name.length)); //creates most of the info wanted to print
            var upper = name.toUpperCase(); //capitalizes
            console.log(upper);
      }
    }
}

outputUsers(users);
