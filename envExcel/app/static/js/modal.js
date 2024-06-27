document.addEventListener('DOMContentLoaded', () => {
    let modalCarga = document.getElementById('modalCarga');
    let overlayCarga = document.getElementById('overlayCarga');
    let form = document.querySelector('.formulario-excel');
    let body = document.body;

    let botonCerrarResultado = document.getElementById('cerrarModal');
    let modalResultado = document.getElementById('modalResultado');
    let overlayResultado = document.getElementById('overlayResultado');

    if(form){
        form.addEventListener('submit', () => {
            momodalCargadal.style.display = 'flex';
            overlayCarga.style.display = 'block';
            body.style.overflow = 'hidden';
        });
    }
        
    if (modalCarga){
        modalCarga.style.display = 'none';
        overlayCarga.style.display = 'none';
        body.style.overflow = 'auto';
    }
        

    if (botonCerrarResultado){
        botonCerrarResultado.addEventListener('click', () => {
            modalResultado.style.display = 'none';
            overlayResultado.style.display = 'none';
            body.style.overflow = 'auto';
        });
    }
});