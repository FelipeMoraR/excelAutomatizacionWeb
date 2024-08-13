
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
    const select = document.createElement("select");
    const opcionesSelect = [
        {
            'text':'Supermercado',
            'value':'super'
        },
        {
            'text':'Fijo',
            'value':'fijo'
        },
        {
            'text':'Salida',
            'value':'salida'
        }, 
        {
            'text':'Regalo',
            'value':'regalo'
        }, 
        {
            'text':'Pasaje',
            'value':'pasaje'
        }
        , 
        {
            'text':'Personal',
            'value':'personal'
        }
        ,
        {
            'text':'Otro',
            'value':'otro'
        }]
    
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


    opcionesSelect.forEach(opcion => {
        const opcionElement = document.createElement('option');
        opcionElement.value = opcion.value
        opcionElement.textContent = opcion.text;
        select.appendChild(opcionElement);
    })
    select.classList.add('w-45');


    botonEliminar.appendChild(spanEliminar);

    nuevoDiv.appendChild(nameInput);
    nuevoDiv.appendChild(priceInput);
    nuevoDiv.appendChild(botonEliminar);
    nuevoDiv.appendChild(select);
    container.appendChild(nuevoDiv);

    asignarFuncionBotonEliminar();
}





