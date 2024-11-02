from tkinter import Tk,Label,Entry,Button,Frame,messagebox,StringVar

class EntryVacios(Exception):
 """excepcion personalizada para los entry vacios"""
 pass

class Ui():
 def __init__(self,root,callback):
  self.color_fond="#2E2E2E"
  self.anch = "1950"
  self.altura = "1400"
  self.root = root
  self.root.title("ALMACEN DE PRODUCTOS")
  self.root.config(bg=self.color_fond)

  self.frame_base = Frame(width= self.anch, height=self.altura)
  self.frame_base.config( bg=self.color_fond)
  self.frame_base.pack()

  self.callback = callback

#metodos simples
 def __Clear(self):
  for widget in self.frame_base.winfo_children():
   widget.destroy()

 def __Salir(self):
  if messagebox.askyesno("SALIR","Desea salir de nuestro entorno de almacenamiento"):
   self.root.quit()

 def __Regreso (self,window):
  self.__Clear()
  ejecutar = window()

 def __Guardar(self,orden):
  try:
   if "Agregar producto" in orden:
    tipo = orden["Agregar producto"]["tipo"]
    nombre = orden["Agregar producto"]["nombre"]
    if nombre.get():
     nombre = str(nombre.get())
     print(nombre)
    else:
     raise EntryVacios()

    if tipo == "Productos_contables":
     try:
      cantidad = orden["Agregar producto"]["cantidad"]
      precio =orden["Agregar producto"]["precio_x_unidad"]
      if cantidad.get():
       cantidad = int(cantidad.get())
      else:
       raise EntryVacios()
      
      if precio.get():
       precio = float(precio.get())
      else:
       precio = None
 
      orden["Agregar producto"] = {"tipo":tipo,nombre:{'nombre':nombre,'cantidad':cantidad,
            'precio_x_unidad':precio}}

     except EntryVacios:messagebox.showerror("Error De Guardado", "Se debe registrar la cantidad del producto")
     except ValueError:messagebox.showerror("Error De Guardado", "La cantidad y el precio deben ser numeros no letras")

    if tipo == "Producto_liquido":
      cantidad_de_contenedores_llenos = orden["Agregar producto"]["cantidad_de_contenedores_llenos"]
      if cantidad_de_contenedores_llenos.get():
       cantidad_de_contenedores_llenos = int(cantidad_de_contenedores_llenos.get())
      else:
       raise EntryVacios()
      
      cantidad_de_liquido_en_contenedores_no_llenos_entry = orden["Agregar producto"]\
        ["cantidad_de_liquido_en_contenedores_no_llenos"]
      if cantidad_de_liquido_en_contenedores_no_llenos.get():
       cantidad_de_liquido_en_contenedores_no_llenos = int(cantidad_de_liquido_en_contenedores_no_llenos.get())
      else:
       cantidad_de_liquido_en_contenedores_no_llenos = None
      
      if precio_del_contenedor.get():
       precio_del_contenedor = precio_del_contenedor.get()
      else:
       precio_del_contenedor = None
      
      if cantidad_de_contenedores_llenos.get():
       cantidad_de_contenedores_llenos = cantidad_de_contenedores_llenos.get()
      else:
       raise EntryVacios()
      
      orden["Agregar producto"] =  {"tipo":"Producto_liquido",nombre:{"nombre":nombre,
            "cantidad_de_contenedores_llenos":cantidad_de_contenedores_llenos,
            "cantidad_de_liquido_x_contenedor":cantidad_de_liquido_x_contenedor_entry,
            "peso_total_de_contenedores_no_llenos":cantidad_de_liquido_en_contenedores_no_llenos_entry,
            "precio_por_peso_entry":precio_del_liquido_entry,
            "precio_por_contenedor_entry":precio_del_contenedor,
            "pesaje_total_del_producto_entry":cantidad_de_liquido_total_entry}}      

     

    if self.callback(orden) is True:
     messagebox.showinfo("Guardado Exitoso", "El producto a sido guardado exitosamente")
     self.__Regreso(self.Clasificator_Product)
    
  except EntryVacios:messagebox.showerror("Error De Guardado", "El producto debe tener un nombre")

