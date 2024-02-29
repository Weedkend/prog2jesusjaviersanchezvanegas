class persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido           
    def obtenernombre(self):
        return f'mi nombre es {self.nombre} {self.apellido}'
