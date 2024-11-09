from controlador.controlProductos import Control
from vista.ui import Ui
from carga_or_creator_or_find import Creator_Productos,Load_archivo,Tipo_product,Sobreescribir_product
from tkinter import Tk


def funcion_auxiliar_del_main(orden,productorigin = None):
 carga = Load_archivo()
 control = Control(carga)
  
 if "Agregar producto" in orden:
  producto = orden["Agregar producto"]
  producto = Creator_Productos(producto)
  if producto:
   control.AggProductos(producto)
  else:
   print("error")
   return False
  
 elif "Buscar nombres producto" in orden:
  values_return=[]
  nombre = orden["Buscar nombres producto"]
  lista_nombres= control.Look_list_product()
  
  for nombres in lista_nombres:
   nombres = str(nombres)
   if nombre in nombres:
    values_return.append(nombres)
  return values_return
 
 elif "Buscar productos" in orden:
  nombre = orden["Buscar productos"]
  producto = control.FindProduct(nombre)
  if producto:
   return producto
  else:
   return False
  
 elif "Tipo de productos" in orden:
  product = orden["Tipo de productos"]
  return Tipo_product(product)
 
 elif "Actualizar productos" in orden:
  producto = orden["Actualizar productos"]
  producto = Creator_Productos(producto)
  producto = Sobreescribir_product(productorigin,producto)
  if producto:
   control.Actualizacion(producto)
  else:
   print("error")
 elif "Borrar" in orden:
  nombre = orden["Borrar"]
  control.Borrar_product(nombre)
  return True
 
 return True

carga = Load_archivo()
archivo = False
if carga:
 archivo = True
else:
 archivo= False
 
root = Tk()
app = Ui(root,funcion_auxiliar_del_main,archivo)
ejecucion =app.Principal_Windows()

root.mainloop()