#metodos complejos
 def Principal_Windows(self):
     #texto inicial
  texto_superior= Label(self.frame_base,text= "ALMACEN DE PRODUCTOS")
  texto_superior.config(bg="#2E2E2E",fg= "white",font=("Arial",69))
  texto_superior.grid(column=0,row=0,ipady=20,pady= 50,columnspan=7)

    #botones
  agregar_productos= Button(self.frame_base,text="Agregar Productos",command=self.Clasificator_Product)
  agregar_productos.config(fg="white",bg="green",font=("Arial",25))
  agregar_productos.config(width="17",height="-2")
  agregar_productos.grid(column=0,row=1,ipady=5,ipadx=3,pady=10)

  actualizar_productos= Button(self.frame_base,text="Actualizar Productos")
  actualizar_productos.config(fg="white",bg="black",font=("Arial",25))
  actualizar_productos.config(width="18",height="-2")
  actualizar_productos.grid(column=0,row=2,pady=10)
    
    #boton de buscar cierto producto
  look_producto = Button(self.frame_base,text="Buscar Productos")
  look_producto.config(fg="white",bg="blue",font=("Arial",25))
  look_producto.config(width="18",height="-2")
  look_producto.grid(column=0,row=3,pady=10)

  configuration = Button(self.frame_base,text="Configuracion",font=("Arial",25),command= self.__Salir)
  configuration.config(fg="white",bg="red")
  configuration.config(width="18",height="-2")
  configuration.grid(column=0,row=5,pady=10)

  salir = Button(self.frame_base,text="Salir",font=("Arial",25),command= self.__Salir)
  salir.config(fg="white",bg="red")
  salir.config(width="18",height="-2")
  salir.grid(column=0,row=5,pady=10)

 def Clasificator_Product(self):


  borrar = self.__Clear()
  frase_superior= Label(self.frame_base,text= "Nuevo Producto")
  frase_superior.config(bg="#2E2E2E",fg= "white",font=("Arial",79))
  frase_superior.grid(column=0,row=0,ipady=20,padx = 125,pady= 50,columnspan=7)

  #boton del producto contable
  buton_productoC = Button(self.frame_base,text= "Productos Contables",command= lambda:self.New_producto(1))
  buton_productoC.config(bg="blue",fg= "black",font=("Arial",25))
  buton_productoC.config(width="17",height="-2")
  buton_productoC.grid(column=0,row=1,ipady=5,ipadx=3,pady=10,padx=10)

  #boton del producto x pesaje
  buton_productoXpeso = Button(self.frame_base,text= "Productos por pesaje",command= lambda:self.New_producto(2))
  buton_productoXpeso.config(bg="white",fg= "black",font=("Arial",25))
  buton_productoXpeso.config(width="17",height="-2")
  buton_productoXpeso.grid(column=1,row=1,ipady=5,ipadx=3,pady=10,padx=10)

  #boton del producto liquidos
  buton_producto_liquidos = Button(self.frame_base,text= "Productos liquidos",command= lambda:self.New_producto(3))
  buton_producto_liquidos.config(bg="green",fg= "black",font=("Arial",25))
  buton_producto_liquidos.config(width="17",height="-2")
  buton_producto_liquidos.grid(column=2,row=1,ipady=5,ipadx=3,pady=10,padx=10)

  #boton para regresar
  buton_back = Button(self.frame_base,text= "Regresar",command= lambda:self.__Regreso(self.Principal_Windows))
  buton_back.config(bg="red",fg= "black",font=("Arial",25))
  buton_back.config(width="17",height="-2")
  buton_back.grid(column=1,row=2,ipady=5,ipadx=3,pady=10,padx=10)

 def New_producto(self,num):

  tipo_producto = StringVar()
  self.__Clear()

  #nombre
  name_label = Label(self.frame_base,text="Nombre del producto :")
  name_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
  name_label.grid(column=0,row=1,pady=10,padx=0)
  name_entry = Entry(self.frame_base)
  name_entry.config(font=("Arial",15))
  name_entry.grid(column=1,row=1,pady=10,padx=0)

  if num ==1:
   tipo_producto.set("Producto Contable")

   #cantidad
   cantidad_label= Label(self.frame_base,text="Cantidad :")
   cantidad_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
   cantidad_label.grid(column=0,row=2,pady=10)
   cantidad_entry = Entry(self.frame_base)
   cantidad_entry.config(font=("Arial",15))
   cantidad_entry.grid(column=1,row=2,pady=10)

   #Precio
   precio_label= Label(self.frame_base,text="Precio por producto :")
   precio_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
   precio_label.grid(column=0,row=3,pady=10)
   precio_entry = Entry(self.frame_base)
   precio_entry.config(font=("Arial",15))
   precio_entry.grid(column=1,row=3,pady=10)
   fila= 4

  elif num == 2:   
   tipo_producto.set("Producto por Pesaje")

  #cantidad de contenedores 
   cantidad_de_contenedores_label= Label(self.frame_base,text="Cantidad de contenedores :")
   cantidad_de_contenedores_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
   cantidad_de_contenedores_label.grid(column=0,row=2,pady=10)
   cantidad_de_contenedores_entry = Entry(self.frame_base)
   cantidad_de_contenedores_entry.config(font=("Arial",15))
   cantidad_de_contenedores_entry.grid(column=1,row=2,pady=10)

   #peso de contenedor 
   peso_del_contenedor_label= Label(self.frame_base,text="peso del contenedor :")
   peso_del_contenedor_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
   peso_del_contenedor_label.grid(column=0,row=3,pady=10)
   peso_del_contenedor_entry = Entry(self.frame_base)
   peso_del_contenedor_entry.config(font=("Arial",15))
   peso_del_contenedor_entry.grid(column=1,row=3,pady=10)

   #pesaje_total_en_contenedores_no_llenos
   pesaje_total_en_contenedores_no_llenos_label= Label(self.frame_base,text="pesaje total de los contenedores no llenos :")
   pesaje_total_en_contenedores_no_llenos_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
   pesaje_total_en_contenedores_no_llenos_label.grid(column=0,row=4,pady=10)
   pesaje_total_en_contenedores_no_llenos_entry = Entry(self.frame_base)
   pesaje_total_en_contenedores_no_llenos_entry.config(font=("Arial",15))
   pesaje_total_en_contenedores_no_llenos_entry.grid(column=1,row=4,pady=10)
   
   #pesaje_total_del_producto 
   pesaje_total_del_producto_label= Label(self.frame_base,text="pesaje total del producto :")
   pesaje_total_del_producto_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
   pesaje_total_del_producto_label.grid(column=0,row=5,pady=10)
   pesaje_total_del_producto_entry = Entry(self.frame_base)
   pesaje_total_del_producto_entry.config(font=("Arial",15))
   pesaje_total_del_producto_entry.grid(column=1,row=5,pady=10)            

  #precio_por_peso 
   precio_por_peso_label= Label(self.frame_base,text="precio por pesaje :")
   precio_por_peso_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
   precio_por_peso_label.grid(column=0,row=6,pady=10)
   precio_por_peso_entry = Entry(self.frame_base)
   precio_por_peso_entry.config(font=("Arial",15))
   precio_por_peso_entry.grid(column=1,row=6,pady=10)

   #precio_por_contenedor
   precio_por_contenedor_label= Label(self.frame_base,text="precio por contenedor :")
   precio_por_contenedor_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
   precio_por_contenedor_label.grid(column=0,row=7,pady=10)
   precio_por_contenedor_entry = Entry(self.frame_base)
   precio_por_contenedor_entry.config(font=("Arial",15))
   precio_por_contenedor_entry.grid(column=1,row=7,pady=10)            
   fila = 8

  else:  
   tipo_producto.set("Productos Liquidos")

   #cantidad de liquido de cada contenedor lleno
   cantidad_de_liquido_x_contenedor_label= Label(self.frame_base,text="Cantidad de liquido por contenedor lleno :")
   cantidad_de_liquido_x_contenedor_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
   cantidad_de_liquido_x_contenedor_label.grid(column=0,row=2,pady=10)
   cantidad_de_liquido_x_contenedor_entry = Entry(self.frame_base)
   cantidad_de_liquido_x_contenedor_entry.config(font=("Arial",15))
   cantidad_de_liquido_x_contenedor_entry.grid(column=1,row=2,pady=10)

    #cantidad de contenedores llenos
   cantidad_de_contenedores_llenos_label= Label(self.frame_base,text="Cantidad de contenedores llenos :")
   cantidad_de_contenedores_llenos_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
   cantidad_de_contenedores_llenos_label.grid(column=0,row=3,pady=10)
   cantidad_de_contenedores_llenos_entry = Entry(self.frame_base)
   cantidad_de_contenedores_llenos_entry.config(font=("Arial",15))
   cantidad_de_contenedores_llenos_entry.grid(column=1,row=3,pady=10)

   #cantidad de liquido en otros contenedores no llenos
   cantidad_de_liquido_en_contenedores_no_llenos_label= Label(self.frame_base,text="Cantidad de liquido en otros contenedores no llenos :")
   cantidad_de_liquido_en_contenedores_no_llenos_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
   cantidad_de_liquido_en_contenedores_no_llenos_label.grid(column=0,row=4,pady=10)
   cantidad_de_liquido_en_contenedores_no_llenos_entry = Entry(self.frame_base)
   cantidad_de_liquido_en_contenedores_no_llenos_entry.config(font=("Arial",15))
   cantidad_de_liquido_en_contenedores_no_llenos_entry.grid(column=1,row=4,pady=10)
   
   #cantidad de liqido total
   cantidad_de_liquido_total_label= Label(self.frame_base,text="Cantidad de liquido total :")
   cantidad_de_liquido_total_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
   cantidad_de_liquido_total_label.grid(column=0,row=5,pady=10)
   cantidad_de_liquido_total_entry = Entry(self.frame_base)
   cantidad_de_liquido_total_entry.config(font=("Arial",15))
   cantidad_de_liquido_total_entry.grid(column=1,row=5,pady=10)

   #precio del liquido
   precio_por_contenedor_label= Label(self.frame_base,text="Precio por contenedor lleno :")
   precio_por_contenedor_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
   precio_por_contenedor_label.grid(column=0,row=6,pady=10)
   precio_por_contenedor_entry = Entry(self.frame_base)
   precio_por_contenedor_entry.config(font=("Arial",15))
   precio_por_contenedor_entry.grid(column=1,row=6,pady=10)

   #Precio por liquido
   precio_del_liquido_label= Label(self.frame_base,text="Precio del liquido :")
   precio_del_liquido_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
   precio_del_liquido_label.grid(column=0,row=7,pady=10)
   precio_del_liquido_entry = Entry(self.frame_base)
   precio_del_liquido_entry.config(font=("Arial",15))
   precio_del_liquido_entry.grid(column=1,row=7,pady=10)

   fila = 8

