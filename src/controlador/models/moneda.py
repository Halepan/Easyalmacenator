
class Moneda(): 
 def __init__(self,cantidad,tipo) -> None:
   self.cantidad = cantidad
   self.tipo = tipo


 def dict(self):
  """convierte los atributos en un diccionario y retorna un 
  diccionario con la clave de moneda"""
  
  return {"cantidad":self.cantidad,"tipo":self.tipo}
 