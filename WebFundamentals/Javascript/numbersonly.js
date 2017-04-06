function numbersOnly(arr){
  var newArray = [];
  for (var i = 0; i<= arr.length; i++){
    if (typeof arr[i] === "number"){
      newArray.push(arr[i]);
    }
  }
  return newArray;
}

var numArray = [1, 2, "eight", 2, "thing1", "thing2", 9, 7, true];

console.log(numbersOnly(numArray));
