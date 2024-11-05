from tkinter import Label,Entry,Button,Frame,messagebox,StringVar,ttk

class EntryVacios(Exception):
 """excepcion personalizada para los entry vacios de los atributos de los productos"""
 pass

class MEntryVacios(Exception):
 """excepcion personalizada para los entry vacios de las monedas"""
 pass

class UEntryVacios(Exception):
 """excepcion personalizada para los entry   vacios de unidades de medida"""
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
    moneda = orden["Agregar producto"]["moneda"]

    if nombre.get():
     nombre = str(nombre.get())
     print(nombre)
    else:
     raise EntryVacios()

    if tipo == "Productos_contables":
     cantidad = orden["Agregar producto"]["cantidad"]
     precio =orden["Agregar producto"]["precio_x_unidad"]
     if cantidad.get():
      cantidad = int(cantidad.get())
     else:
      raise EntryVacios()
     
     if precio.get():  
      if moneda.get() != "Tipo de moneda":
       precio = {"cantidad":float(precio.get()),"tipo":moneda.get()}
      else:
       raise MEntryVacios()
     else:
      precio = None

     orden["Agregar producto"] = {"tipo":tipo,nombre:{'nombre':nombre,'cantidad':cantidad,
            'precio_x_unidad':precio}}


    if tipo == "Producto_liquido":
     
      cantidad_de_contenedores_llenos = orden["Agregar producto"]["cantidad_de_contenedores_llenos"]
      unidad_de_medida= orden["Agregar producto"]["unidad_de_medida"]
      cantidad_de_liquido_x_contenedor = orden["Agregar producto"]["cantidad_de_liquido_x_contenedor"]
      cantidad_de_liquido_en_contenedores_no_llenos = orden["Agregar producto"]\
        ["cantidad_de_liquido_en_contenedores_no_llenos"]
      precio_del_liquido = orden["Agregar producto"]["precio_del_liquido"]
      precio_del_contenedor= orden["Agregar producto"]["precio_por_contenedor"]
      cantidad_de_liquido_total = orden["Agregar producto"]["cantidad_de_liquido_total"]

      if cantidad_de_contenedores_llenos.get():
       cantidad_de_contenedores_llenos = int(cantidad_de_contenedores_llenos.get())
      else:
       raise EntryVacios()
       
      if cantidad_de_liquido_x_contenedor.get():
       if unidad_de_medida != "Unidad de medida":
        cantidad_de_liquido_x_contenedor = {"cantidad":float(
         cantidad_de_liquido_x_contenedor.get()),
         "unidad de medida":unidad_de_medida.get()}
       else:
        raise UEntryVacios()
      else:
       cantidad_de_liquido_x_contenedor = None

      if cantidad_de_liquido_en_contenedores_no_llenos.get():
       if unidad_de_medida != "Unidad de medida":
        cantidad_de_liquido_en_contenedores_no_llenos = {"cantidad":float(
         cantidad_de_liquido_en_contenedores_no_llenos.get()),
         "unidad de medida":unidad_de_medida.get()}
       else:
        raise UEntryVacios()
      else:
       cantidad_de_liquido_en_contenedores_no_llenos = None

      if precio_del_liquido.get():
       if unidad_de_medida != "Unidad de medida":
        precio_del_liquido = {"cantidad":float(
         precio_del_liquido.get()),
         "unidad de medida":unidad_de_medida.get()}
       else:
        raise MEntryVacios()
      else:
       precio_del_liquido = None
              
      if precio_del_contenedor.get():
       if unidad_de_medida != "Unidad de medida":
        precio_del_contenedor = {"cantidad":float(
         precio_del_contenedor.get()),
         "unidad de medida":unidad_de_medida.get()}
       else:
        raise MEntryVacios()
      else:
       precio_del_contenedor = None
       
      if cantidad_de_liquido_total.get():
       if unidad_de_medida != "Unidad de medida":
        cantidad_de_liquido_total = {"cantidad":float(
         cantidad_de_liquido_total.get()),
         "unidad de medida":unidad_de_medida.get()}
       else:
        raise UEntryVacios()
      else:
       cantidad_de_liquido_total = None
       
      orden["Agregar producto"] =  {"tipo":"Producto_liquido",nombre:{"nombre":nombre,
            "cantidad_de_contenedores_llenos":cantidad_de_contenedores_llenos,
            "cantidad_de_liquido_del_contenedor":cantidad_de_liquido_x_contenedor,
            "cantidad_de_liquido_en_contenedores_no_llenos":cantidad_de_liquido_en_contenedores_no_llenos,
            "precio_x_litros":precio_del_liquido,
            "precio_x_contenedor":precio_del_contenedor,
            "cantidad_liquido_total":cantidad_de_liquido_total}}
             

    if tipo == "Producto_x_pesaje":
     cantidad_de_contenedores_llenos = orden["Agregar producto"]["cantidad_de_contenedores_llenos"]
     unidad_de_medida= orden["Agregar producto"]["unidad_de_medida"]
     cantidad_de_liquido_x_contenedor = orden["Agregar producto"]["peso_del_contenedor"]
     cantidad_de_liquido_en_contenedores_no_llenos = orden["Agregar producto"]\
       ["peso_total_de_contenedores_no_llenos"]
     precio_del_liquido = orden["Agregar producto"]["precio_x_pesaje"]
     precio_del_contenedor= orden["Agregar producto"]["precio_por_contenedor"]
     cantidad_de_liquido_total = orden["Agregar producto"]["pesaje_total_del_producto"]

     if cantidad_de_contenedores_llenos.get():
      cantidad_de_contenedores_llenos = int(cantidad_de_contenedores_llenos.get())
     else:
      raise EntryVacios()
       
     if peso_del_contenedor.get():
      if unidad_de_medida != "Unidad de medida":
       peso_del_contenedor = {"cantidad":float(
        peso_del_contenedor.get()),
        "unidad de medida":unidad_de_medida.get()}
      else:
       raise UEntryVacios()
     else:
      peso_del_contenedor = None

     if peso_total_de_contenedores_no_llenos.get():
      if unidad_de_medida != "Unidad de medida":
       peso_total_de_contenedores_no_llenos = {"cantidad":float(
        peso_total_de_contenedores_no_llenos.get()),
        "unidad de medida":unidad_de_medida.get()}
      else:
       raise UEntryVacios()
     else:
      peso_total_de_contenedores_no_llenos = None

     if precio_x_pesaje.get():
      if unidad_de_medida != "Unidad de medida":
       precio_del_liquido = {"cantidad":float(
        precio_x_pesaje.get()),
        "unidad de medida":unidad_de_medida.get()}
      else:
       raise MEntryVacios()
     else:
      precio_x_pesaje = None
              
     if precio_del_contenedor.get():
      if unidad_de_medida != "Unidad de medida":
       precio_del_contenedor = {"cantidad":float(
        precio_del_contenedor.get()),
        "unidad de medida":unidad_de_medida.get()}
      else:
       raise MEntryVacios()
     else:
      precio_del_contenedor = None
       
     if pesaje_total_del_producto.get():
      if unidad_de_medida != "Unidad de medida":
       pesaje_total_del_producto = {"cantidad":float(
        pesaje_total_del_producto.get()),
        "unidad de medida":unidad_de_medida.get()}
      else:
       raise UEntryVacios()
     else:
      cantidad_de_liquido_total = None
       
     orden["Agregar producto"] =  {"tipo":"Producto_x_pesaje",nombre:{"nombre":nombre,
           "cantidad_de_contenedores_llenos":cantidad_de_contenedores_llenos,
           "peso_del_contenedor":peso_del_contenedor,
           "peso_total_de_contenedores_no_llenos":peso_total_de_contenedores_no_llenos,
           "precio_x_pesaje":precio_x_pesaje,
           "precio_x_contenedor":precio_del_contenedor,
           "pesaje_total_del_producto":pesaje_total_del_producto}}

    if self.callback(orden) is True:
     messagebox.showinfo("Guardado Exitoso", "El producto a sido guardado exitosamente")
     self.__Regreso(self.Clasificator_Product)
    
  except EntryVacios:messagebox.showerror("Error De Guardado", "Se debe registrar un nombre y la cantidad de lotes del producto")
  except ValueError:messagebox.showerror("Error De Guardado", "Excepto el nombre todo lo demas se debe registrar con numeros")
  except MEntryVacios:messagebox.showerror("Error De Guardado", "Si se registro un precio, tambien se debe seleccionar el tipo de moneda")
  except UEntryVacios:messagebox.showerror("Error De Guardado", "Se debe seleccionar el tipo de moneda")

 def __Find(self,event,nombre):
  if nombre.get(): 
   orden = {"Buscar producto":nombre.get()}
   lista_recibida= self.callback(orden)
   print(lista_recibida)
   nombre.config(values = lista_recibida)

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

  actualizar_productos= Button(self.frame_base,text="Actualizar Productos",command=lambda:self.Find_Product("Actualizar productos"))
  actualizar_productos.config(fg="white",bg="black",font=("Arial",25))
  actualizar_productos.config(width="18",height="-2")
  actualizar_productos.grid(column=0,row=2,pady=10)
    
    #boton de buscar cierto producto
  look_producto = Button(self.frame_base,text="Buscar Productos",command=lambda:self.Find_Product("Mostrar productos"))
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
   #estos son los valores que tendra el boton los valores de unidad de medida
   valores = ["Unidad de medida","gramos","kilogramos","onzas","libras", "miligramos", "toneladas"]

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
   #estos son los valores pque tendra el boton de unidad de medida
   valores = ["Unidad de medida","mililitros","litros", "onzas líquidas"]


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

  #boton del tipo de moneda 
  values = ["Tipo de moneda","CUP","USD","MLC"]
  tipo_de_moneda_buton = ttk.Combobox(self.frame_base,values=values,font=("Arial",15))
  tipo_de_moneda_buton.current(0)
  tipo_de_moneda_buton.grid(column=2,row = 1,padx=10)

  #boton de unidades de medida solo para los productos pesajes y los liquidos
  if num ==2 or num== 3:
   unidad_de_medida_buton = ttk.Combobox(self.frame_base,values=valores,font=("Arial",15))
   unidad_de_medida_buton.current(0)
   unidad_de_medida_buton.grid(column=3,row=1,padx= 10)

  if num ==1:
   producto = {"tipo":"Productos_contables","nombre":name_entry,"cantidad":cantidad_entry,
               "precio_x_unidad":precio_entry,"moneda":tipo_de_moneda_buton}

  elif num ==2:
   producto = {"tipo":"Producto_x_pesaje","nombre":name_entry,
               "cantidad_de_contenedores_llenos":cantidad_de_contenedores_entry,
               "peso_del_contenedor":peso_del_contenedor_entry,
               "peso_total_de_contenedores_no_llenos":pesaje_total_en_contenedores_no_llenos_entry,
               "precio_x_pesaje":precio_por_peso_entry,
               "precio_x_contenedor":precio_por_contenedor_entry,
               "pesaje_total_del_producto":pesaje_total_del_producto_entry,
               "moneda":tipo_de_moneda_buton,"unidad_de_medida":unidad_de_medida_buton}

  else:
   producto =  {"tipo":"Producto_liquido","nombre":name_entry,
               "cantidad_de_contenedores_llenos":cantidad_de_contenedores_llenos_entry,
               "cantidad_de_liquido_x_contenedor":cantidad_de_liquido_x_contenedor_entry,
               "cantidad_de_liquido_en_contenedores_no_llenos":cantidad_de_liquido_en_contenedores_no_llenos_entry,
               "precio_del_liquido":precio_del_liquido_entry,
               "precio_por_contenedor":precio_por_contenedor_entry,
               "cantidad_de_liquido_total":cantidad_de_liquido_total_entry,
               "moneda":tipo_de_moneda_buton,"unidad_de_medida":unidad_de_medida_buton}

  orden = {"Agregar producto":producto}      
  save_button.config(command=lambda : self.__Guardar(orden))

 def Find_Product(self,Nextaccion):
  self.__Clear()
  label_principal = Label(self.frame_base,text="Buscar Producto")
  label_principal.config(fg="white",bg="#2E2E2E",font=("Arial",69))
  label_principal.grid(column=0,row=0,pady=20)

  barra_find = ttk.Combobox(self.frame_base,values=[],state="normal",font=("Arial",15))
  barra_find.grid(column=0,row=1,padx=5,pady=10)
  barra_find.bind("<KeyRelease>",lambda event: self.__Find(event,barra_find))

  boton_Buscar = Button(self.frame_base,text="Buscar",
    font=("Arial",12))
  boton_Buscar.config(bg="blue",fg="white")
  boton_Buscar.grid(column=1,row=1,padx=5)

  button_atras=Button(self.frame_base,text="Regresar",
    font=("Arial",12),command=lambda: self.__Regreso(self.Principal_Windows))
  button_atras.config(bg="red",fg="white")
  button_atras.grid(column=1, row=2,pady=10)
