document.addEventListener('DOMContentLoaded', () => {
    let modal = document.getElementById('modalCarga');
    let overlayCarga = document.getElementById('overlayCarga');
    let form = document.querySelector('.formulario-excel');
    let body = document.body;

    let botonCerrarResultado = document.getElementById('cerrarModal');
    let modalResultado = document.getElementById('modalResultado');
    let overlayResultado = document.getElementById('overlayResultado');

    form.addEventListener('submit', () => {
        modal.style.display = 'flex';
        overlayCarga.style.display = 'block';
        body.style.overflow = 'hidden';
    });

    modal.style.display = 'none';
    overlayCarga.style.display = 'none';
    body.style.overflow = 'auto';

    if (botonCerrarResultado){
        botonCerrarResultado.addEventListener('click', () => {
            modalResultado.style.display = 'none';
            overlayResultado.style.display = 'none';
        });
    }
});