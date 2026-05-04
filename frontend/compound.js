const BASE_URL = "http://127.0.0.1:8000";

window.onload = function () {

const params = new URLSearchParams(window.location.search);

const data = {
    formula: params.get("formula"),
    name: params.get("name"),
    bond: params.get("bond"),
    state: params.get("state"),
    color: params.get("color"),
    uses: params.get("uses"),
    desc: params.get("desc")
};

const container = document.getElementById("compound-info");

container.innerHTML = `
    <h2>${data.formula}</h2>
    <p><b>Name:</b> ${data.name}</p>
    <p><b>Bond Type:</b> ${data.bond}</p>
    <p><b>State:</b> ${data.state}</p>
    <p><b>Color:</b> ${data.color}</p>
    <p><b>Uses:</b> ${data.uses}</p>
    <p><b>Description:</b> ${data.desc}</p>
`;

function goBack() {
    window.history.back();
}
}


