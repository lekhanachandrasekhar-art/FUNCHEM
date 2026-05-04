const BASE_URL = "http://127.0.0.1:8000";

window.onload = function () {

    const params = new URLSearchParams(window.location.search);
    const e1 = params.get("e1");
    const e2 = params.get("e2");

    const pairDiv = document.getElementById("pairDisplay");
    const container = document.getElementById("compoundContainer");

    if (!pairDiv || !container) {
        console.error("HTML elements missing!");
        return;
    }

    // ✅ Show selected elements
    pairDiv.innerText = `${e1} + ${e2}`;

    // ✅ Fetch compounds
    fetch(`${BASE_URL}/compounds?e1=${e1}&e2=${e2}`)
        .then(res => res.json())
        .then(data => {

            if (!data.possible_compounds || data.possible_compounds.length === 0) {
                container.innerHTML = "<p>No compounds found</p>";
                return;
            }

            // 🔥 CREATE BUTTONS
            data.possible_compounds.forEach(c => {

                const btn = document.createElement("button");

                btn.className = "compound-btn";
                btn.innerText = c.formula;

                // ✅ FIX: DIRECT POPUP CALL
                btn.onclick = () => showCompoundPopup(c);

                container.appendChild(btn);
            });
        })
        .catch(err => {
            console.error(err);
            container.innerHTML = "<p>Error loading data</p>";
        });
};



// 🔥 POPUP FUNCTION (WORKING)
function showCompoundPopup(c) {
    const popup = document.getElementById("popup");
    const body = document.getElementById("popup-body");

    if (!popup || !body) {
        console.error("Popup not found!");
        return;
    }

    body.innerHTML = `
        <h2>${c.formula}</h2>
        <p><b>Name:</b> ${c.name}</p>
        <p><b>Bond Type:</b> ${c.bond_type}</p>
        <p><b>State:</b> ${c.state}</p>
        <p><b>Color:</b> ${c.color}</p>
        <p><b>Uses:</b> ${c.uses}</p>
        <p><b>Description:</b> ${c.description}</p>
        
    `;

    popup.style.display = "flex";
}



// 🔥 CLOSE POPUP
function closePopup() {
    document.getElementById("popup").style.display = "none";
}
function goBack() {
    window.location.href = "home.html";
}