from fastapi import FastAPI
from pydantic import BaseModel

appgd = FastAPI()

lista=[]

class invoice (BaseModel):
    id_invoice:int
    id_user:int
    date: int
    id_client: int
    id_product:int
    detail_invoice:str
    taxes:int
    discount:int
    rented:int
    total:int
    amount:int

@appgd.get("/selectinvoice") 
def mostrarinvoice():
    return lista

@appgd.post("/insertinvoice") 
def guardarinvoice(datos:invoice):
    lista.append(datos)
    return {"Mensaje":"Factura registrado"}

@appgd.put("/updateinvoice") 
def actualizarinvoice(datos:invoice):
    estado=False
    for item in lista:
        if item.id_invoice == datos.id_invoice:
            lista.remove(item)
            lista.append(datos)
            estado=True
            break 
        
    if estado==True:
        return {"Mensaje": "Factura actualizado"}
    else:
        return {"Mensaje": "La factura no existe"}

@appgd.delete("/deleteinvoice")
def eliminarinvoice(id_invoice):
    estado=False
    for item in lista:
        if item.id_invoice == int(id_invoice):
            lista.remove(item)
            estado=True
            break 
        
    if estado==True:
        return {"Mensaje": "Factura eliminada"}
    else:
        return {"Mensaje": "La factura no se ha encontrado"}