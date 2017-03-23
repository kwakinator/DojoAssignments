var sum = 0;
var avg = 0;

function avg1(arr){
  for(vari = 0; i<=arr.length; i++){
    sum+=arr[i];
  }
  avg = sum/arr.length;
  return avg;
}

test = [1,2,3,4,5];
console.log(avg1(test));
