
document.addEventListener('DOMContentLoaded', () => {
    input = document.getElementById('posicion_gasto')
    enviar = document.getElementById('enviar');

    input.addEventListener('change', () => {

        if (input.value < 0){
            enviar.disabled = true
        } else{
            enviar.disabled = false
        }
        
    })
})
