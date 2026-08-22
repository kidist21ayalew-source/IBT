import { menu } from "./data/menu.js";

const menuList = document.querySelector("#menuList");
const searchInput = document.querySelector("#search");
const cartItems = document.querySelector("#cartItems");
const cartTotal = document.querySelector("#cartTotal");
const clearCart = document.querySelector("#clearCart");
const categoryButtons = document.querySelector("#categoryButtons");

let cart =JSON.parse(localStorage.getItem("cart")) || [];
let selectedCategory = "All";


displayCart();

function displayMenu(dishes) {
    menuList.innerHTML = "";

    dishes .forEach(dish => {
        const card = document.createElement("div");
    
        card.classList.add("card");

        card.innerHTML = `
            <img src="${dish.images}" alt="${dish.name}">
            <h3>${dish.name}</h3>
            <p>Category: ${dish.category}</p>
            <p class="price">Price: ${dish.price} ETB</p>
            <p>${dish.spicy ?"Spicy" : "Not Spicy"}</p>
            <button class="addToCart" data-id="${dish.id}">
                Add to Cart
            </button>
    `;

    menuList.appendChild(card);
});

}
displayMenu(menu);

searchInput.addEventListener("input", () => {
    const searchText = searchInput.value.toLowerCase();

    const filteredMenu = menu.filter(dish =>
        (selectedCategory ==="All"|| dish.category===selectedCategory)&&
        (                                         
            dish.name.toLowerCase().includes(searchText)||
            dish.category.toLowerCase().includes(searchText)
        )
        );

    displayMenu(filteredMenu);
});
categoryButtons.addEventListener("click",event =>{
    if (event.target.tagName==="BUTTON") {
        selectedCategory = event.target.dataset.category;

        const searchText = searchInput.value.toLowerCase();

        const filteredMenu= menu.filter(dish =>
            (selectedCategory ==="All"||
            dish.category===selectedCategory) &&
            (
                dish.name.toLowerCase().includes(searchText)||
                dish.category.toLowerCase().includes(searchText)
            )
        );
            displayMenu(filteredMenu);
    }
        
});    
    
function displayCart() {
    cartItems.innerHTML = "";

    if(cart.length===0){
        cartItems.innerHTML ="<p>Your cart is empty.</p>";
    }

    cart.forEach(dish=> {
        const item = document.createElement("div");

        item.innerHTML =`
            <p>
            ${dish.name} - ${dish.price} ETB
            </p>
            <button class="decrease" data-id="${dish.id}">-</button>
            
            <span>${dish.quantity}</span>

            <button class="increase" data-id="${dish.id}">+</button>
            `;

            cartItems.appendChild(item);
    });

    const total=cart.reduce(
    (sum, dish) => sum +dish.price * dish.quantity,
    0

    );
    cartTotal.textContent = `${total} ETB`;
    localStorage.setItem("cart",JSON.stringify(cart));
   
} 

menuList.addEventListener("click", event => {
    if (event.target.classList.contains("addToCart")) {
        
        const id = Number(event.target.dataset.id);
        
        const dish = menu.find(dish =>dish.id===id);
        
        const existingDish = cart.find(dish =>dish.id ===id);

        if (existingDish) {
            existingDish.quantity++;
        }else{

        cart.push({
            ...dish,
            quantity:1
        });
        }
        displayCart();
        }

    });   
    
    cartItems.addEventListener("click",event => {
        const id = Number(event.target.dataset.id);
        const dish = cart.find(dish =>dish.id===id);

        if(event.target.classList.contains("increase")) {
            dish.quantity++;

            displayCart();
        }
        
        if(event.target.classList.contains("decrease")) {
            dish.quantity--;
            
            if(dish.quantity===0) {
                cart = cart.filter(dish => dish.id !==id);
            }

            displayCart();
        }

    });
    
clearCart.addEventListener("click",() =>{
    cart = [];
    displayCart();
})    

