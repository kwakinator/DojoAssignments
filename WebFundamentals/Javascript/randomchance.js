function playSlots(numQuarters){
  for(numQuarters = numQuarters; numQuarters > 0; numQuarters--){
    var winNum = Math.floor(Math.random()*100)+1;
    if (winNum === 1){
      var coinsWon = Math.floor(Math.random()*50)+51;
      numQuarters = numQuarters + coinsWon;
      console.log("Congrats! You won " + coinsWon + " quarters!! You now have a total of " + numQuarters + " quarters!")
    }
    else if (winNum !== 1) {
      console.log("Try Again!");
    }
  }
  return 0;
}

playSlots(100);
