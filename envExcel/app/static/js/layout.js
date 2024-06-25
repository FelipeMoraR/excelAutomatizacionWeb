function addInputAgregar() {
    const container = document.getElementById("input-container");
    const nuevoDiv = document.createElement("div");
    const botonEliminar = document.createElement("div");
    const nameInput = document.createElement("input");

    nuevoDiv.className = 'd-flex justify-content-space-between'


    nameInput.type = "text";
    nameInput.name = "nombre_gasto";
    nameInput.required = true;
    nameInput.placeholder = 'Nombre';
    nameInput.className = 'input-paso2';

    const priceInput = document.createElement("input");
    priceInput.type = "number";
    priceInput.name = "precio_gasto";
    priceInput.required = true;
    priceInput.placeholder = 'Precio';
    priceInput.className = 'input-paso2';

    nuevoDiv.appendChild(nameInput);
    nuevoDiv.appendChild(priceInput);
    nuevoDiv.appendChild(botonEliminar);
    container.appendChild(nuevoDiv);
    
}

