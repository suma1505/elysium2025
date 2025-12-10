// destucture operator

let person={
    name:"uma",
    age:21,
    city:"ariyalur"
}
const {name,age,city}=person
    console.log(name);
    console.log(age);
    console.log(city);

 let colors=["pink","purple","violet"]
 const[a,b,c]=colors
 console.log(a);
 console.log(b);
 console.log(c);

 // spred operator

 let frd=["uma"]

 let frds=[...frd,"prarthana","sneha"]
 console.log(frds);

 // rest operator

 let person1={
     name1:"uma",
     age1:21,
     city1:"ariyalur"
    }

 const{name1,age1,...others}=person1

 console.log(name1);
 console.log(age1);
 console.log(others);

 let fruits=["apple","orange","grapes","pineapple"]
 const [fruit,...res]=fruits

 console.log(fruit);
 console.log(res); 