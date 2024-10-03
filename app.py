from fastapi import FastAPI
import mysql.connector
import schemas

app = FastAPI()

host_name = "52.204.168.191"
port_number = "8008" #TETASSSSSSSS
user_name = "root"
password_db = "utec"
database_name = "bd_api_python" 

@app.get("/")
def get_echo_test():
    return {"message": "Echo Test OK"}

# Get all profesores
@app.get("/profesores")
def get_employees():
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Profesor")
    result = cursor.fetchall()
    cursor.close()
    mydb.close()
    return {"Profesor": result}

# Anadir un nuevo profesor
@app.post("/profesores")
def add_profesor(item:schemas.Item):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    nombre = item.nombre
    especialidad = item.especialidad
    dni = item.dni
    telefono = item.telefono
    cursor = mydb.cursor()
    sql = "INSERT INTO Profesor (nombre, especialidad, dni, telefono) VALUES (%s, %s, %s, %s)"
    val = (nombre,especialidad,dni,telefono)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Profesor added successfully"}