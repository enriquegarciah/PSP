from flask import Flask, jsonify, request, render_template
from config import config
from flask_mysqldb import MySQL 
from flask_cors import CORS

app=Flask(__name__, template_folder='../templates', static_folder='../static')

conexion = MySQL(app)
CORS(app, supports_credentials=True)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/civilizaciones', methods=['GET'])
def listar_civilizaciones():
    try:
        cursor=conexion.connection.cursor()
        sql="SELECT * from civilizaciones"
        cursor.execute(sql)
        datos=cursor.fetchall()
        civilizaciones=[]
        for fila in datos:
            civilizacion={'nombre':fila[0],'especialidad':fila[1],'unidad_unica':fila[2],'tecnologia_unica':fila[3],'imagen':fila[4]}
            civilizaciones.append(civilizacion)        
        return jsonify({'civilizaciones':civilizaciones})

    except Exception as ex:
        return "Error"


@app.route('/civilizaciones/<civilizacion>')
def listar_civilizacion(civilizacion):
    try:
        cursor=conexion.connection.cursor()
        sql="SELECT * FROM civilizaciones WHERE nombre = '{0}'".format(civilizacion)
        cursor.execute(sql)
        datos=cursor.fetchone()
        if datos != None:
            civilizacion={'nombre':datos[0],'especialidad':datos[1],'unidad unica':datos[2],'tecnologia unica':datos[3],'imagen':datos[4]}
            return jsonify({'civilizacion':civilizacion})
    except Exception as ex:
        return "Error"

@app.route('/civilizaciones', methods=['POST'])
def agregar_civilizacion():
    try:
        cursor=conexion.connection.cursor()
        sql="""INSERT INTO civilizaciones (NOMBRE, ESPECIALIDAD, UNIDAD_UNICA, TECNOLOGIA_UNICA, IMAGEN)
        VALUES ('{0}','{1}','{2}','{3}','{4}')""".format(request.json['NOMBRE'],request.json['ESPECIALIDAD'],request.json['UNIDAD_UNICA'],request.json['TECNOLOGIA_UNICA'],request.json['IMAGEN'])
        cursor.execute(sql)
        conexion.connection.commit()
        return "Civilizacion registrada"

    except Exception as ex:
        return "Error"
@app.route('/civilizaciones/<civilizacion>',methods=['DELETE'])
def eliminar_civilizacion(civilizacion):
    try:
        cursor=conexion.connection.cursor()
        sql="DELETE FROM civilizaciones WHERE nombre = '{0}'".format(civilizacion)
        cursor.execute(sql)
        conexion.connection.commit()
        return "Civilizacion eliminada"

    except Exception as ex:
        return "Error"

@app.route('/civilizaciones/<civilizacion>',methods=['PUT'])
def modificar_civilizacion(civilizacion):
    try:
        cursor=conexion.connection.cursor()
        sql="""UPDATE civilizaciones SET ESPECIALIDAD = '{0}', UNIDAD_UNICA = '{1}',TECNOLOGIA_UNICA = '{2}'
         WHERE nombre =  '{3}'""".format(request.json['ESPECIALIDAD'],request.json['UNIDAD_UNICA'],request.json['TECNOLOGIA_UNICA'],civilizacion)
        cursor.execute(sql)
        conexion.connection.commit()
        return "Civilizacion Actualizada"

    except Exception as ex:
        return "Error"


def pagina_no_encontrada(error):
    return """<h1>La pagina que has introducido no existe</h1>
            <h1>:(</h1>"""



if __name__=='__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404,pagina_no_encontrada)
    app.run()