def Verificador_de_None(variable,funcion,otherfunc=None):
    if variable:
        return funcion
    return otherfunc

class Productos:
 """
 Clase base para representar productos.

 Attributes:
   nombre (str): El nombre del producto.
 """
 def __init__(self, nombre):
  """
  Inicializa un objeto Productos.

  Args:
    nombre (str): El nombre del producto.
  """
  self.nombre = nombre

 def dict(self):
  """Devuelve un diccionario con los atributos del producto"""
  return{"nombre":self.nombre}



class Productos_contables(Productos):
 """
 Clase para representar productos contables, como unidades individuales.

 Attributes:
   cantidad (int): La cantidad de unidades del producto.
   precio_x_unidad (float): El precio por unidad del producto.
 """
 def __init__(self, nombre, cantidad, precio_x_unidad= None):
  """
  Inicializa un objeto Productos_contables.

  Args:
    nombre (str): El nombre del producto.
    cantidad (int): La cantidad de unidades del producto.
    precio_x_unidad (float): El precio por unidad del producto.
  """
  super().__init__(nombre)
  self.cantidad = cantidad
  self.precio_x_unidad = precio_x_unidad

 def dict(self):
  """convierte los atributos en un diccionario y retorna un 
  diccionario con la clave ProductoContable"""
  datos= super().dict()
  datos["cantidad"]= self.cantidad
  try:
    datos["precio_x_unidad"]=Verificador_de_None(self.precio_x_unidad,self.precio_x_unidad.dict(),
     otherfunc="no se han rejistrado datos al respecto")
  except AttributeError:
   datos["precio_x_unidad"]=Verificador_de_None(self.precio_x_unidad,self.precio_x_unidad)
  
  return datos


 def PrecioTotal(self):
  """
  Calcula el precio total del producto.

  Returns:
    float: El precio total del producto.
  """
  return self.cantidad * self.precio_x_unidad



class Producto_x_pesaje(Productos):
 """Clase para productos que se venden por peso."""


 def __init__(self, nombre, cantidad_de_contenedores_llenos=None, peso_del_contenedor=None, 
  peso_total_de_contenedores_no_llenos=None, precio_x_pesaje=None, 
  precio_x_contenedor=None, pesaje_total_del_producto=None):
  """Inicializa la clase con atributos relacionados al pesaje."""
  super().__init__(nombre)
  self.cantidad_de_contenedores_llenos = cantidad_de_contenedores_llenos
  self.peso_del_contenedor = peso_del_contenedor
  self.peso_total_de_contenedores_no_llenos = peso_total_de_contenedores_no_llenos
  self.precio_x_pesaje = precio_x_pesaje
  self.precio_x_contenedor = precio_x_contenedor
  self.pesaje_total_del_producto = pesaje_total_del_producto


 def dict(self):
   """Devuelve un disccionario con los atributos del producto pesado."""
   datos = super().dict()
   datos["cantidad_de_contenedores_llenos"]=self.cantidad_de_contenedores_llenos

   try:
    datos["peso_total_de_contenedores_no_llenos"]=Verificador_de_None(self.peso_total_de_contenedores_no_llenos,
     self.peso_total_de_contenedores_no_llenos.dict())
   except AttributeError:datos["peso_total_de_contenedores_no_llenos"]=Verificador_de_None(self.peso_total_de_contenedores_no_llenos,
     self.peso_total_de_contenedores_no_llenos)

   try:
    datos["precio_x_contenedor"]=Verificador_de_None(self.precio_x_contenedor,
     self.precio_x_contenedor.dict(),)
   except AttributeError:  datos["precio_x_contenedor"]=Verificador_de_None(self.precio_x_contenedor,
     self.precio_x_contenedor)

   try:
    datos["precio_x_pesaje"]=Verificador_de_None(self.precio_x_pesaje,
     self.precio_x_pesaje.dict())
   except AttributeError:  datos["precio_x_pesaje"]=Verificador_de_None(self.precio_x_pesaje,
     self.precio_x_pesaje)

   try:
    datos["pesaje_total_del_producto"]=Verificador_de_None(self.pesaje_total_del_producto,
     self.pesaje_total_del_producto.dict())
   except AttributeError:  datos["pesaje_total_del_producto"]=Verificador_de_None(self.pesaje_total_del_producto,
     self.pesaje_total_del_producto)

   try:
    datos["peso_del_contenedor"]=Verificador_de_None(self.peso_del_contenedor,
     self.peso_del_contenedor.dict())
   except AttributeError:  datos["peso_del_contenedor"]=Verificador_de_None(self.peso_del_contenedor,
     self.peso_del_contenedor.dict())

   return datos


 def Calcular_precio_x_contenedor(self):
  """Calcula el precio por contenedor si precio_x_pesaje no es None."""
  self.precio_x_contenedor = Verificador_de_None(self.precio_x_pesaje,
   self.precio_x_pesaje * self.peso_del_contenedor)
  return self.precio_x_contenedor


 def Calcular_precio_x_pesaje(self):
  """Calcula el precio por pesaje si precio_x_contenedor no es None."""
  self.precio_x_pesaje = Verificador_de_None(self.precio_x_contenedor,
   self.precio_x_contenedor / self.cantidad_de_contenedores)
  return self.precio_x_pesaje


 def PrecioTotal(self):
  """Calcula el precio total del producto por pesaje.

  Returns:
    float: El precio total del producto, o None si no se puede calcular.
  """
  precio_x_cont = self.Calcular_precio_x_contenedor()
  precio_x_p = self.Calcular_precio_x_pesaje()

  precio_total_cont = Verificador_de_None(precio_x_cont and
   self.cantidad_de_contenedores_llenos,precio_x_cont * self.cantidad_de_contenedores_llenos)
  precio_total_no_llenos= Verificador_de_None(precio_x_p and 
   self.cantidad_de_liquido_en_contenedores_no_llenos,precio_x_p *
   self.cantidad_de_liquido_en_contenedores_no_llenos)
  self.precio_total = Verificador_de_None(
   precio_total_cont and precio_total_no_llenos, 
   precio_total_cont + precio_total_no_llenos,
   otherfunc=Verificador_de_None(precio_total_cont,precio_total_cont)
  )
  return self.precio_total



