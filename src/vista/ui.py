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

class NohayArchivo(Exception):
 """excepcion personalizada para cuando el archivo este vacio"""
 pass

class Ui():
 def __init__(self,root,callback,archivo):
  self.color_fond="#2E2E2E"
  self.anch = "1950"
  self.altura = "1400"
  self.root = root
  self.root.title("ALMACEN DE PRODUCTOS")
  self.root.config(bg=self.color_fond)

  self.frame_base = Frame(self.root,width= self.anch, height=self.altura)
  self.frame_base.config( bg=self.color_fond)
  self.frame_base.pack()

  self.callback = callback
  self.archivo = archivo

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

 def __Guardar(self,orden,key,producto):
  try:
   if key in orden:
    tipo = orden[key]["tipo"]
    nombre = orden[key]["nombre"]
    moneda = orden[key]["moneda"]

    if nombre.get():
     nombre = str(nombre.get())
    else:
     raise EntryVacios()

    if tipo == "Productos_contables":
     cantidad = orden[key]["cantidad"]
     precio = orden[key]["precio_x_unidad"]
     if cantidad.get():
      cantidad = int(cantidad.get())
     else:
      if key == "Agregar producto":
       raise EntryVacios()
      else:
       cantidad = None

     if precio.get():  
      if moneda.get() != "Tipo de moneda":
       precio = {"cantidad":float(precio.get()),"tipo":moneda.get()}
      else:
       raise MEntryVacios()
     else:
      precio = None

     orden[key] = {"tipo":tipo,nombre:{'nombre':nombre,'cantidad':cantidad,
            'precio_x_unidad':precio}}

    if tipo == "Producto_liquido":
     
      cantidad_de_contenedores_llenos = orden[key]["cantidad_de_contenedores_llenos"]
      unidad_de_medida= orden[key]["unidad_de_medida"]
      cantidad_de_liquido_x_contenedor = orden[key]["cantidad_de_liquido_x_contenedor"]
      cantidad_de_liquido_en_contenedores_no_llenos = orden[key]\
        ["cantidad_de_liquido_en_contenedores_no_llenos"]
      precio_del_liquido = orden[key]["precio_del_liquido"]
      precio_del_contenedor= orden[key]["precio_por_contenedor"]
      cantidad_de_liquido_total = orden[key]["cantidad_de_liquido_total"]

      if cantidad_de_contenedores_llenos.get():
       cantidad_de_contenedores_llenos = int(cantidad_de_contenedores_llenos.get())
      else:
       if key == "Agregar producto":
        raise EntryVacios()
       else:
        cantidad_de_contenedores_llenos = None
       
      if cantidad_de_liquido_x_contenedor.get():
       if unidad_de_medida.get() != "Unidad de medida":
        cantidad_de_liquido_x_contenedor = {"cantidad":float(
         cantidad_de_liquido_x_contenedor.get()),
         "unidad_de_medida":unidad_de_medida.get()}
       else:
        raise UEntryVacios()
      else:
       cantidad_de_liquido_x_contenedor = None

      if cantidad_de_liquido_en_contenedores_no_llenos.get():
       if unidad_de_medida.get() != "Unidad de medida":
        cantidad_de_liquido_en_contenedores_no_llenos = {"cantidad":float(
         cantidad_de_liquido_en_contenedores_no_llenos.get()),
         "unidad_de_medida":unidad_de_medida.get()}
       else:
        raise UEntryVacios()
      else:
       cantidad_de_liquido_en_contenedores_no_llenos = None

      if precio_del_liquido.get():
       if moneda.get() != "Unidad de medida":
        precio_del_liquido = {"cantidad":float(
         precio_del_liquido.get()),
         "unidad_de_medida":moneda.get()}
       else:
        raise MEntryVacios()
      else:
       precio_del_liquido = None
              
      if precio_del_contenedor.get():
       if moneda.get() != "Unidad de medida":
        precio_del_contenedor = {"cantidad":float(
         precio_del_contenedor.get()),
         "unidad_de_medida":moneda.get()}
       else:
        raise MEntryVacios()
      else:
       precio_del_contenedor = None
       
      if cantidad_de_liquido_total.get():
       if unidad_de_medida.get() != "Unidad de medida":
        cantidad_de_liquido_total = {"cantidad":float(
         cantidad_de_liquido_total.get()),
         "unidad_de_medida":unidad_de_medida.get()}
       else:
        raise UEntryVacios()
      else:
       cantidad_de_liquido_total = None
       
      orden[key] =  {"tipo":"Producto_liquido",nombre:{"nombre":nombre,
            "cantidad_de_contenedores_llenos":cantidad_de_contenedores_llenos,
            "cantidad_de_liquido_del_contenedor":cantidad_de_liquido_x_contenedor,
            "cantidad_de_liquido_en_contenedores_no_llenos":cantidad_de_liquido_en_contenedores_no_llenos,
            "precio_x_litros":precio_del_liquido,
            "precio_x_contenedor":precio_del_contenedor,
            "cantidad_liquido_total":cantidad_de_liquido_total}}
             
    if tipo == "Producto_x_pesaje":
     cantidad_de_contenedores_llenos = orden[key]["cantidad_de_contenedores_llenos"]
     unidad_de_medida= orden[key]["unidad_de_medida"]
     peso_del_contenedor = orden[key]["peso_del_contenedor"]
     peso_total_de_contenedores_no_llenos = orden[key]\
       ["peso_total_de_contenedores_no_llenos"]
     precio_x_pesaje = orden[key]["precio_x_pesaje"]
     precio_del_contenedor= orden[key]["precio_x_contenedor"]
     pesaje_total_del_producto = orden[key]["pesaje_total_del_producto"]

     if cantidad_de_contenedores_llenos.get():
      cantidad_de_contenedores_llenos = int(cantidad_de_contenedores_llenos.get())
     else:
      if key == "Agregar producto":
       raise EntryVacios()
      else:
       cantidad_de_contenedores_llenos = None
       
     if peso_del_contenedor.get():
      if unidad_de_medida.get() != "Unidad de medida":
       peso_del_contenedor = {"cantidad":int(peso_del_contenedor.get()),
        "unidad_de_medida":unidad_de_medida.get()}
      else:
       raise UEntryVacios()
     else:
      peso_del_contenedor = None

     if peso_total_de_contenedores_no_llenos.get():
      if unidad_de_medida.get() != "Unidad de medida":
       peso_total_de_contenedores_no_llenos = {"cantidad":float(
        peso_total_de_contenedores_no_llenos.get()),
        "unidad_de_medida":unidad_de_medida.get()}
      else:
       raise UEntryVacios()
     else:
      peso_total_de_contenedores_no_llenos = None

     if precio_x_pesaje.get():
      if unidad_de_medida.get() != "Unidad de medida":
       precio_del_liquido = {"cantidad":float(
        precio_x_pesaje.get()),
        "unidad_de_medida":unidad_de_medida.get()}
      else:
       raise MEntryVacios()
     else:
      precio_x_pesaje = None
              
     if precio_del_contenedor.get():
      if unidad_de_medida.get() != "Unidad de medida":
       precio_del_contenedor = {"cantidad":float(
        precio_del_contenedor.get()),
        "unidad_de_medida":unidad_de_medida.get()}
      else:
       raise MEntryVacios()
     else:
      precio_del_contenedor = None
       
     if pesaje_total_del_producto.get():
      if unidad_de_medida != "Unidad de medida":
       pesaje_total_del_producto = {"cantidad":float(
        pesaje_total_del_producto.get()),
        "unidad_de_medida":unidad_de_medida.get()}
      else:
       raise UEntryVacios()
     else:
      pesaje_total_del_producto = None
       
     orden[key] =  {"tipo":"Producto_x_pesaje",nombre:{"nombre":nombre,
           "cantidad_de_contenedores_llenos":cantidad_de_contenedores_llenos,
           "peso_del_contenedor":peso_del_contenedor,
           "peso_total_de_contenedores_no_llenos":peso_total_de_contenedores_no_llenos,
           "precio_x_pesaje":precio_x_pesaje,
           "precio_x_contenedor":precio_del_contenedor,
           "pesaje_total_del_producto":pesaje_total_del_producto}}
     
    if self.callback(orden,producto) is True:
     messagebox.showinfo("Guardado Exitoso", "El producto a sido guardado exitosamente")
     self.archivo = True
     self.__Regreso(self.Clasificator_Product)
    
  except EntryVacios:messagebox.showerror("Error De Guardado", "Se debe registrar un nombre y la cantidad de lotes del producto")
  except ValueError:messagebox.showerror("Error De Guardado", "Excepto el nombre todo lo demas se debe registrar con numeros")
  except MEntryVacios:messagebox.showerror("Error De Guardado", "Si se registro un precio, tambien se debe seleccionar el tipo de moneda")
  except UEntryVacios:messagebox.showerror("Error De Guardado", "Se debe seleccionar una unidad de medida")

 def __Findlistcoincidence(self,event,nombre):
  if nombre.get(): 
   orden = {"Buscar nombres producto":nombre.get()}
   lista_recibida= self.callback(orden)
   nombre.config(values = lista_recibida)

 def __FindAction(self,orden):
  try:
   for key in orden:
    nombre = orden[key] 
   nombre = nombre.get()
   product = self.callback({"Buscar productos":nombre})
   if product:
    if "Actualizar productos" in orden:
      self.Actualizar_product(product)
    elif "Mostrar productos"in orden:
      self.Mostrar_product(product)
   else:
    raise ValueError()
  except ValueError:messagebox.showerror("ERROR DE BUSQUEDA","Al buscar uno de los productos selecciona uno de los productos de la\
  lista para facilitar la busqueda de los productos")
  
 def Actualizar_product(self,product):
  num = self.callback({"Tipo de productos":product})
  self.New_producto(num,product)

 def __Mostrador_de_info(self,num,diccionary,prosedencia):
  match prosedencia:
    case "escribir":
      columna = 2
    case "mostrar":
      columna = 1
  
  match num:
    case 1 :
     varcant = StringVar()
     varprecio = StringVar()
     varcant.set(diccionary["cantidad"])

     if diccionary["precio_x_unidad"]:
      varprecio.set(f"{diccionary["precio_x_unidad"]["cantidad"]} {diccionary["precio_x_unidad"]["tipo"]}")
     else:
      varprecio.set("no se conoce su precio")

     mostrar_cant = Label(self.frame_base,text=varcant.get())
     mostrar_cant.config(font=("Arial",25),bg="#2E2E2E",fg="white")
     mostrar_cant.grid(column=columna,row=2,pady=10,padx=0)
     
     mostrar_precio = Label(self.frame_base,text=varprecio.get())
     mostrar_precio.config(font=("Arial",25),bg="#2E2E2E",fg="white")
     mostrar_precio.grid(column=columna,row=3,pady=10,padx=0)
    case 2:
     varcantidad_de_contenedores_llenos = StringVar()
     varpeso_del_contenedor = StringVar()
     varpeso_total_de_contenedores_no_llenos = StringVar()
     varprecio_x_pesaje = StringVar()
     varprecio_x_contenedor = StringVar()
     varpesaje_total_del_producto = StringVar()
     varcantidad_de_contenedores_llenos.set(diccionary["cantidad_de_contenedores_llenos"])

     if diccionary["peso_total_de_contenedores_no_llenos"]:
      varpeso_total_de_contenedores_no_llenos.set\
      (f"{diccionary["peso_total_de_contenedores_no_llenos"]["cantidad"]} {diccionary["peso_total_de_contenedores_no_llenos"]["unidad_de_medida"]}")
     else:
      varpeso_total_de_contenedores_no_llenos.set("no se conoce su preso")

     if diccionary["peso_del_contenedor"]:
      varpeso_del_contenedor.\
        set(f"{diccionary["peso_del_contenedor"]["cantidad"]} {diccionary["peso_del_contenedor"]["unidad_de_medida"]}")
     else:
      varpeso_del_contenedor.set("no se conoce su peso")

     if diccionary["precio_x_pesaje"]:
      varprecio_x_pesaje.set(f"{diccionary["precio_x_pesaje"]["cantidad"]} {diccionary["precio_x_pesaje"]["tipo"]}")
     else:
      varprecio_x_pesaje.set("no se conoce su precio")

     if diccionary["precio_x_contenedor"]:
      varprecio_x_contenedor.set(f"{diccionary["precio_x_contenedor"]["cantidad"]} {diccionary["precio_x_contenedor"]["tipo"]}")
     else:
      varprecio_x_contenedor.set("no se conoce su precio")
     
     if diccionary["pesaje_total_del_producto"]:
      varpesaje_total_del_producto.set\
      (f"{diccionary["pesaje_total_del_producto"]["cantidad"]} {diccionary["pesaje_total_del_producto"]["unidad_de_medida"]}")
     else:
      varpesaje_total_del_producto.set("no se conoce su preso")

     varcantidad_de_contenedores_llenos = Label(self.frame_base,text=varcantidad_de_contenedores_llenos.get())
     varcantidad_de_contenedores_llenos.config(font=("Arial",25),bg="#2E2E2E",fg="white")
     varcantidad_de_contenedores_llenos.grid(column=columna,row=2,pady=10,padx=0)
     
     varpeso_del_contenedor = Label(self.frame_base,text=varpeso_del_contenedor.get())
     varpeso_del_contenedor.config(font=("Arial",25),bg="#2E2E2E",fg="white")
     varpeso_del_contenedor.grid(column=columna,row=3,pady=10,padx=0)

     varpeso_total_de_contenedores_no_llenos = Label(self.frame_base,text=varpeso_total_de_contenedores_no_llenos.get())
     varpeso_total_de_contenedores_no_llenos.config(font=("Arial",25),bg="#2E2E2E",fg="white")
     varpeso_total_de_contenedores_no_llenos.grid(column=columna,row=4,pady=10,padx=0)
     
     varpesaje_total_del_producto = Label(self.frame_base,text=varpesaje_total_del_producto.get())
     varpesaje_total_del_producto.config(font=("Arial",25),bg="#2E2E2E",fg="white")
     varpesaje_total_del_producto.grid(column=columna,row=5,pady=10,padx=0)

     varprecio_x_pesaje = Label(self.frame_base,text=varprecio_x_pesaje.get())
     varprecio_x_pesaje.config(font=("Arial",25),bg="#2E2E2E",fg="white")
     varprecio_x_pesaje.grid(column=columna,row=6,pady=10,padx=0)
     
     varprecio_x_contenedor = Label(self.frame_base,text=varprecio_x_contenedor.get())
     varprecio_x_contenedor.config(font=("Arial",25),bg="#2E2E2E",fg="white")
     varprecio_x_contenedor.grid(column=columna,row=7,pady=10,padx=0)
    case 3:
      pass
  return 0

 def ___Borrar(self,nombre):
  eliminar =messagebox.askyesno("Eliminar","Desea eliminar este producto")
  if eliminar:
   orden = {"Borrar":nombre}
   if self.callback(orden):
    messagebox.showinfo("Eliminado",f"Se ha eliminado el producto: {nombre}")
    self.__Regreso(lambda: self.Find_Product("Actualizar productos"))

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
  look_producto = Button(self.frame_base,text="Mostrar Productos",command=lambda:self.Find_Product("Mostrar productos"))
  look_producto.config(fg="white",bg="blue",font=("Arial",25))
  look_producto.config(width="18",height="-2")
  look_producto.grid(column=0,row=3,pady=10)

  """configuration = Button(self.frame_base,text="Configuracion",font=("Arial",25),command= self.__Salir)
  configuration.config(fg="white",bg="red")
  configuration.config(width="18",height="-2")
  configuration.grid(column=0,row=5,pady=10)"""

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

 def New_producto(self,num,product= None):

  tipo_producto = StringVar()
  self.__Clear()
  if product:
   atras = lambda: self.Find_Product("Actualizar productos")
   diccionary = product.dict()
   nom = StringVar()
   nom.set(diccionary["nombre"])
   name_entry = Label(self.frame_base,text=nom.get())
   name_entry.config(font=("Arial",25),bg="#2E2E2E",fg="white")
   name_entry.grid(column=1,row=1,pady=10,padx=0)
   self.__Mostrador_de_info(num,diccionary,"escribir")
   
  else:
   atras = self.Clasificator_Product
   #nombre
   name_entry = Entry(self.frame_base)
   name_entry.config(font=("Arial",10))
   name_entry.grid(column=1,row=1,pady=10,padx=0)
  name_label = Label(self.frame_base,text="Nombre del producto :")
  name_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
  name_label.grid(column=0,row=1,pady=10,padx=0)
  
  match num:
   case 1:
    tipo_producto.set("Producto Contable")

    #cantidad
    cantidad_label= Label(self.frame_base,text="Cantidad :")
    cantidad_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    cantidad_label.grid(column=0,row=2,pady=10)
    cantidad_entry = Entry(self.frame_base)
    cantidad_entry.config(font=("Arial",10))
    cantidad_entry.grid(column=1,row=2,pady=10)

    #Precio
    precio_label= Label(self.frame_base,text="Precio por producto :")
    precio_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    precio_label.grid(column=0,row=3,pady=10)
    precio_entry = Entry(self.frame_base)
    precio_entry.config(font=("Arial",10))
    precio_entry.grid(column=1,row=3,pady=10)
    fila= 4

   case 2:   
    #estos son los valores que tendra el boton los valores de unidad_de_medida
    valores = ["Unidad de medida","gramos","kilogramos","onzas","libras", "miligramos", "toneladas"]

    tipo_producto.set("Producto por Pesaje")
  
   #cantidad de contenedores 
    cantidad_de_contenedores_label= Label(self.frame_base,text="Cantidad de contenedores :")
    cantidad_de_contenedores_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    cantidad_de_contenedores_label.grid(column=0,row=2,pady=10)
    cantidad_de_contenedores_entry = Entry(self.frame_base)
    cantidad_de_contenedores_entry.config(font=("Arial",10))
    cantidad_de_contenedores_entry.grid(column=1,row=2,pady=10)

    #peso de contenedor 
    peso_del_contenedor_label= Label(self.frame_base,text="peso del contenedor :")
    peso_del_contenedor_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    peso_del_contenedor_label.grid(column=0,row=3)
    peso_del_contenedor_entry = Entry(self.frame_base)
    peso_del_contenedor_entry.config(font=("Arial",10))
    peso_del_contenedor_entry.grid(column=1,row=3)

    #pesaje_total_en_contenedores_no_llenos
    pesaje_total_en_contenedores_no_llenos_label= Label(self.frame_base,text="pesaje total de los contenedores no llenos :")
    pesaje_total_en_contenedores_no_llenos_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    pesaje_total_en_contenedores_no_llenos_label.grid(column=0,row=4,pady=10)
    pesaje_total_en_contenedores_no_llenos_entry = Entry(self.frame_base)
    pesaje_total_en_contenedores_no_llenos_entry.config(font=("Arial",10))
    pesaje_total_en_contenedores_no_llenos_entry.grid(column=1,row=4,pady=10)
   
   #pesaje_total_del_producto 
    pesaje_total_del_producto_label= Label(self.frame_base,text="pesaje total del producto :")
    pesaje_total_del_producto_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    pesaje_total_del_producto_label.grid(column=0,row=5)
    pesaje_total_del_producto_entry = Entry(self.frame_base)
    pesaje_total_del_producto_entry.config(font=("Arial",10))
    pesaje_total_del_producto_entry.grid(column=1,row=5)            

   #precio_por_peso 
    precio_por_peso_label= Label(self.frame_base,text="precio por pesaje :")
    precio_por_peso_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    precio_por_peso_label.grid(column=0,row=6,pady=10)
    precio_por_peso_entry = Entry(self.frame_base)
    precio_por_peso_entry.config(font=("Arial",10))
    precio_por_peso_entry.grid(column=1,row=6,pady=10)

    #precio_por_contenedor
    precio_por_contenedor_label= Label(self.frame_base,text="precio por contenedor :")
    precio_por_contenedor_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    precio_por_contenedor_label.grid(column=0,row=7,pady=10)
    precio_por_contenedor_entry = Entry(self.frame_base)
    precio_por_contenedor_entry.config(font=("Arial",10))
    precio_por_contenedor_entry.grid(column=1,row=7)            
    fila = 8

   case 3:  
    tipo_producto.set("Productos Liquidos")
    #estos son los valores pque tendra el boton de unidad_de_medida
    valores = ["Unidad de medida","mililitros","litros"]

    #cantidad de liquido de cada contenedor lleno
    cantidad_de_liquido_x_contenedor_label= Label(self.frame_base,text="Cantidad de liquido por contenedor lleno :")
    cantidad_de_liquido_x_contenedor_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    cantidad_de_liquido_x_contenedor_label.grid(column=0,row=2,pady=10)
    cantidad_de_liquido_x_contenedor_entry = Entry(self.frame_base)
    cantidad_de_liquido_x_contenedor_entry.config(font=("Arial",10))
    cantidad_de_liquido_x_contenedor_entry.grid(column=1,row=2,pady=10)

    #cantidad de contenedores llenos
    cantidad_de_contenedores_llenos_label= Label(self.frame_base,text="Cantidad de contenedores llenos :")
    cantidad_de_contenedores_llenos_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    cantidad_de_contenedores_llenos_label.grid(column=0,row=3)
    cantidad_de_contenedores_llenos_entry = Entry(self.frame_base)
    cantidad_de_contenedores_llenos_entry.config(font=("Arial",10))
    cantidad_de_contenedores_llenos_entry.grid(column=1,row=3)

    #cantidad de liquido en otros contenedores no llenos
    cantidad_de_liquido_en_contenedores_no_llenos_label= Label(self.frame_base,text="Cantidad de liquido en otros contenedores no llenos :")
    cantidad_de_liquido_en_contenedores_no_llenos_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    cantidad_de_liquido_en_contenedores_no_llenos_label.grid(column=0,row=4,pady=10)
    cantidad_de_liquido_en_contenedores_no_llenos_entry = Entry(self.frame_base)
    cantidad_de_liquido_en_contenedores_no_llenos_entry.config(font=("Arial",10))
    cantidad_de_liquido_en_contenedores_no_llenos_entry.grid(column=1,row=4,pady=10)
   
    #cantidad de liqido total
    cantidad_de_liquido_total_label= Label(self.frame_base,text="Cantidad de liquido total :")
    cantidad_de_liquido_total_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    cantidad_de_liquido_total_label.grid(column=0,row=5)
    cantidad_de_liquido_total_entry = Entry(self.frame_base)
    cantidad_de_liquido_total_entry.config(font=("Arial",10))
    cantidad_de_liquido_total_entry.grid(column=1,row=5)

   #precio del liquido
    precio_por_contenedor_label= Label(self.frame_base,text="Precio por contenedor lleno :")
    precio_por_contenedor_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    precio_por_contenedor_label.grid(column=0,row=6,pady=10)
    precio_por_contenedor_entry = Entry(self.frame_base)
    precio_por_contenedor_entry.config(font=("Arial",10))
    precio_por_contenedor_entry.grid(column=1,row=6,pady=10)

    #Precio por liquido
    precio_del_liquido_label= Label(self.frame_base,text="Precio del liquido :")
    precio_del_liquido_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    precio_del_liquido_label.grid(column=0,row=7,pady=10)
    precio_del_liquido_entry = Entry(self.frame_base)
    precio_del_liquido_entry.config(font=("Arial",10))
    precio_del_liquido_entry.grid(column=1,row=7)
    fila = 8
   

