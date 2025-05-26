# Ejercicio N° 2 del  Parcial N° 2 - Optativo.
# Alumno: Elias Franco Duarte - C.I: 6.167.356

class Curso:
    def __init__(self, nombre, listaEstudiantes, capacidadMaxima):
        self._nombre = nombre
        self._listaEstudiantes = []
        self._capacidadMaxima = capacidadMaxima
        
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def capacidadMaxima(self):
        return self._capacidadMaxima
    
    @property
    def listaEstudiantes(self):
        return self._listaEstudiantes
    

    def agregarAlumnos(self, nombre, notaAlumno):
        if len(self._listaEstudiantes) >= self._capacidadMaxima:
            raise ValueError(f"No se pueden agregar más alumnos. Capacidad máxima alcanzada. Capacidad: {self.capacidadMaxima}")
        
        if notaAlumno < 0 or notaAlumno > 5:
            raise ValueError("La nota del alumno debe de ser entre 0 y 5")
        
        self._listaEstudiantes.append((nombre, notaAlumno))
        print(f"Se ha agregado correctamente al alumno: {nombre} con una nota de {notaAlumno}")
        
    @property
    def calcularPromedioCurso(self):
        if not self._listaEstudiantes:
            return  0
        total = sum(notaAlumno for _, notaAlumno in self._listaEstudiantes)
        return total / len(self._listaEstudiantes)
    
    def mostrarResultados(self):
        promedio = self.calcularPromedioCurso
        return print(f"Promedio del curso: '{self.nombre}': {promedio:.2f} ")
    
c = Curso("Optativo", 3, 5)
c.agregarAlumnos("Elias", 5)
c.agregarAlumnos("Juan", 4)
c.agregarAlumnos("Luana", 2)
c.agregarAlumnos("Juana", 3)
c.agregarAlumnos("Liza", 5)
# c.agregarAlumnos("Martin", 2) Comentado para poder probar si lanza error y no pasa la cantidad máxima establecida
c.mostrarResultados()