class Producto_liquido(Productos):
 """
 Clase para representar productos líquidos, como líquidos envasados.

 Attributes:
   cantidad_de_liquido_del_contenedor (float): La cantidad de líquido en un contenedor.
   cantidad_de_contenedores_llenos (int): La cantidad de contenedores llenos.
   cantidad_de_liquido_en_contenedores_no_llenos (float): La cantidad de líquido en contenedores no llenos.
   cantidad_liquido_total (float): La cantidad total de líquido.
   precio_x_contenedor (float): El precio por contenedor.
   precio_x_litros (float): El precio por litro.
 """
 def __init__(self, nombre, cantidad_de_liquido_del_contenedor=None, cantidad_de_contenedores_llenos=None, 
    cantidad_de_liquido_en_contenedores_no_llenos=None, cantidad_liquido_total=None, 
    precio_x_contenedor=None, precio_x_litros=None):
  """
  Inicializa un objeto Producto_liquido.

  Args:
    nombre (str): El nombre del producto.
    cantidad_de_liquido_del_contenedor (float): La cantidad de líquido en un contenedor.
    cantidad_de_contenedores_llenos (int): La cantidad de contenedores llenos.    cantidad_de_liquido_en_contenedores_no_llenos (float): La cantidad de líquido en contenedores no llenos.
    cantidad_liquido_total (float): La cantidad total de líquido.
    precio_x_contenedor (float): El precio por contenedor.
    precio_x_litros (float): El precio por litro.
  """
  super().__init__(nombre)
  self.cantidad_de_liquido_del_contenedor = cantidad_de_liquido_del_contenedor
  self.cantidad_de_contenedores_llenos = cantidad_de_contenedores_llenos
  self.cantidad_de_liquido_en_contenedores_no_llenos = cantidad_de_liquido_en_contenedores_no_llenos
  self.cantidad_liquido_total = cantidad_liquido_total
  self.precio_x_contenedor = precio_x_contenedor
  self.precio_x_litros = precio_x_litros

 def dict(self):
   """Devuelve un diccionario con la clave de Productos_Liquidos
    para acceder a los atributos del producto liquido."""
   datos = super().dict()
   datos["cantidad_de_contenedores_llenos"]=self.cantidad_de_contenedores_llenos
   try:
    datos["cantidad_de_liquido_del_contenedor"]=Verificador_de_None(self.cantidad_de_liquido_del_contenedor,
     self.cantidad_de_liquido_del_contenedor.dict())
   except AttributeError:     datos["cantidad_de_liquido_del_contenedor"]=Verificador_de_None(self.cantidad_de_liquido_del_contenedor,
     self.cantidad_de_liquido_del_contenedor,)

   try: 
    datos["precio_x_contenedor"]=Verificador_de_None(self.precio_x_contenedor,
     self.precio_x_contenedor.dict(),otherfunc="no se han rejistrado datos al respecto")
   except AttributeError:datos["precio_x_contenedor"]=Verificador_de_None(self.precio_x_contenedor,
     self.precio_x_contenedor)

   try:
    datos["precio_x_litros"]=Verificador_de_None(self.precio_x_litros,
     self.precio_x_litros.dict())
   except AttributeError:datos["precio_x_litros"]=Verificador_de_None(self.precio_x_litros,
     self.precio_x_litros)

   try:
    datos["cantidad_liquido_total"]=Verificador_de_None(self.cantidad_liquido_total,
     self.cantidad_liquido_total.dict())
   except AttributeError:datos["cantidad_liquido_total"]=Verificador_de_None(self.cantidad_liquido_total,
     self.cantidad_liquido_total)

   try:
    datos["cantidad_de_liquido_en_contenedores_no_llenos"]=Verificador_de_None(
     self.cantidad_de_liquido_en_contenedores_no_llenos,
     self.cantidad_de_liquido_en_contenedores_no_llenos.dict(),
     otherfunc="no se han rejistrado datos al respecto")
   except AttributeError:datos["cantidad_de_liquido_en_contenedores_no_llenos"]=Verificador_de_None(
     self.cantidad_de_liquido_en_contenedores_no_llenos,
     self.cantidad_de_liquido_en_contenedores_no_llenos)

   return datos


 def Calcular_precio_x_contenedor(self):
  """
  Calcula el precio por contenedor si precio_x_litros no es None.

  Returns:
    float: El precio por contenedor, o None si precio_x_litros es None.
  """
  self.precio_x_contenedor = Verificador_de_None(self.precio_x_litros,
    self.precio_x_litros * self.cantidad_de_liquido_del_contenedor)

  return self.precio_x_contenedor


 def Calcular_precio_x_litros(self):
  """
  Calcula el precio por litro si precio_x_contenedor no es None.

  Returns:
    float: El precio por litro, o None si precio_x_contenedor es None.
  """
  self.precio_x_litros = Verificador_de_None(
   self.precio_x_contenedor,
   self.precio_x_contenedor / self.cantidad_de_liquido_del_contenedor)

  return self.precio_x_litros


 def PrecioTotal(self):
  """
  Calcula el precio total del producto líquido.

  Returns:
    float: El precio total del producto, o None si no se puede calcular.
  """
  precio_x_cont = self.Calcular_precio_x_contenedor()
  precio_x_l = self.Calcular_precio_x_litros()

  precio_total_cont = Verificador_de_None(precio_x_cont and
   self.cantidad_de_contenedores_llenos,precio_x_cont * self.cantidad_de_contenedores_llenos)

  precio_total_no_llenos= Verificador_de_None(precio_x_l and 
   self.cantidad_de_liquido_en_contenedores_no_llenos,precio_x_l *
   self.cantidad_de_liquido_en_contenedores_no_llenos)

  self.precio_total = Verificador_de_None(
   precio_total_cont and precio_total_no_llenos, 
   precio_total_cont + precio_total_no_llenos,
   otherfunc=Verificador_de_None(precio_total_cont,precio_total_cont))

  return self.precio_total
 