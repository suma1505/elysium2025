// promise ()
const promise = new Promise((resolve, reject) => {
  let success = true;
  if (success) {
    resolve(" Operation success");
  } 
  else {
    reject("Operation failed");
  }
});

promise
  .then((msg) => console.log(msg))
  .catch((err) => console.error(err));

// settimeout () + promise

function waitForMe() {
  return new Promise((resolve) => {
  setTimeout(() => {
  resolve(" Waited 2 seconds");
  }, 2000);
  });
}

waitForMe().then((msg) => console.log(msg));

 // async/await

function delay(ms) {
  return new Promise(resolve => setTimeout(resolve,ms))
}
async function main(){
  console.log("start")
  await delay(2000)
  console.log("end after 2 second")
}
main()

 // fake API with promise

function  fetchUserData() {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
      resolve({ name: "Sneha", age: 21 });
    }, 1500);
  });
 }

//  fake API with promise

 async function showUser() {
  console.log(" Fetching user...");
   const user = await fetchUserData();
  console.log(" User:", user);
}

showUser();

 // mini project
 function orderPizza(flavor) {
    return new Promise((resolve, reject) => {
      if (flavor === "chicken") {
      setTimeout(() => resolve("Chicken pizza ready!"), 2000);
    } else {
    reject(" Sorry, only veg available.");
  }
});
}

// mini project

async function placeOrder() {
  try {
    console.log(" Placing order...");
    const result = await orderPizza("chicken");
    console.log(result);
  } catch (err) {
  console.log(err);
  }
}

placeOrder()

