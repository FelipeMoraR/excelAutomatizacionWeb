from flask import Flask, render_template, request, url_for, redirect, session
import sys
import os
import  ast
from decouple import config

# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# Ahora puedes importar googleSheet.py
import googleSheet

app = Flask(__name__)
app.secret_key = config('SECRET_KEY')


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
    data = session.get('data', None)
    print('data => ', data)
    if data:
        return render_template('index.html', data = data)
    else:
        dataModificarExcel = {
                        'estado': '',
                        'error': '',
                        'siguienteNivel': '',
                        'excelId': '',
                        'accion': '',
                        'nombreHojaCalculo': '',
                        
                    }
        return render_template('index.html', data = dataModificarExcel)

@app.route('/home')
def limpiarSesion():
    session.pop('data', None)
    return redirect(url_for('index'))


@app.route('/verExcel')
def verExcel():

    dataVerExcel = {
        'estado': '',
        'nombreExcel': '',
        'urlExcel': ''
    }

    return render_template('verExcel.html', dataVerExcel = dataVerExcel)


@app.route('/submit_form_ver', methods=['POST'])
def submit_form_ver():
    if request.method == 'POST':
        nombre = request.form['nombre'].lower()
        
        if googleSheet.verificarExistenciaExcel(nombre, drive_service):
            excel = googleSheet.obtenerExcel(nombre, drive_service)
            urlExcel = googleSheet.obtener_url_archivo(excel['id'], drive_service)
            
            dataVerExcel = {
                'estado': '200',
                'nombreExcel': nombre,
                'urlExcel': urlExcel
            }
        else:
            dataVerExcel = {
                'estado': '404',
                'nombreExcel': '',
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
        nombre = request.form['nombre'].lower()     
        
        if googleSheet.crearExcel(nombre, cliente, drive_service, sheets_service):
            excelCreado = googleSheet.obtenerExcel(nombre, drive_service)
            urlExcelCreado = googleSheet.obtener_url_archivo(excelCreado['id'], drive_service)

            dataCrearExcel = {
                'estado': '200',
                'error': '',
                'nombre': nombre,
                'urlExcel': urlExcelCreado
            }
        else:
            dataCrearExcel = {
                'estado': '404',
                'error': 'El excel ya existe',
                'nombre': '',
                'urlExcel': ''
            }
            
        return render_template('crearExcel.html', dataCrearExcel = dataCrearExcel)
    
    return 'Error al enviar el formulario'



@app.route('/modificarExcel')
def modificarExcel():
    dataModificarExcel = {
                'estado': '',
                'siguienteNivel': '1',
                'excelId': ''
            }
    

    return render_template('modificarExcel.html', data = dataModificarExcel)

@app.route('/submit_form_modificar', methods=['POST'])
def submit_form_modificar():
    if request.method == 'POST':
        nombreExcel = request.form['nombre'].lower()     
        accion = request.form['accion']     
        hojaCalculo = request.form['hojaCalculo'].lower()

        if accion == 'eliminarHoja' or accion == 'agregarHoja':
            if googleSheet.verificarExistenciaExcel(nombreExcel, drive_service):
                excel = googleSheet.obtenerExcel(nombreExcel, drive_service)
                
                if googleSheet.obtenerHojaCalculo(excel['id'], hojaCalculo, sheets_service) != None and accion != 'eliminarHoja':
                    print('Se encontró')
                    dataModificarExcel = {
                        'estado': '406',
                        'error': 'Se encontró la hoja de calculo, debes usar un nombre inexistente',
                        'siguienteNivel': '',
                        'excelId': '',
                        'nombreHojaCalculo': '',
                        'accion': '',
                        }
                    
                    return render_template('modificarExcel.html', data = dataModificarExcel)
                
                if accion == 'eliminarHoja':
                    print('algo => ', googleSheet.eliminarHoja(excel['id'], hojaCalculo, sheets_service))
                    if googleSheet.eliminarHoja(excel['id'], hojaCalculo, sheets_service) == False:
                        dataModificarExcel = {
                            'estado': '404',
                            'error': 'No existe la hoja a eliminar',
                            'siguienteNivel': '',
                            'excelId': '',
                            'accion': 'eliminarHoja',
                            'nombreHojaCalculo': '',
                        
                        }
                        return render_template('modificarExcel.html', data = dataModificarExcel)
                    else:
                        dataModificarExcel = {
                            'estado': '200',
                            'error': '',
                            'siguienteNivel': '',
                            'excelId': '',
                            'accion': 'eliminarHoja',
                            'nombreHojaCalculo': '',
                        
                        }
                        session['data'] = dataModificarExcel

                        return redirect(url_for('index'))
                        #return render_template('index.html', data = dataModificarExcel)
                
                else:
                    googleSheet.crearNuevaHoja(excel['id'], hojaCalculo, sheets_service, cliente)

                    dataModificarExcel = {
                        'estado': '200',
                        'error': '',
                        'siguienteNivel': '',
                        'excelId': '',
                        'accion': 'agregarHoja',
                        'nombreHojaCalculo': '',
                    
                    }
                    
                    session['data'] = dataModificarExcel

                    return redirect(url_for('index'))
                    #return render_template('index.html', data = dataModificarExcel)
            else:
                dataModificarExcel = {
                        'estado': '404',
                        'error': 'Excel no existe',
                        'siguienteNivel': '',
                        'excelId': '',
                        'accion': '',
                        'nombreHojaCalculo': '',
                        
                }

            return render_template('modificarExcel.html', data = dataModificarExcel)   
        

        else:
            if googleSheet.verificarExistenciaExcel(nombreExcel, drive_service):
                excel = googleSheet.obtenerExcel(nombreExcel, drive_service)
                listaDict = googleSheet.identificarTodosValoresFilasEliminar(excel['id'], hojaCalculo, cliente)
                print('lista => ', listaDict)

                if googleSheet.obtenerHojaCalculo(excel['id'], hojaCalculo, sheets_service) == None:
                    print('No se encontró nada')
                    dataModificarExcel = {
                        'estado': '404',
                        'error': 'No se encontró la hoja de calculo',
                        'siguienteNivel': '',
                        'excelId': '',
                        'nombreHojaCalculo': '',
                        'accion': '',
                        }
                    
                    return render_template('modificarExcel.html', data = dataModificarExcel)

                if accion == 'eliminar' and len(listaDict) == 0:
                    dataModificarExcel = {
                        'estado': '204',
                        'error': 'No existen valores a eliminar',
                        'siguienteNivel': '',
                        'excelId': '',
                        'accion': '',
                        'nombreHojaCalculo': '',  
                    }

                    return render_template('modificarExcel.html', data = dataModificarExcel)



                dataModificarExcel = {
                        'estado': '200',
                        'error': '',
                        'siguienteNivel': '2',
                        'excelId': excel['id'],
                        'accion': accion,
                        'nombreHojaCalculo': hojaCalculo,
                        'listaGastos' : listaDict
                        
                    }
                
                return render_template('modificarExcelPaso2.html', data = dataModificarExcel)

            else:
                dataModificarExcel = {
                        'estado': '404',
                        'error': 'Excel no existe',
                        'siguienteNivel': '',
                        'excelId': '',
                        'accion': '',
                        'nombreHojaCalculo': '',  
                }

            return render_template('modificarExcel.html', data = dataModificarExcel)
            
    
    return 'Error al enviar el formulario'


            
@app.route('/submit_form_modificar_p2', methods=['POST'])
def submit_form_modificar_p2():
    conjutoFilasAgregar = []
    filasAgregar = []

    if request.method == 'POST':
        id_excel = request.form['id_excel']
        nombre_hoja = request.form['nombre_hoja'].lower()
        accion = request.form['accion']
        
        

        if accion == 'agregar':
            nombre_gasto = request.form.getlist('nombre_gasto')
            precio_gasto = request.form.getlist('precio_gasto')
            categoria_gasto = request.form.getlist('categoria_gasto')


            for nombre, precio, categoria in zip(nombre_gasto, precio_gasto, categoria_gasto):
                nombreCategoria = categoria.lower() + '-' + nombre.lower()
                filasAgregar.append(nombreCategoria)
                filasAgregar.append(precio.lower())
                conjutoFilasAgregar.append(filasAgregar.copy())
                filasAgregar.clear()
                
            try:
                googleSheet.agregarNuevasFilas(id_excel, nombre_hoja, conjutoFilasAgregar, cliente)

                dataModificarExcel = {
                        'estado': '200',
                        'error': '',
                        'siguienteNivel': '',
                        'excelId': '',
                        'accion': 'agregar',
                        'nombreHojaCalculo': '',
                    
                }

                session['data'] = dataModificarExcel

                return redirect(url_for('index'))
                #return render_template('index.html', data = dataModificarExcel)
            
            except Exception as e:
                print(f'Ocurrio un error al intentar agregar nuevas filas. ERROR => {e}')
                dataModificarExcel = {
                    'estado': '',
                    'error': '',
                    'siguienteNivel': '',
                    'excelId': '',
                    'accion': '',
                    'nombreHojaCalculo': '',
                    
                }
                return render_template('index.html', data = dataModificarExcel)
                
        elif accion == 'eliminar':
            lista_gasto = request.form['lista_gastos']
            array_lista_gastos = ast.literal_eval(lista_gasto)

            lista_posicion_gasto = request.form.getlist('gasto')

            #Explicacion sintaxis nueva_lista = [expresion for elemento in lista]
            lista_posicion_gasto = [int(pos) for pos in lista_posicion_gasto]
            
            try:
                print(lista_posicion_gasto)
                googleSheet.eliminarFilas(id_excel, nombre_hoja, lista_posicion_gasto, cliente)
                if len(lista_posicion_gasto) == 0:
                    dataModificarExcel = {
                        'estado': '404',
                        'error': 'No ingresaste nada',
                        'siguienteNivel': '2',
                        'excelId': id_excel,
                        'accion': accion,
                        'nombreHojaCalculo': nombre_hoja,
                        'listaGastos': array_lista_gastos
                    
                    }
                    return render_template('modificarExcelPaso2.html', data = dataModificarExcel)
                else:
                    dataModificarExcel = {
                        'estado': '200',
                        'error': '',
                        'siguienteNivel': '1',
                        'excelId': '',
                        'accion': 'eliminar',
                        'nombreHojaCalculo': '',
                    
                    }
                    session['data'] = dataModificarExcel

                    return redirect(url_for('index'))
                    #return render_template('index.html', data = dataModificarExcel)
            except Exception as e:
                print(f'Ocurrió un error al identificar las filas a elimianr. Error => {e}')  
                dataModificarExcel = {
                    'estado': '404',
                    'error': '',
                    'siguienteNivel': '1',
                    'excelId': '',
                    'accion': 'eliminar',
                    'nombreHojaCalculo': '',
                    
                }
                return render_template('index.html', data = dataModificarExcel)          
        
        else:
            print('error lectura accion')
        


       
        
    
    return 'Error al enviar el formulario'



@app.route('/submit_form_modificar_p3', methods=['POST'])
def submit_form_modificar_p3():

    if request.method == 'POST':
        id_excel = request.form['id_excel']
        nombre_hoja = request.form['nombre_hoja']
        accion = request.form['accion']
        filasEliminar = request.form['filasEliminar'] #Aqui llega como string
        arrayFilasEliminar = ast.literal_eval(filasEliminar)
        posicion_gasto = int(request.form['posicion_gasto'])
        lista_gasto = request.form['lista_gastos']
        array_lista_gastos = ast.literal_eval(lista_gasto)
        try:
            arrayFilasEliminar[posicion_gasto]
        except:
            dataModificarExcel = {
                    'estado': '400',
                    'error': 'Error al realizar la eliminacion, valor fuera del rango',
                    'siguienteNivel': '2',
                    'excelId': id_excel,
                    'accion': accion,
                    'nombreHojaCalculo': nombre_hoja,
                    'listaGastos': array_lista_gastos
                    
                }
            return render_template('modificarExcelPaso2.html', data = dataModificarExcel)
            

        try:
            estadoEliminar = googleSheet.eliminarFilas(id_excel, nombre_hoja, arrayFilasEliminar, posicion_gasto, cliente)
            
            if estadoEliminar == False:
                dataModificarExcel = {
                    'estado': '404',
                    'error': 'Error al eliminar un elemento',
                    'siguienteNivel': '1',
                    'excelId': id_excel,
                    'accion': accion,
                    'nombreHojaCalculo': nombre_hoja,
                    'listaGastos': array_lista_gastos
                    
                }

                return render_template('modificarExcelPaso2.html', data = dataModificarExcel)

            dataModificarExcel = {
                    'estado': '200',
                    'error': '',
                    'siguienteNivel': '1',
                    'excelId': '',
                    'accion': 'eliminar',
                    'nombreHojaCalculo': '',
                    
                }
            
            return render_template('index.html', data = dataModificarExcel)
            
        except Exception as e:
            print('ERROR AL ELIMINAR ESTA VAINA => ', e)
            dataModificarExcel = {
                    'estado': '400',
                    'error': 'Error al realizar la eliminacion',
                    'siguienteNivel': '2',
                    'excelId': id_excel,
                    'accion': accion,
                    'nombreHojaCalculo': nombre_hoja,
                    'listaGastos': array_lista_gastos
                    
                }
            return render_template('modificarExcelPaso2.html', data = dataModificarExcel)
            
    return 'Error al enviar el formulario'



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
    app.run(debug = True, port = os.getenv("PORT", default=5000))