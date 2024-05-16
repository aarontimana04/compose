from fastapi import FastAPI
import mysql.connector
from pydantic import BaseModel

app = FastAPI()

host_name = "100.28.85.79"
port_number = "8005"
user_name = "root"
password_db = "utec"
database_name = "bd_api_shared"
schema_name = "api_clases"

class Item(BaseModel):
    name: str
    id_alumno: int
    id_profesor: int
    degree: int

# Get all classes
@app.get("/classes")
def get_classes():
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM {schema_name}.clases")  # Utilizar el esquema específico
    result = cursor.fetchall()
    mydb.close()
    return {"classes": result}

# Get a class by ID
@app.get("/classes/{id}")
def get_class(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM {schema_name}.clases WHERE id = {id}")  # Utilizar el esquema específico
    result = cursor.fetchone()
    mydb.close()
    return {"class": result}

# Add a new class
@app.post("/classes")
def add_class(item: Item):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    sql = f"INSERT INTO {schema_name}.clases (name, id_alumno, id_profesor, degree) VALUES (%s, %s, %s, %s)"  # Utilizar el esquema específico
    val = (item.name, item.id_alumno, item.id_profesor, item.degree)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Class added successfully"}

# Modify a class
@app.put("/classes/{id}")
def update_class(id: int, item: Item):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    sql = f"UPDATE {schema_name}.clases SET name = %s, id_alumno = %s, id_profesor = %s, degree = %s WHERE id = %s"  # Utilizar el esquema específico
    val = (item.name, item.id_alumno, item.id_profesor, item.degree, id)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Class modified successfully"}

# Delete a class by ID
@app.delete("/classes/{id}")
def delete_class(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM {schema_name}.clases WHERE id = {id}")  # Utilizar el esquema específico
    mydb.commit()
    mydb.close()
    return {"message": "Class deleted successfully"}
