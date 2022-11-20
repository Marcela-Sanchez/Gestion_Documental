from fastapi import FastAPI
from pydantic import BaseModel

appgd = FastAPI()

lista=[]

class user(BaseModel):
    id_user:int
    cedula:int
    username:str
    email:str
    pasword:str

@appgd.get("/selectuser") 
def mostraruser():
    return lista

@appgd.post("/insertuser") 
def guardaruser(datos:user):
    lista.append(datos)
    return {"Mensaje":"Usuario almacenado"}

@appgd.put("/updateuser") 
def actualizaruser(datos:user):
    estado=False
    for item in lista:
        if item.id_user == datos.id_user:
            lista.remove(item)
            lista.append(datos)
            estado=True
            break 
        
    if estado==True:
        return {"Mensaje": "Registro actualizado"}
    else:
        return {"Mensaje": "Registro no encontrado"}

@appgd.delete("/deleteuser")
def eliminaruser(id_user):
    estado=False
    msg=""
    for item in lista:
        if item.id_user == int(id_user):
            lista.remove(item)
            estado=True
            break 
        
    if estado:
        return {"Mensaje": "Registro eliminado"}
    else:
        return {"Mensaje": "Registro no encontrado"}