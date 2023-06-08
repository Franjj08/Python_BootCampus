class ALumno:
    nombre = None
    nota = None

    def __init__(self,nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def imprimirNota(self):
        print(self.nota)
    def EstaAprobado(self):
        if (self.nota < 4):
            return False
        else:
            return True
        
ALumno = ALumno('Alex',8)
ALumno.imprimirNota()
print(ALumno.EstaAprobado())