function printRange(x,y,z)
{
  if (x,y,z){
    for(x=x; x<y;x+=z){
      console.log(x);
    }
  }
  else if(x,y) {
    for(x=x; x<y; x++){
      console.log(x);
    }
  }
  else if(x) {
    for (var i=0; i<x; i++){
      console.log(i);
    }
  }
}

printRange(1, 11, 2);
