from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # https://fastapi.tiangolo.com/tutorial/cors/#use-corsmiddleware
import mysql.connector
import schemas

app = FastAPI()

origins = ['*'] # Permite que el Api Rest se consuma desde cualquier origen

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

host_name = "172.31.87.103" # IPv4 privada de "MV Bases de Datos"
port_number = "8005"
user_name = "root"
password_db = "pass_personas"
database_name = "DB_Personas"

# Get echo test for load balancer's health check
@app.get("/")
def get_echo_test():
    return {"message": "Echo Test OK"}

# Get all employees
@app.get("/personas")
def get_personas():
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM personas")
    result = cursor.fetchall()
    cursor.close()
    mydb.close()
    return {"employees": result}

# Get an employee by ID
@app.get("/personas/{id}")
def get_persona(codigo_persona: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM peronas WHERE codigo_persona = {codigo_persona}")
    result = cursor.fetchone()
    cursor.close()
    mydb.close()
    return {"persona": result}

# Add a new employee
@app.post("/personas")
def add_persona(item:schemas.Persona):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  

    tipo_persona = item.tipo_persona
    indicador_lista_negra = item.indicador_lista_negra
    nacionalidad = item.nacionalidad
    pais_procedencia = item.pais_procedencia

    cursor = mydb.cursor()
    sql = "INSERT INTO personas (tipo_persona, indicador_lista_negra, necionalidad, pais_procedencia) VALUES (%s, %s, %s, %s)"
    val = (tipo_persona, indicador_lista_negra, nacionalidad, pais_procedencia)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Persona added successfully"}

# Modify an employee
@app.put("/employees/{id}")
def update_employee(codigo_persona:int, item:schemas.Persona):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    tipo_persona = item.tipo_persona
    indicador_lista_negra = item.indicador_lista_negra
    cursor = mydb.cursor()
    sql = "UPDATE personas set tipo_persona=%s, indicador_lista_negra=%s where codigo_persona=%s"
    val = (tipo_persona, indicador_lista_negra, codigo_persona)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Employee modified successfully"}

# Delete an employee by ID
@app.delete("/employees/{id}")
def delete_employee(codigo_persona: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM personas WHERE codigo_persona = {codigo_persona}")
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Employee deleted successfully"}