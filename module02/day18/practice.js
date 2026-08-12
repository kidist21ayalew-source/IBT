//Question N01

// const prices = [500, 750, 900, 1200, 650]


// const total = prices
//     .map(price => price * 1.15)
//     .filter(price =>price <1000)
//     .reduce((sum, price) =>sum +price, 0);

// console.log(total);     


//Question N02

// const customer ={
//     name: "kidist",
//     city: "Addis Ababa",
//     balance: 5000,

// };


// for (const [key, value] of Object.entries(customer)) {
//     console.log(`${key}: ${value}`);
// }


//Question N03

// const customer = {
//     name: "Kidist",
//     city: "Addis Ababa",
//     balance: 5000
// };

// const { name, city } = customer;

// function greet({ name }) {
//     console.log(`Hello, ${name}!`);
// }

// console.log(name);
// console.log(city);

// greet(customer);

//Question N04

const customer = {
    name: "Kidist",
    city: "Addis Ababa",
    balance: 5000
};

const updatedCustomer = {
    ...customer,
    city: "Hawassa",
    phone: "0912345678"
};

console.log("Original:", customer);
console.log("Updated:", updatedCustomer);