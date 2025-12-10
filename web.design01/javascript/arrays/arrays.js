const cart = [
  { id: 1, name: "Laptop", price: 60000, qty: 1 },
  { id: 2, name: "Headphones", price: 2000, qty: 2 },
  { id: 3, name: "Mouse", price: 800, qty: 3 },
  { id: 4, name: "Keyboard", price: 1500, qty: 1 }
];

// map fuction

const productnames=cart.map(id=>id.name);
console.log(productnames);

const ProductTotals = cart.map(id=>({
  name: id.name,
  total: id.price * id.qty
}));
console.log(ProductTotals);

// filter fuction

const Productitems=cart.filter(id=>id.qty>1);
console.log(Productitems);

// reduce function

const ProducttotalAmount = cart.reduce((acc, id)=>acc + id.price*id.qty, 0);
console.log(ProducttotalAmount);

// foreach fuction

cart.forEach(id=>{
  console.log(`${id.qty} x ${id.name} = RS.${id.price * id.qty}`);
});

// some function

const LuxuryItem = cart.some(id=>id.price > 50000);
console.log(LuxuryItem);

// every function

const item = cart.every(id=>id.price > 50000);
console.log(item);