#frase que identifica el tipo de producto
  frase_superior= Label(self.frame_base,textvariable= tipo_producto)
  frase_superior.config(bg="#2E2E2E",fg= "white",font=("Arial",79))
  frase_superior.grid(column=0,row=0,ipady=20,padx = 125,pady= 50,columnspan=7)

  # boton guardado
  save_button = Button(self.frame_base,text = "Guardar Producto")
  save_button.config(bg="blue",font=("Arial",15))
  save_button.grid(column=0,row=fila,padx=10)

  #boton regresar
  atras_button = Button(self.frame_base,text = "Regresar",command=lambda:self.__Regreso(self.Clasificator_Product))
  atras_button.config(bg="red",font=("Arial",15))
  atras_button.grid(column=1,row=fila,padx=10)

  if num ==1:
   producto = {"tipo":"Productos_contables","nombre":name_entry,"cantidad":cantidad_entry,
               "precio_x_unidad":precio_entry}

  elif num ==2:
   producto = {"tipo":"Producto_x_pesaje","nombre":name_entry,
               "cantidad_de_contenedores_llenos":cantidad_de_contenedores_entry,
               "peso_del_contenedor":peso_del_contenedor_entry,
               "peso_total_de_contenedores_no_llenos":pesaje_total_en_contenedores_no_llenos_entry,
               "precio_por_peso_entry":precio_por_peso_entry,
               "precio_por_contenedor_entry":precio_por_contenedor_entry,
               "pesaje_total_del_producto_entry":pesaje_total_del_producto_entry}

  else:
   producto =  {"tipo":"Producto_liquido","nombre":name_entry,
               "cantidad_de_contenedores_llenos":cantidad_de_contenedores_llenos_entry,
               "cantidad_de_liquido_x_contenedor":cantidad_de_liquido_x_contenedor_entry,
               "peso_total_de_contenedores_no_llenos":cantidad_de_liquido_en_contenedores_no_llenos_entry,
               "precio_por_peso_entry":precio_del_liquido_entry,
               "precio_por_contenedor_entry":precio_por_contenedor_entry,
               "pesaje_total_del_producto_entry":cantidad_de_liquido_total_entry}

  orden = {"Agregar producto":producto}      
  save_button.config(command=lambda : self.__Guardar(orden))
