
document.addEventListener('DOMContentLoaded', () => {
    input = document.getElementsByName('accion')
    label = document.getElementById('hojaCalculo')

    input.forEach(element => {
        element.addEventListener('change', () => {
            if( element.value == 'agregarHoja'){
                label.innerText = 'Ingrese nombre hoja a agregar'
            }
            else if (element.value == 'eliminarHoja'){
                label.innerText = 'Ingrese nombre hoja a eliminar'
            } 
            else {
                label.innerText = 'Ingrese Hoja de calculo a modificar'
            }
        })
    });
    
})
