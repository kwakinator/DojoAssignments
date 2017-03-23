//Given an array, move all values forward by one index, dropping the first and leaving a '0' value at the end.

function shiftVals(arr){
    //move all values forward
    for(var i = 0; i < arr.length-1; i++){
      arr[i] = arr[i+1];
    }
    //last index a 0
    arr[arr.length-1]=0;
    return arr;
}

var test =[1,2,3,4,5,6,7,8,9,10];
console.log(shiftVals(test));
