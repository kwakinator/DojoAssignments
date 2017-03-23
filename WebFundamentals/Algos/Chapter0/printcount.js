var log = 0
for(i = 512; i<4096; i++){
  if(i % 5 === 0){
    console.log(i);
    log = log+1;
  }
}
console.log(log)
