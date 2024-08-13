document.addEventListener('DOMContentLoaded', () => {
    checkBox = document.querySelector('#verGasto');
    containerInput = document.querySelector('#nombreHoja');
    input = containerInput.querySelector('input');
    btn = document.querySelector('#accionVerGastos');

    checkBox.addEventListener('change', (e) => {
        if (e.target.checked === true){
            btn.classList.remove('d-none');
            containerInput.classList.remove('d-none');
            containerInput.classList.add('d-flex');
            input.required = true;
        } 
        else {
            btn.classList.add('d-none');
            containerInput.classList.add('d-none');
            containerInput.classList.remove('d-flex');
            input.required = false;
        }
    })
});