
function asignarFuncionBotonEliminar() {
    const botonesEliminar = document.querySelectorAll('.eliminar_gasto');
    console.info(botonesEliminar)
    botonesEliminar.forEach((boton) => {
        boton.addEventListener('click', () => {
            let divMasCercano = boton.closest('.d-flex');

            divMasCercano.remove();
        })
    })
}

function addInputAgregar() {
    const container = document.getElementById("input-container");
    const nuevoDiv = document.createElement("div");
    const botonEliminar = document.createElement("div");
    const spanEliminar = document.createElement("span");
    const nameInput = document.createElement("input");

    nuevoDiv.className = 'd-flex gap-1'
    nuevoDiv.style.maxHeight = '20px'
    nuevoDiv.style.position = 'relative'

    nameInput.type = "text";
    nameInput.name = "nombre_gasto";
    nameInput.required = true;
    nameInput.placeholder = 'Nombre';
    nameInput.className = 'w-45';

    const priceInput = document.createElement("input");
    priceInput.type = "number";
    priceInput.name = "precio_gasto";
    priceInput.required = true;
    priceInput.placeholder = 'Precio';
    priceInput.className = 'w-45';

    botonEliminar.className = 'eliminar_gasto';
    spanEliminar.className = 'material-symbols-outlined';
    spanEliminar.innerText = 'cancel'

    botonEliminar.appendChild(spanEliminar);

    nuevoDiv.appendChild(nameInput);
    nuevoDiv.appendChild(priceInput);
    nuevoDiv.appendChild(botonEliminar);
    container.appendChild(nuevoDiv);

    asignarFuncionBotonEliminar();
}





