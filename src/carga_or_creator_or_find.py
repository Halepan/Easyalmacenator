from controlador.models.productos import Productos_contables,Producto_x_pesaje,Producto_liquido
from controlador.models.moneda import Moneda
from controlador.models.unidadadMedida import Unidades_Medida
import json

def Creator_Productos(registro):
 """
 Esta función se encarga de crear productos a partir de un diccionario de datos.

 Args:
  registro (dict): Diccionario que contiene la información del producto.
   Este diccionario debe tener la clave "tipo" para indicar el tipo de 
   producto que se quiere crear.

 Returns:
  object: Objeto producto instanciado según el tipo especificado en el 
   diccionario, o None si no se encuentra el tipo o hay errores.

 Raises:
  KeyError: Si el diccionario no tiene la clave "tipo" o si faltan claves 
   específicas para el tipo de producto.
 """

 try:
  tipo = registro["tipo"]

  # Creación de productos contables
  if tipo == "Productos_contables":
   # Se busca la clave del producto contable dentro del registro
   for clave in registro:
    if clave != "tipo":
     # Se extraen los datos del producto contable
     claves_cargada = registro[clave]
     # Se crea el objeto del producto contable
     producto = Productos_contables(
       claves_cargada['nombre'],
       claves_cargada['cantidad'],
       claves_cargada['precio_x_unidad']
     )

     # Se establece el precio por unidad, si está definido
     if producto.precio_x_unidad:
      producto.precio_x_unidad = Moneda(
        producto.precio_x_unidad['cantidad'],
        producto.precio_x_unidad['tipo']
      )

     # Se retorna el producto creado
     return producto 

  # Creación de productos líquidos
  elif tipo == "Producto_liquido":
   # Se busca la clave del producto líquido dentro del registro
   for clave in registro:
    if clave != "tipo":
     # Se extraen los datos del producto líquido
     claves_cargada = registro[clave]
     # Se crea el objeto del producto líquido
     producto = Producto_liquido(
       claves_cargada['nombre'],
       claves_cargada['cantidad_de_liquido_del_contenedor'],
       claves_cargada['cantidad_de_contenedores_llenos'],
       claves_cargada['cantidad_de_liquido_en_contenedores_no_llenos'],
       claves_cargada['cantidad_liquido_total'],
       claves_cargada['precio_x_contenedor'],
       claves_cargada['precio_x_litros']
     )

     # Se establecen las unidades de medida y moneda, si están definidas
     if producto.cantidad_liquido_total:
      producto.cantidad_liquido_total = Unidades_Medida(
        producto.cantidad_liquido_total['cantidad'],
        producto.cantidad_liquido_total['unidad_de_medida']
      )

     if producto.cantidad_de_liquido_del_contenedor:
      producto.cantidad_de_liquido_del_contenedor = Unidades_Medida(
        producto.cantidad_de_liquido_del_contenedor['cantidad'],
        producto.cantidad_de_liquido_del_contenedor['unidad_de_medida']
      )

     if producto.cantidad_de_liquido_en_contenedores_no_llenos:
      producto.cantidad_de_liquido_en_contenedores_no_llenos = Unidades_Medida(
        producto.cantidad_de_liquido_en_contenedores_no_llenos['cantidad'],
        producto.cantidad_de_liquido_en_contenedores_no_llenos['unidad_de_medida']
      )

     if producto.precio_x_contenedor:
      producto.precio_x_contenedor = Moneda(
        producto.precio_x_contenedor['cantidad'],
        producto.precio_x_contenedor['tipo']
      )

     if producto.precio_x_litros:
      producto.precio_x_litros = Moneda(
        producto.precio_x_litros['cantidad'],
        producto.precio_x_litros['tipo']
      )

     # Se retorna el producto creado
     return producto 
  
