from fastapi import FastAPI
from pydantic import BaseModel

appgd = FastAPI()

lista=[]

class invoice_detail (BaseModel):
    id_invoiceDetail:int
    id_product:int
    quiantitye:int
    unit_price:int
    date:int

    
@appgd.get("/selectinvoiceDetail") 
def mostrarinvoiceDetail():
    return lista

@appgd.post("/insertinvoiceDetail") 
def guardarinvoiceDetail(datos:invoice_detail):
    lista.append(datos)
    return {"Mensaje":"Detalles de la Factura guardados"}

@appgd.put("/updateinvoiceDetail") 
def actualizarinvoiceDetail(datos:invoice_detail):
    estado=False
    for item in lista:
        if item.id_invoiceDetail == datos.id_invoiceDetail:
            lista.remove(item)
            lista.append(datos)
            estado=True
            break 
        
    if estado==True:
        return {"Mensaje": "Detalles de la factura actualizados"}
    else:
        return {"Mensaje": "Los detalles de la factura no existen"}

@appgd.delete("/deleteinvoiceDetail")
def eliminarinvoiceDetail(id_invoiceDetail):
    estado=False
    for item in lista:
        if item.id_invoiceDetail == int(id_invoiceDetail):
            lista.remove(item)
            estado=True
            break 
        
    if estado==True:
        return {"Mensaje": "Detalles de la factura eliminados"}
    else:
        return {"Mensaje": "Los detalles de la factura no existen"}