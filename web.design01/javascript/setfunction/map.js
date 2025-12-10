// map method
// set()

let mymap=new Map()
mymap.set("name", "uma");
mymap.set(2, "two");
mymap.set(false, "no");
console.log(mymap);

// get()

console.log(mymap.get("name"));
console.log(mymap.get(false));

// has()

console.log(mymap.has(2));

// delete()

console.log(mymap.delete(false));

// size()

console.log(mymap.size);

// clear()

console.log(mymap.clear);

