from fastapi import FastAPI
from pydantic import BaseModel

appgd = FastAPI()

lista=[]

class client (BaseModel):
    id_client:int
    cedula:int
    clientname:str
    city:str
    phone:int
    date:int

@appgd.get("/selectclient") 
def mostrarclient():
    return lista

@appgd.post("/insertclient") 
def guardarclient(datos:client):
    lista.append(datos)
    return {"Mensaje":"Cliente registrado"}

@appgd.put("/updateclient") 
def actualizarclient(datos:client):
    estado=False
    for item in lista:
        if item.id_client == datos.id_client:
            lista.remove(item)
            lista.append(datos)
            estado=True
            break 
        
    if estado==True:
        return {"Mensaje": "Cliente actualizado"}
    else:
        return {"Mensaje": "Cliente no encontrado"}


@appgd.delete("/deleteclient")
def eliminarclient(id_client):
    estado=False
    for item in lista:
        if item.id_client == int(id_client):
            lista.remove(item)
            estado=True
            break 
        
    if estado:
        return {"Mensaje": "Cliente eliminado"}
    else:
        return {"Mensaje": "Cliente no encontrado"}

def test():
    print("hola")