#frase que identifica el tipo de producto
  frase_superior= Label(self.frame_base,textvariable= tipo_producto)
  frase_superior.config(bg="#2E2E2E",fg= "white",font=("Arial",79))
  frase_superior.grid(column=0,row=0,ipady=10,padx = 125,pady= 50,columnspan=7)

# boton guardado
  save_button = Button(self.frame_base,text = "Guardar Producto")
  save_button.config(bg="blue",font=("Arial",15))
  save_button.grid(column=0,row=fila,padx=15)

#boton regresar
  atras_button = Button(self.frame_base,text = "Regresar",command=lambda:self.__Regreso(atras))
  atras_button.config(bg="red",font=("Arial",15))
  atras_button.grid(column=1,row=fila,padx=15)

#boton del tipo de moneda 
  values = ["Tipo de moneda","CUP","USD","MLC"]
  tipo_de_moneda_buton = ttk.Combobox(self.frame_base,values=values,font=("Arial",10))
  tipo_de_moneda_buton.current(0)
  tipo_de_moneda_buton.grid(column=2,row = 1,padx=10)

#boton de unidades de medida solo para los productos pesajes y los liquidos
  if num ==2 or num== 3:
   unidad_de_medida_buton = ttk.Combobox(self.frame_base,values=valores,font=("Arial",10))
   unidad_de_medida_buton.current(0)
   unidad_de_medida_buton.grid(column=3,row=1,padx= 10)

  if product:  
   clave = "Actualizar productos"
   producto = {"nombre":nom}
   orden = {clave:producto}
   # boton guardado
   name = nom.get()
   delete_button = Button(self.frame_base,text = "Borrar Producto")
   delete_button.config(bg="blue",font=("Arial",15),command= lambda: self.___Borrar(name))
   delete_button.grid(column=2,row=fila,padx=15)
  else:
   clave = "Agregar producto"
   producto = {"nombre":name_entry}
   orden = {clave :producto}

  if num ==1:
   newproducto = {"tipo":"Productos_contables","cantidad":cantidad_entry,
               "precio_x_unidad":precio_entry,"moneda":tipo_de_moneda_buton}

  elif num ==2:
   newproducto = {"tipo":"Producto_x_pesaje",
               "cantidad_de_contenedores_llenos":cantidad_de_contenedores_entry,
               "peso_del_contenedor":peso_del_contenedor_entry,
               "peso_total_de_contenedores_no_llenos":pesaje_total_en_contenedores_no_llenos_entry,
               "precio_x_pesaje":precio_por_peso_entry,
               "precio_x_contenedor":precio_por_contenedor_entry,
               "pesaje_total_del_producto":pesaje_total_del_producto_entry,
               "moneda":tipo_de_moneda_buton,"unidad_de_medida":unidad_de_medida_buton}

  else:
   newproducto =  {"tipo":"Producto_liquido",
               "cantidad_de_contenedores_llenos":cantidad_de_contenedores_llenos_entry,
               "cantidad_de_liquido_x_contenedor":cantidad_de_liquido_x_contenedor_entry,
               "cantidad_de_liquido_en_contenedores_no_llenos":cantidad_de_liquido_en_contenedores_no_llenos_entry,
               "precio_del_liquido":precio_del_liquido_entry,
               "precio_por_contenedor":precio_por_contenedor_entry,
               "cantidad_de_liquido_total":cantidad_de_liquido_total_entry,
               "moneda":tipo_de_moneda_buton,"unidad_de_medida":unidad_de_medida_buton}

  producto |= newproducto

  orden[clave] = producto      
  save_button.config(command=lambda : self.__Guardar(orden,clave,product))

 def Find_Product(self,Nextaccion):
  try:
   if self.archivo is False:
    raise NohayArchivo()
   self.__Clear()
   label_principal = Label(self.frame_base,text="Buscar Producto")
   label_principal.config(fg="white",bg="#2E2E2E",font=("Arial",69))
   label_principal.grid(column=0,row=0,pady=20)
 
   barra_find = ttk.Combobox(self.frame_base,values=[],state="normal",font=("Arial",10))
   barra_find.config(font= ("Arial",15))
   barra_find.grid(column=0,row=1,padx=5,pady=10,sticky="we")
   barra_find.bind("<KeyRelease>",lambda event: self.__Findlistcoincidence(event,barra_find))
 
   boton_Buscar = Button(self.frame_base,text="Buscar",
     font=("Arial",12),command=lambda: self.__FindAction(orden = {Nextaccion:barra_find}))
   boton_Buscar.config(bg="blue",fg="white")
   boton_Buscar.grid(column=1,row=1,padx=5)
 
   button_atras=Button(self.frame_base,text="Regresar",
     font=("Arial",12),command=lambda: self.__Regreso(self.Principal_Windows))
   button_atras.config(bg="red",fg="white")
   button_atras.grid(column=1, row=2,pady=10)
  except NohayArchivo: messagebox.showinfo("Archivo Vacio","Aun no se han guardado ningun producto")

 def Mostrar_product(self,product):
  tipo_producto = StringVar()
  diccionary = product.dict()
  num = self.callback({"Tipo de productos":product})
  self.__Clear()
  atras = lambda: self.Find_Product("Mostrar productos")
  diccionary = product.dict()
  nom = StringVar()
  nom.set(diccionary["nombre"])
  mostrar_nom = Label(self.frame_base,text=nom.get())
  mostrar_nom.config(font=("Arial",25),bg="#2E2E2E",fg="white")
  mostrar_nom.grid(column=1,row=1,pady=10,padx=0)
  name_label = Label(self.frame_base,text="Nombre del producto :")
  name_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
  name_label.grid(column=0,row=1,pady=10,padx=0)
  self.__Mostrador_de_info(num,diccionary,"mostrar")
    
  match num:
   case 1:
    tipo_producto.set("Producto Contable")

    #cantidad
    cantidad_label= Label(self.frame_base,text="Cantidad :")
    cantidad_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    cantidad_label.grid(column=0,row=2,pady=10)


    #Precio
    precio_label= Label(self.frame_base,text="Precio por producto :")
    precio_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    precio_label.grid(column=0,row=3,pady=10)

    fila= 4

   case 2:   
    #estos son los valores que tendra el boton los valores de unidad_de_medida
    valores = ["Unidad de medida","gramos","kilogramos","onzas","libras", "miligramos", "toneladas"]

    tipo_producto.set("Producto por Pesaje")
  
   #cantidad de contenedores 
    cantidad_de_contenedores_label= Label(self.frame_base,text="Cantidad de contenedores :")
    cantidad_de_contenedores_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    cantidad_de_contenedores_label.grid(column=0,row=2,pady=10)

    #peso de contenedor 
    peso_del_contenedor_label= Label(self.frame_base,text="peso del contenedor :")
    peso_del_contenedor_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    peso_del_contenedor_label.grid(column=0,row=3)

    #pesaje_total_en_contenedores_no_llenos
    pesaje_total_en_contenedores_no_llenos_label= Label(self.frame_base,text="pesaje total de los contenedores no llenos :")
    pesaje_total_en_contenedores_no_llenos_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    pesaje_total_en_contenedores_no_llenos_label.grid(column=0,row=4,pady=10)
   
   #pesaje_total_del_producto 
    pesaje_total_del_producto_label= Label(self.frame_base,text="pesaje total del producto :")
    pesaje_total_del_producto_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    pesaje_total_del_producto_label.grid(column=0,row=5)            

   #precio_por_peso 
    precio_por_peso_label= Label(self.frame_base,text="precio por pesaje :")
    precio_por_peso_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    precio_por_peso_label.grid(column=0,row=6,pady=10)

    #precio_por_contenedor
    precio_por_contenedor_label= Label(self.frame_base,text="precio por contenedor :")
    precio_por_contenedor_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    precio_por_contenedor_label.grid(column=0,row=7,pady=10)            
    fila = 8

   case 3:  
    tipo_producto.set("Productos Liquidos")
    #estos son los valores pque tendra el boton de unidad_de_medida
    valores = ["Unidad de medida","mililitros","litros", "onzas líquidas"]

    #cantidad de liquido de cada contenedor lleno
    cantidad_de_liquido_x_contenedor_label= Label(self.frame_base,text="Cantidad de liquido por contenedor lleno :")
    cantidad_de_liquido_x_contenedor_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    cantidad_de_liquido_x_contenedor_label.grid(column=0,row=2,pady=10)

    #cantidad de contenedores llenos
    cantidad_de_contenedores_llenos_label= Label(self.frame_base,text="Cantidad de contenedores llenos :")
    cantidad_de_contenedores_llenos_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    cantidad_de_contenedores_llenos_label.grid(column=0,row=3)

    #cantidad de liquido en otros contenedores no llenos
    cantidad_de_liquido_en_contenedores_no_llenos_label= Label(self.frame_base,text="Cantidad de liquido en otros contenedores no llenos :")
    cantidad_de_liquido_en_contenedores_no_llenos_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    cantidad_de_liquido_en_contenedores_no_llenos_label.grid(column=0,row=4,pady=10)
   
    #cantidad de liqido total
    cantidad_de_liquido_total_label= Label(self.frame_base,text="Cantidad de liquido total :")
    cantidad_de_liquido_total_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    cantidad_de_liquido_total_label.grid(column=0,row=5)

   #precio del liquido
    precio_por_contenedor_label= Label(self.frame_base,text="Precio por contenedor lleno :")
    precio_por_contenedor_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    precio_por_contenedor_label.grid(column=0,row=6,pady=10)

    #Precio por liquido
    precio_del_liquido_label= Label(self.frame_base,text="Precio del liquido :")
    precio_del_liquido_label.config(bg="#2E2E2E",fg= "white",font=("Arial",26))
    precio_del_liquido_label.grid(column=0,row=7,pady=10)
    fila = 8

#boton regresar
  atras_button = Button(self.frame_base,text = "Regresar",command=lambda:self.__Regreso(atras))
  atras_button.config(bg="red",font=("Arial",15))
  atras_button.grid(column=1,row=fila,padx=15)

#frase que identifica el tipo de producto
  frase_superior= Label(self.frame_base,textvariable= tipo_producto)
  frase_superior.config(bg="#2E2E2E",fg= "white",font=("Arial",79))
  frase_superior.grid(column=0,row=0,ipady=10,padx = 125,pady= 50,columnspan=7)
  
   