

class Unidades_Medida():#clase auxiliar abstracta
 def __init__ (self, cantidad, unidad_de_medida):
  self.cantidad = cantidad
  self.unidad_de_medida = unidad_de_medida

 def dict(self):
  """convierte los atributos en un diccionario y retorna un 
  diccionario con la clave de unidad de medida"""

  return {"cantidad":self.cantidad,"unidad_de_medida":self.unidad_de_medida}
