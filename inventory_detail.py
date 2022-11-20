from fastapi import FastAPI
from pydantic import BaseModel

appgd = FastAPI()

lista=[]

class inventory_detail(BaseModel):
    id_inventoryDetail:int
    product_description:str
    type:str
    date:int
    returns:int
    id_supplier:int
   
    

@appgd.get("/selectinventoryDetail") 
def mostrarinventoryDetail():
    return lista

@appgd.post("/insertinventoryDetail") 
def guardarinventoryDetail(datos:inventory_detail):
    lista.append(datos)
    return {"Mensaje":"Detalle del inventario modificado"}

@appgd.put("/updateinventoryDetail") 
def actualizarinventoryDetail(datos:inventory_detail):
    estado=False
    for item in lista:
        if item.id_inventoryDetail== datos.id_inventoryDetail:
            lista.remove(item)
            lista.append(datos)
            estado=True
            break 
        
    if estado==True:
        return {"Mensaje": "Detalle del inventario actualizado"}
    else:
        return {"Mensaje": "Detalle del inventario no encontrado"}

@appgd.delete("/deleteinventoryDetail")
def eliminarinventoryDetail(id_inventoryDetail):
    estado=False
    for item in lista:
        if item.id_inventoryDetail == int(id_inventoryDetail):
            lista.remove(item)
            estado=True
            break 
        
    if estado==True:
        return {"Mensaje":"Detalle del inventario eliminado"}
    else:
        return {"Mensaje": "Detalle del inventario no encontrado"}