# Creación de productos de pesajes
  elif tipo == "Producto_x_pesaje":
   # Se busca la clave del producto_x_pesaje dentro del registro
   for clave in registro:
    if clave != "tipo":
     # Se extraen los datos del producto_x_pesaje
     claves_cargada = registro[clave]
     # Se crea el objeto del producto_x_pesaje
     producto = Producto_x_pesaje(
       claves_cargada['nombre'],
       claves_cargada['cantidad_de_contenedores_llenos'],
       claves_cargada['peso_del_contenedor'],
       claves_cargada['peso_total_de_contenedores_no_llenos'],
       claves_cargada['precio_x_pesaje'],
       claves_cargada['precio_x_contenedor'],
       claves_cargada['pesaje_total_del_producto']
     )

     # Se establecen las unidades de medida y moneda, si están definidas
     if producto.pesaje_total_del_producto:
      producto.pesaje_total_del_producto = Unidades_Medida(
        producto.pesaje_total_del_producto['cantidad'],
        producto.pesaje_total_del_producto['unidad_de_medida']
      )

     if producto.peso_del_contenedor:
      producto.peso_del_contenedor = Unidades_Medida(
        producto.peso_del_contenedor['cantidad'],
        producto.peso_del_contenedor['unidad_de_medida']
      )

     if producto.peso_total_de_contenedores_no_llenos:
      producto.peso_total_de_contenedores_no_llenos = Unidades_Medida(
        producto.peso_total_de_contenedores_no_llenos['cantidad'],
        producto.peso_total_de_contenedores_no_llenos['unidad_de_medida']
      )

     if producto.precio_x_contenedor:
      producto.precio_x_contenedor = Moneda(
        producto.precio_x_contenedor['cantidad'],
        producto.precio_x_contenedor['tipo']
      )

     if producto.precio_x_pesaje:
      producto.precio_x_pesaje = Moneda(
        producto.precio_x_pesaje['cantidad'],
        producto.precio_x_pesaje['tipo']
      )

     # Se retorna el producto creado
     return producto 

  print("error inesperado")
 # Se manejan los errores de claves faltantes
 except ValueError:
  print("Error: Faltan claves de registro.")
  return None # Se retorna None si hay un error


def Load_archivo():
   
 productos_cargados = {}
 try:
  archivo = open("Productos del almacen.txt", "r")
  datos = json.load(archivo)
  for registro in datos :#recorrer el archivo cargado
   product = Creator_Productos(registro)
   if product:
    productos_cargados[product.nombre] = product
   else:
    raise TypeError("no aparece el archivo")
  return productos_cargados
 except FileNotFoundError:return False
 except json.JSONDecodeError: print("Error al decodificar el archivo Json")
 except TypeError:print(TypeError)

def Tipo_product(product):
 if isinstance(product,Productos_contables):
   return 1
 elif isinstance(product,Producto_x_pesaje):
   return 2
 elif isinstance(product,Producto_liquido):
   return 3

def Sobreescribir_product(producto_origin,new_producto):
 num_new = Tipo_product(new_producto)
 match num_new:
  case 1:
   if new_producto.cantidad:
    producto_origin.cantidad = new_producto.cantidad

   if new_producto.precio_x_unidad:
    producto_origin.precio_x_unidad = new_producto.precio_x_unidad

   return producto_origin
  
  case 2:
       if new_producto.peso_del_contenedor:
        producto_origin.peso_del_contenedor = new_producto.peso_del_contenedor

       if new_producto.cantidad_de_contenedores_llenos:
        producto_origin.cantidad_de_contenedores_llenos = new_producto.cantidad_de_contenedores_llenos

       if new_producto.peso_total_de_contenedores_no_llenos:
        producto_origin.peso_total_de_contenedores_no_llenos = new_producto.peso_total_de_contenedores_no_llenos

       if new_producto.pesaje_total_del_producto:
        producto_origin.pesaje_total_del_producto = new_producto.pesaje_total_del_producto

       if new_producto.precio_x_contenedor:
        producto_origin.precio_x_contenedor = new_producto.precio_x_contenedor

       if new_producto.precio_x_pesaje:
        producto_origin.precio_x_pesaje = new_producto.precio_x_pesaje

       return producto_origin

  case 3:
       if new_producto.cantidad_de_liquido_del_contenedor:
        producto_origin.cantidad_de_liquido_del_contenedor = new_producto.cantidad_de_liquido_del_contenedor

       if new_producto.cantidad_de_contenedores_llenos:
        producto_origin.cantidad_de_contenedores_llenos = new_producto.cantidad_de_contenedores_llenos

       if new_producto.cantidad_de_liquido_en_contenedores_no_llenos:
        producto_origin.cantidad_de_liquido_en_contenedores_no_llenos = new_producto.cantidad_de_liquido_en_contenedores_no_llenos

       if new_producto.cantidad_liquido_total:
        producto_origin.cantidad_liquido_total = new_producto.cantidad_liquido_total

       if new_producto.precio_x_contenedor:
        producto_origin.precio_x_contenedor = new_producto.precio_x_contenedor

       if new_producto.precio_x_litros:
        producto_origin.precio_x_litros = new_producto.precio_x_litros

       return producto_origin
 print("Error")

