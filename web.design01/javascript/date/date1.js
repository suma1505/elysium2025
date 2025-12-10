// default date and time
let now=new Date()
console.log(now);

// custom date and time

let specific=new Date(2004, 5, 2);
console.log(specific);

// getting values

let today=new Date()
console.log(today.getDate());
console.log(today.getFullYear());

// setting values

let day=new Date()
day.setFullYear(2004)
day.setMonth(1)
day.setDate(5)
console.log(day);

// formatting date

let date = new Date();

let dd = String(date.getDate()).padStart(2, '0');
let mm = String(date.getMonth() + 1).padStart(2, '0'); 
let yyyy = date.getFullYear();

console.log(`${dd}-${mm}-${yyyy}`);

