from fastapi import FastAPI
from pydantic import BaseModel

appgd = FastAPI()

lista=[]

class product (BaseModel):
    id_product:int
    detail_product:str
    genre:str
    author:str
    editorial:str
    pages_number:int
    price:int
    amount:int

@appgd.get("/selectproduct") 
def mostrarproduct():
    return lista

@appgd.post("/insertproduct") 
def guardarproduct(datos:product):
    lista.append(datos)
    return {"Mensaje":"Producto registrado"}

@appgd.put("/updateproduct") 
def actualizarproduct(datos:product):
    estado=False
    for item in lista:
        if item.id_product == datos.id_product:
            lista.remove(item)
            lista.append(datos)
            estado=True
            break 
        
    if estado==True:
        return {"Mensaje": "Producto actualizado"}
    else:
        return {"Mensaje": "Producto no encontrado"}

@appgd.delete("/deleteproduct")
def eliminarProduct(id_product):
    estado=False
    for item in lista:
        if item.id_product == int(id_product):
            lista.remove(item)
            estado=True
            break 
        
    if estado==True:
        return {"Mensaje": "Producto eliminado"}
    else:
        return {"Mensaje": "El producto no se ha encontrado"}