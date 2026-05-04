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

    // Show selected elements
    pairDiv.innerText = `${e1} + ${e2}`;

    // Fetch compounds
    fetch(`${BASE_URL}/compounds?e1=${e1}&e2=${e2}`)
        .then(res => res.json())
        .then(data => {

            if (!data.possible_compounds || data.possible_compounds.length === 0) {
                container.innerHTML = "<p>No compounds found</p>";
                return;
            }

            data.possible_compounds.forEach(c => {
                const btn = document.createElement("button");

                btn.className = "compound-btn";
                btn.innerText = c.formula;

                // 🔥 IMPORTANT: send full data
                btn.onclick = () => goToCompound(c);

                container.appendChild(btn);
            });
        })
        .catch(err => {
            console.error(err);
            container.innerHTML = "<p>Error loading data</p>";
        });
};


// 🔥 FUNCTION MUST BE OUTSIDE (NOT INSIDE LOOP)
function goToCompound(c) {

    const params = new URLSearchParams({
        formula: c.formula,
        name: c.name,
        bond: c.bond_type,
        state: c.state,
        color: c.color,
        uses: c.uses,
        desc: c.description
    });

    window.location.href = "compound.html?" + params.toString();
}


// Back button
function goBack() {
    window.history.back();
}