from fastapi import FastAPI
from pydantic import BaseModel

appgd = FastAPI()

lista=[]

class inventory(BaseModel):
    id_inventory:int
    id_product:int
    detail_product:str
    supplier:str
    amount:int
    

@appgd.get("/selectinventory") 
def mostrarinventory():
    return lista

@appgd.post("/insertinventory") 
def guardarinventory(datos:inventory):
    lista.append(datos)
    return {"Mensaje":"inventario modificado"}

@appgd.put("/updateinventory") 
def actualizarinventory(datos:inventory):
    estado=False
    for item in lista:
        if item.id_inventory== datos.id_inventory:
            lista.remove(item)
            lista.append(datos)
            estado=True
            break 
        
    if estado==True:
        return {"Mensaje": "Inventario actualizado"}
    else:
        return {"Mensaje": "Producto no encontrado"}

@appgd.delete("/deleteinventory")
def eliminarinventory(id_inventory):
    estado=False
    for item in lista:
        if item.id_inventory == int(id_inventory):
            lista.remove(item)
            estado=True
            break 
        
    if estado==True:
        return {"Mensaje": "Producto eliminado"}
    else:
        return {"Mensaje": "Producto no encontrado"}