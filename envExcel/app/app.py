from flask import Flask, render_template, request, url_for, redirect
import sys
import os

# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# Ahora puedes importar googleSheet.py
import googleSheet

app = Flask(__name__)

sheets_service = googleSheet.conexionSheetBuildService()

drive_service = googleSheet.conexionDriveBuildService()
cliente = googleSheet.conexionDriveCliente()

#@app.before_request
#def before_request():
    #print('Antes de la peticion')


#@app.after_request
#def after_request(response):
    #print('Despues de la peticion')
    #return response

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/verExcel')
def verExcel():

    dataVerExcel = {
        'estado': '',
        'urlExcel': ''
    }

    return render_template('verExcel.html', dataVerExcel = dataVerExcel)


@app.route('/submit_form_ver', methods=['POST'])
def submit_form_ver():
    if request.method == 'POST':
        nombre = request.form['nombre']

        if googleSheet.verificarExistenciaExcel(nombre, drive_service):
            excel = googleSheet.obtenerExcel(nombre, drive_service)
            urlExcel = googleSheet.obtener_url_archivo(excel['id'], drive_service)
            dataVerExcel = {
                'estado': '200',
                'urlExcel': urlExcel
            }
        else:
            dataVerExcel = {
                'estado': '404',
                'urlExcel': ''
            }

        return render_template('verExcel.html', dataVerExcel = dataVerExcel)
       
        
        
    return 'Error al enviar el formulario'


@app.route('/crearExcel')
def crearExcel():
    dataCrearExcel = {
                'estado': '',
                'urlExcel': ''
            }
    
    return render_template('crearExcel.html', dataCrearExcel = dataCrearExcel)


@app.route('/submit_form_crear', methods=['POST'])
def submit_form_crear():
    if request.method == 'POST':
        nombre = request.form['nombre']     
        
        if googleSheet.crearExcel(nombre, cliente, drive_service, sheets_service):
            excelCreado = googleSheet.obtenerExcel(nombre, drive_service)
            urlExcelCreado = googleSheet.obtener_url_archivo(excelCreado['id'], drive_service)

            dataCrearExcel = {
                'estado': '200',
                'urlExcel': urlExcelCreado
            }
        else:
            dataCrearExcel = {
                'estado': '404',
                'urlExcel': ''
            }
            
        return render_template('crearExcel.html', dataCrearExcel = dataCrearExcel)
    
    return 'Error al enviar el formulario'

@app.route('/modificarExcel')
def modificarExcel():
    return render_template('modificarExcel.html')



#Este es un ejemplo
@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data = {
        'titulo': 'contacto',
        'nombre': nombre,
        'edad': edad
    }
    return render_template('contacto.html', data = data)

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    return "ok"

def pagina_no_encontrada(error):
    return render_template('404.html'), 404
    #return redirect(url_for('index'))

if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func = query_string)
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug = True, port = 5021)