

const state = {
    rates: {},
    watchlist: [],

    };
const API_URL = ("https://open.er-api.com/v6/latest/ETB")


const status = document.querySelector("#status");
const currencySelect = document.querySelector("#currency");
const addwtchlistButton = document.querySelector("#add-watchlist");

async function fetchRates() {

    status.textContent ="Loading rates...";
    try{
        const response = await fetch(API_URL);

        if(!response.ok) {
            throw new Error("Failed to load rates");
        }
        const data = await response.json();
        state.rates = data.rates;
        renderCurrencies();
        status.textContent = "Exchange rate loaded successfully";
    }catch (error) {
        
            status.textContent = "Could not load exchange rates.";
            console.error(error);
    }

}    

function renderCurrencies() {
    currencySelect.innerHTML = "";
    Object.keys(state.rates).forEach(function(currency){
        
        const option = document.createElement("option");
        
        option.value = currency;
        option.textContent = currency;

        currencySelect.appendChild(option);
    })
}
fetchRates();

    