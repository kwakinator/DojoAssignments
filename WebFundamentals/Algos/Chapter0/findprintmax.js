  function printMax(arr){
  var max = 0;
  for (var i = 0; i<array.length; i++){
    if(arr[i] > max){
      max = arr[i];
    }
  }
  return max;
}

var test=[1,2,3,4,5];
console.log(printMax(test));
