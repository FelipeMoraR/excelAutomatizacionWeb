function addInputAgregar() {
    const container = document.getElementById("input-container");
    
    const nameInput = document.createElement("input");
    nameInput.type = "text";
    nameInput.name = "nombre_gasto";
    nameInput.required = true
    
    const priceInput = document.createElement("input");
    priceInput.type = "number";
    priceInput.name = "precio_gasto";
    priceInput.required = true

    container.appendChild(nameInput);
    container.appendChild(priceInput);
    container.appendChild(document.createElement("br"));
}

function addInputEliminar() {
    const container = document.getElementById("input-container");
    
    const nameInput = document.createElement("input");
    nameInput.type = "text";
    nameInput.name = "nombre_gasto";
    nameInput.required = true
    
   

    container.appendChild(nameInput);
    container.appendChild(document.createElement("br"));
}