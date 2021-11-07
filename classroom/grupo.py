from classroom.asignatura import Asignatura
class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if not lista == None:  
            self.listadoAlumnos = lista + [alumno]
        else:
            self.listadoAlumnos = [alumno]
            
    def __str__(self):
        re="Grupo de estudiantes: "+ self._grupo
        return re

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
       

   