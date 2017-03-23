var hour = 2;
var minute = 31;
var period = "AM";

if (minute <= 30 && period ==="AM"){
  console.log("It's just after", hour, "in the morning");
}
else if (minute > 30 && period === "AM") {
  console.log("It's almost", (hour+1), "in the morning");
}
else if (minute <= 30 && period === "PM") {
  console.log("It's almost", (hour+1), "in the evening");
}
else {
  console.log("It's almost", (hour+1), "in the evening");
}
