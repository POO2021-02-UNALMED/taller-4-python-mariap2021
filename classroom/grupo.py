from classroom.asignatura import Asignatura
class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs:
            self._asignaturas.append(Asignatura(x))

    def __str__(self):
       nuevo= " Grupo de estudiantes:"+ self._gr
       return nuevo



    def agregarAlumno(self, alumno, lista=[]):
        if(lista != []):
            lista.append(alumno)
            self.listadoAlumnos = self.listadoAlumnos + lista
        else:
            self.listadoAlumnos = [alumno]

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    

   