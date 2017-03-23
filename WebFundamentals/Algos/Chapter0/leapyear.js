function leapYear(Y){
  if (Y % 4 === 0 && (Y % 100 !==0 || Y % 400 === 0)){
    console.log("It is leap year!");
  }
  else {
    console.log("Not leap year!");
  }
}

leapYear(2020);
leapYear(2522);
leapYear(6852);
