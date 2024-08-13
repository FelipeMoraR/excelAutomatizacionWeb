document.addEventListener('DOMContentLoaded', () => {
    const elementoDiv = document.getElementById('containerGastos');
    if (elementoDiv){
        const altoVisible = elementoDiv.clientHeight;
        const altoTotal = elementoDiv.scrollHeight;
        const flechaAbajo = document.querySelector('.container-flecha-abajo');
        const containerGastos = document.querySelectorAll('.container-gasto');
    

        if(altoTotal <= altoVisible){
            flechaAbajo.style.display = 'none';
        }

        containerGastos.forEach((gasto) => {
            gasto.addEventListener('click', () => {
                gasto.classList.toggle('gasto-agregado');
            });
        })
    }
    
})