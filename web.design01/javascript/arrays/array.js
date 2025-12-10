let frds=["sundar","arun","santhose"]
console.log(frds);
console.log(frds[0]);
frds[1]="kumar"
console.log(frds[1]);
console.log(frds);
for(let frd of frds){
    console.log(frd);
}

frds.push("arun")
frds.push("prakash")
console.log(frds);
frds.pop()
console.log(frds);

frds.shift()
console.log(frds);
frds.unshift("prakash")
console.log(frds);

console.log( frds.includes("sundar"));