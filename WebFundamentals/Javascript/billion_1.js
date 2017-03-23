var money = .01 ;
for(var days= 1; days <= 30; days++){
  money = money + (money*=2);
}
console.log("The accumulated reward total by day 30 is $" + money);
