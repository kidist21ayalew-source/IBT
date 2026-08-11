// 1. vat calculation 
function Vat(amount,rate = 0.15) {
    return amount * rate
}
console.log(Vat(100)) // 15

// arrow function with implicit return
const  vatArrow = (amount, rate = 0.15) => amount * rate

console.log(vatArrow(100)) 

//2. makeCounter 
function makeCounter() {
    let count = 0;

    return function() {
        count++;
        return count;
    };
}    

const counter = makeCounter();
console .log(counter());
console .log(counter());
console .log(counter());
console .log(counter());
console .log(counter());

//count is private to the makecounter function, it is not accessible from outside the function.
//3.discountBy
function discountBy(rate) {
    return function(price){
        return price - (price*rate);
    };
}

//create a 10% discount function
const memberPrice = discountBy(0.1);

//create a 30% discount function
const salePrice = discountBy(0.3);

//apply both discount to 1000ETB
console.log("member price: ", memberPrice(1000), "ETB"); 
console.log("sale price: ", salePrice(1000), "ETB"); 


//4. higher-order function
function applyToAll(list,fn){
    const result = [];

    for (const item of list){
        result.push(fn(item));
    }
    return result;
}

//prices  in ETB
const prices = [100, 200, 300, 400];

//function that adds 15% VAT
const addVAT =price =>price + (price*0.15);

//apply VAT to every price
const priceWithVAT =applyToAll(prices, addVAT);

console.log(priceWithVAT);


//5.Ethiopian cities
const cities = ["Addis Ababa", "Bahir Dar", "Gondar", "Mekelle", "Hawassa"];

cities .forEach(function(city, index) {
    console.log(`${index + 1}. ${city}`);
});
