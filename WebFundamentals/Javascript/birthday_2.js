var daysUntilMyBirthday = 50;

while (daysUntilMyBirthday >=0){
  if(daysUntilMyBirthday >=30){
    console.log(daysUntilMyBirthday + " days until my birthday. Such a long time... :(")
  }
  else if (daysUntilMyBirthday < 30 && daysUntilMyBirthday > 5){
    console.log(daysUntilMyBirthday + " days until my birthday. Getting Closer!!");
  }
  else if (daysUntilMyBirthday <= 5 && daysUntilMyBirthday >= 2){
    console.log(daysUntilMyBirthday + " DAYS UNTIL MY BIRTHDAY!!!");
  }
  else if (daysUntilMyBirthday == 1){
    console.log(daysUntilMyBirthday + " DAY UNTIL MY BIRTHDAY!!!");
  }
  else {
    console.log("♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪ღ♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•*♪ღ♪░H░A░P░P░Y░ B░I░R░T░H░D░A░Y░░♪ღ♪*•♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•«");
  }
  daysUntilMyBirthday--;
}
