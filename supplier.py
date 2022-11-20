from fastapi import FastAPI
from pydantic import BaseModel

appgd = FastAPI()

lista=[]

class supplier(BaseModel):
    id_supplier:int
    NIT:int
    suppliername:str
    amount:int
    

@appgd.get("/selectsupplier") 
def mostrarsupplier():
    return lista

@appgd.post("/insertsupplier") 
def guardarsupplier(datos:supplier):
    lista.append(datos)
    return {"Mensaje":"Proveedor registrado"}

@appgd.put("/updatesupplier") 
def actualizarsupplier(datos:supplier):
    estado=False
    for item in lista:
        if item.id_supplier == datos.id_supplier:
            lista.remove(item)
            lista.append(datos)
            estado=True
            break 
        
    if estado==True:
        return {"Mensaje": "Proveedor actualizado"}
    else:
        return {"Mensaje": "Proveedor no encontrado"}

@appgd.delete("/deletesupplier")
def eliminarsupplier(id_supplier):
    estado=False
    for item in lista:
        if item.id_supplier == int(id_supplier):
            lista.remove(item)
            estado=True
            break 
        
    if estado==True:
        return {"Mensaje": "Proveedor eliminado"}
    else:
        return {"Mensaje": "Proveedor no encontrado"}