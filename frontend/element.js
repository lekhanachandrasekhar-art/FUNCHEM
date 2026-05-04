const BASE_URL = "http://127.0.0.1:8000";

const params = new URLSearchParams(window.location.search);
const symbol = params.get("symbol");

fetch(BASE_URL + "/elements")
.then(res => res.json())
.then(data => {

    const el = data.find(e => e.symbol === symbol);

    document.getElementById("title").innerText =
        el.name + " (" + el.symbol + ")";

    document.getElementById("info").innerHTML = `
        <p>Atomic Number: ${el.atomic_number}</p>
        <p>Atomic Mass: ${el.atomic_mass}</p>
        <p>Valency: ${el.valency}</p>
        <p>Oxidation States: ${el.oxidation_states}</p>
        <p>Bond Type: ${el.bond_type}</p>
        <p>Applications: ${el.applications}</p>
    `;
});

function goBack() {
    window.location.href = "home.html";
}