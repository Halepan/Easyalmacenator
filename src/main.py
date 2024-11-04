from controlador.models.productos import Productos_contables,Producto_x_pesaje,Producto_liquido
from controlador.models.moneda import Moneda
from controlador.models.unidadadMedida import Unidades_Medida
from controlador.controlProductos import Control
from vista.ui import Ui
from carga_or_creator_or_find import Creator_Productos,Load_archivo
from tkinter import Tk

def funcion_auxiliar_del_main(orden):
 carga = Load_archivo()
 control = Control(carga)
 if "Agregar producto" in orden:
  producto = orden["Agregar producto"]
  print(producto)
  producto = Creator_Productos(producto)
  if producto:
   control.AggProductos(producto)
  else:
   print("error")
   return False
 elif "Buscar producto" in orden:
  values_return=[]
  nombre = orden["Buscar producto"]
  lista_nombres= control.Look_list_product()
  
  for nombres in lista_nombres:
   nombres = str(nombres)
   if nombre in nombres:
    values_return.append(nombres)
  return values_return
 return True


root = Tk()
app = Ui(root,funcion_auxiliar_del_main)
ejecucion =app.Principal_Windows()

root.mainloop()



