// method 1
let person={
    name:"uma",
    age:21,
    city:"ariyalur"
}
console.log(person);
console.log(person.name);
console.log(person.age);
console.log(person.city);

person.name="sneha"
person.city="trichy"
console.log(person);

// method 2

let student=new Object()

student.name="uma"
student.age=21
student.mark=480
console.log(student);

student.name="prarthana"
student.age=21
student.mark=578
console.log(student);

student.name="sneha"
student.age=21
student.mark=558
console.log(student);

// method 3

class product{
    constructor(id,name,price){
        this.id=id
        this.name=name
        this.price=price
    }
     validate(){
        return this.salary+=2000
    }
    display(){
        console.log(`Id:${this.id}|Name:${this.name}|price:${this.price}`);
    }
}
let product1=new product(1,"tv",15000)
let product2=new product(2,"fridge",10000)
let product3=new product(3,"washing machine",20000)
let product4=new product(4,"ac",30000)

product1.display()
product2.display()
product3.display()
product4.display()
  