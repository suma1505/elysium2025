// default functins

function great(){
    console.log("welcome to functions");
}
great()

// parameter functions

function sub(a,b){
    let res=a-b
    console.log(`sub of ${a} and ${b} is ${res}`);
}
sub(10,5)
sub(50,20)
sub(15,7)

// return functions

function div(a,b){
    return a/b
}
let value=div(10,5)
console.log(value);

// arrow functions

let name=()=>{
    console.log("hello user");
}
name()

// parameter arrow functions

let login=(user,password)=>{
    console.log(`username is ${user} and password is ${password}`);
}
login("admin",1234)
login("newadmin",1234)