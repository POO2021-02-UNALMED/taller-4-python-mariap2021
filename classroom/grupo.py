from classroom.asignatura import Asignatura
class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas= None, estudiantes= None):
        self._grupo = grupo
        if estudiantes is None:
            self.listadoAlumnos = []
        else:
             self.listadoAlumnos = estudiantes    
        

        if asignaturas is None:
            self._asignaturas = []
        else:
            self._asignaturas = asignaturas
                 

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))





    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = [alumno]
            self.listadoAlumnos = self.listadoAlumnos + lista
        else:
            self.listadoAlumnos = lista + [alumno]
               
     

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __str__(self):
       r= " Grupo de estudiantes:"+ self._grupo
       return r
       

   