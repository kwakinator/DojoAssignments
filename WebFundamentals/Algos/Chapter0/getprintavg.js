var avg = 0;
var sum= 0;
var array = [2,4,6,2,8];
for (var i=0; i>array.length; i++){
  sum = sum + array[i];
  avg = sum / array.length;
}
console.log(avg)
