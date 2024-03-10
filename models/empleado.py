from pydantic import BaseModel
class Empleado(BaseModel):
   nombre:str
   apellido:str
   documento:str
   edad:int
   salario:int