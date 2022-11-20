from fastapi import FastAPI
from pydantic import BaseModel

appgd = FastAPI()

lista=[]

class product_detail (BaseModel):
    id_productDetail:int
    name:str
    description:str
    date:int
   

@appgd.get("/selectproductDetail") 
def mostrarproductDetail():
    return lista

@appgd.post("/insertproductDetail") 
def guardarproductDetail(datos:product_detail):
    lista.append(datos)
    return {"Mensaje":"Detalles del Producto registrados"}

@appgd.put("/updateproductDetail") 
def actualizarproductDetail(datos:product_detail):
    estado=False
    for item in lista:
        if item.id_productDetail == datos.id_productDetail:
            lista.remove(item)
            lista.append(datos)
            estado=True
            break 
        
    if estado==True:
        return {"Mensaje": "Detalles del producto actualizado"}
    else:
        return {"Mensaje": "Los detalles del Producto no se encontraron"}

@appgd.delete("/deleteproductDetail")
def eliminarProductDetail(id_productDetail):
    estado=False
    for item in lista:
        if item.id_productDetail == int(id_productDetail):
            lista.remove(item)
            estado=True
            break 
        
    if estado==True:
        return {"Mensaje": "Los detalles del producto fueron eliminados"}
    else:
        return {"Mensaje": "Los detalles del Producto no se encontraron"}