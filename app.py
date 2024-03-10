from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from models import empleado
import pymysql.cursors

app = Flask(__name__)

def connection_mysql():
    connection = pymysql.connect (host='localhost', port=3307, user='root',password='',database='proyectos_cul',cursorclass=pymysql.cursors.DictCursor)
    return connection

@app.route('/usuarios', methods=["POST"] )
def create():
      
    data = request.get_json ()
    connection = connection_mysql()
    
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (NOMBRE,CC,EMAIL) VALUES (%s,%s,%s)"
            cursor. execute(sql, (data ['NOMBRE'], data ['CC'], data['EMAIL']))
        connection.commit()

    return jsonify({
        'message': 'Datos creados de manera exitosa'
    }), 201
 
@app.route('/usuarios', methods=["GET"] )
def list():
    connection = connection_mysql()

    with connection.cursor() as cursor:
    
            sql = 'SELECT * FROM users'
            cursor. execute(sql) 
            
            result = cursor.fetchall()

    return jsonify({
'datos': result
}), 200

@app.route('/update/<id>', methods=['PUT'])
def update(id):

    data = request.json
    
    connection = connection_mysql()
    cursor = connection.cursor()

    cursor.execute ("UPDATE users SET NOMBRE = %s, CC = %s, EMAIL = %s WHERE id = %s",
    (data ['NOMBRE'], data ['CC'], data['EMAIL'],id))

    connection.commit()
    return jsonify({'mensaje': "usuario actualizado exitosamente"})

@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):

    connection = connection_mysql()
    cursor = connection.cursor()

    cursor.execute('''DELETE FROM users WHERE id = %s''', (id,))
    connection.commit()
    return jsonify({'message': 'Datos eliminados de manera correcta'})
   

if __name__ == '__main__':
        app.run(debug=True)
