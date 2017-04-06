var array = ["James", "Jill", "Jane", "Jack"];
var symbol = [" -> ", " => ", " :: ", " ---- "]

function printArray(reversed){
  if(reversed == true){
    for (var i = (array.length)-1; i>=0; i--){
      console.log( i + symbol[2] + array[i])
    }
  }
  else{
    for (var i = 0; i < array.length; i++){
      console.log( i + symbol[3] + array[i]);
    }
  }
}
printArray(true);
