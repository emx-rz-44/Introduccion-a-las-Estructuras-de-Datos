from datetime import datetime
class Ejercicios:
    @staticmethod
    def leer_entero(mensaje, minimo=None):
        """Lee un número entero por teclado y repite hasta que sea válido."""
        while True:
            try:
                valor = int(input(mensaje))
                if minimo is not None and valor < minimo:
                    print(f"  Error: el valor debe ser mayor o igual a {minimo}.")
                    continue
                return valor
            except ValueError:
                print("  Error: ingrese un número entero válido.")

    @staticmethod
    def leer_decimal(mensaje, minimo=0.0, maximo=5.0):
        """Lee un número decimal (acepta coma o punto) dentro de un rango."""
        while True:
            try:
                valor = float(input(mensaje).replace(",", "."))
                if valor < minimo or valor > maximo:
                    print(f"  Error: la nota debe estar entre {minimo} y {maximo}.")
                    continue
                return valor
            except ValueError:
                print("  Error: ingrese un número válido (ej. 3.5).")

    # Ejercicio 1: promedio con ingreso por teclado y valor centinela

    def ejercicio_1(self):
        """Promedio de las edades de un estudiante; termina al digitar 0."""
        print("EJERCICIO 1 - Promedio con ingreso por teclado (centinela 0)")
        valores = []
        while True:
            edad = self.leer_entero("Ingrese una edad (0 para terminar): ", 0)
            if edad == 0:
                break
            valores.append(edad)
        if valores:
            promedio = sum(valores) / len(valores)
            print(f"Valores ingresados: {valores}")
            print(f"Suma = {sum(valores)} | Cantidad = {len(valores)}")
            print(f"Promedio = {promedio:.2f}")
        else:
            print("No se ingresaron datos.")

    # Ejercicio 2: promedio de edades indicando la cantidad

    def ejercicio_2(self):
        """Promedio de edades; primero se pide la cantidad de datos."""
        print("EJERCICIO 2 - Promedio de edades indicando la cantidad")
        n = self.leer_entero("Cantidad de edades a ingresar: ", 1)
        edades = []
        for i in range(1, n + 1):
            edades.append(self.leer_entero(f"  Edad {i}: ", 0))
        promedio = sum(edades) / n
        print(f"Edades: {edades}")
        print(f"Suma = {sum(edades)} | Cantidad = {n}")
        print(f"Promedio de edades = {promedio:.2f}")

    # Ejercicio 3: promedio de notas con decimales

    def ejercicio_3(self):
        """Promedio de notas decimales (escala 0.0 a 5.0)."""
        print("EJERCICIO 3 - Promedio de notas con decimales")
        n = self.leer_entero("Cantidad de notas a ingresar: ", 1)
        notas = []
        for i in range(1, n + 1):
            notas.append(self.leer_decimal(f"  Nota {i} (0.0 - 5.0): "))
        promedio = sum(notas) / n
        print(f"Notas: {notas}")
        print(f"Suma = {sum(notas):.2f} | Cantidad = {n}")
        print(f"Promedio de notas = {promedio:.2f}")

    # Ejercicio 4: nombres con sus edades

    def ejercicio_4(self):
        """Almacena nombres y edades en listas paralelas y los imprime."""
        print("EJERCICIO 4 - Nombres de estudiantes con sus edades")
        n = self.leer_entero("Cantidad de estudiantes: ", 1)
        nombres, edades = [], []
        for i in range(1, n + 1):
            nombres.append(input(f"  Nombre del estudiante {i}: ").strip().title())
            edades.append(self.leer_entero(f"  Edad de {nombres[-1]}: ", 0))
        print("\nListado de estudiantes")
        print(f"{'No.':<5}{'Nombre':<20}{'Edad':>5}")
        print("-" * 30)
        for i in range(n):
            print(f"{i + 1:<5}{nombres[i]:<20}{edades[i]:>5}")

    # Ejercicio 5: suma de dos matrices

    def leer_matriz(self, nombre, filas, columnas):
        """Lee una matriz fila por fila (valores enteros separados por espacio)."""
        matriz = []
        for i in range(filas):
            while True:
                try:
                    fila = [int(x) for x in
                            input(f"  {nombre} fila {i + 1}: ").split()]
                    if len(fila) != columnas:
                        print(f"  Error: la fila debe tener {columnas} valores.")
                        continue
                    matriz.append(fila)
                    break
                except ValueError:
                    print("  Error: ingrese solo números enteros.")
        return matriz

    @staticmethod
    def imprimir_matriz(nombre, matriz):
        """Imprime una matriz con formato de columnas alineadas."""
        print(f"{nombre} =")
        for fila in matriz:
            print("   [ " + " ".join(f"{x:>4}" for x in fila) + " ]")

    def ejercicio_5(self):
        """Suma de dos matrices de igual dimensión: C[i][j] = A[i][j] + B[i][j]."""
        print("EJERCICIO 5 - Sumatoria de dos matrices")
        filas = self.leer_entero("Número de filas: ", 1)
        columnas = self.leer_entero("Número de columnas: ", 1)
        print("Matriz A (valores separados por espacio):")
        a = self.leer_matriz("A", filas, columnas)
        print("Matriz B (valores separados por espacio):")
        b = self.leer_matriz("B", filas, columnas)
        c = [[a[i][j] + b[i][j] for j in range(columnas)] for i in range(filas)]
        print()
        self.imprimir_matriz("A", a)
        self.imprimir_matriz("B", b)
        self.imprimir_matriz("C = A + B", c)

    # Ejercicio 6: tabla de multiplicar con vectores y matrices

    def ejercicio_6(self):
        """Tabla de multiplicar: matriz de factores y matriz de resultados."""
        print("EJERCICIO 6 - Tabla de multiplicar con vectores y matrices")
        tabla = self.leer_entero("Tabla a generar (ej. 7): ", 1)
        limite = self.leer_entero("Multiplicar hasta (ej. 10): ", 1)

        multiplicadores = list(range(1, limite + 1))          
        factores = [[tabla, m] for m in multiplicadores]      
        resultados = [[f[0] * f[1]] for f in factores]        

        print("\nVector de multiplicadores:", multiplicadores)
        print("\nMatriz de factores [a, b]   |  Matriz de resultados")
        for i in range(limite):
            par = f"[{factores[i][0]:>3}, {factores[i][1]:>3}]"
            print(f"{par:<28}|  [{resultados[i][0]:>4}]")

   # Menú principal
    def menu(self):
        """Muestra el menú y ejecuta el ejercicio seleccionado."""
        opciones = {
            1: self.ejercicio_1, 2: self.ejercicio_2, 3: self.ejercicio_3,
            4: self.ejercicio_4, 5: self.ejercicio_5, 6: self.ejercicio_6,
        }
        while True:
            print("\n" + "=" * 52)
            print(" TALLER PYTHON - " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            print("=" * 52)
            for k in opciones:
                print(f"  {k}. Ejercicio {k}")
            print("  0. Salir")
            op = self.leer_entero("Seleccione una opción: ", 0)
            if op == 0:
                print("Programa finalizado.")
                break
            if op in opciones:
                print()
                opciones[op]()
            else:
                print("Opción no válida.")


if __name__ == "__main__":
    Ejercicios().menu()

#-----------------------------------------------------------------------------------------------------------------#
                                             #PSEUDOCODIGO
                         #EJERCICIO 1
  #INICIO
  #suma <- 0
  #cantidad <- 0
  #LEER edad
  #MIENTRAS edad <> 0 HACER
  #suma <- suma + edad
  #cantidad <- cantidad + 1
  #LEER edad
  #FIN MIENTRAS
  #SI cantidad > 0 ENTONCES
  #promedio <- suma / cantidad
  #ESCRIBIR promedio
  #SINO
  #ESCRIBIR "No se ingresaron datos"
  #FIN SI
  #FIN
                         #EJERCICIO 2
  #INICIO
  #LEER n
  #suma <- 0
  #PARA i <- 1 HASTA n HACER
  #LEER edad
  #suma <- suma + edad
  #FIN PARA
  #promedio <- suma / n
  #ESCRIBIR promedio
  #FIN

                         #EJERCICIO 3
#INICIO
#LEER n
#suma <- 0
#PARA i <- 1 HASTA n HACER
#REPETIR  
#LEER nota
#SI nota < 0 O nota > 5 ENTONCES
#ESCRIBIR "Nota fuera de rango"
#FIN SI
#HASTA QUE nota >= 0 Y nota <= 5
#suma <- suma + nota
#FIN PARA
#promedio <- suma / n
#ESCRIBIR promedio
#FIN
                          #EJERCICIO 4
#INICIO
#LEER n
#PARA i <- 1 HASTA n HACER
#LEER nombre[i]
#LEER edad[i]
#FIN PARA
#PARA i <- 1 HASTA n HACER
#ESCRIBIR i, nombre[i], edad[i]
#FIN PARA
#FIN
                          #EJERCICIO 5

#INICIO
#LEER filas, columnas
#PARA i <- 0 HASTA filas - 1 HACER
#PARA j <- 0 HASTA columnas - 1 HACER
#LEER A[i][j]
#FIN PARA
#FIN PARA
#PARA i <- 0 HASTA filas - 1 HACER
#PARA j <- 0 HASTA columnas - 1 HACER
#LEER B[i][j]
#FIN PARA
#FIN PARA
#PARA i <- 0 HASTA filas - 1 HACER
#PARA j <- 0 HASTA columnas - 1 HACER
#C[i][j] <- A[i][j] + B[i][j]
#ESCRIBIR C[i][j]
#FIN PARA
#FIN PARA
#FIN
                         #EJERCICIO 6
#INICIO
#LEER tabla, limite
#PARA i <- 1 HASTA limite HACER
#multiplicadores[i] <- i
#factores[i] <- [tabla, i]
#resultados[i] <- tabla * i
#FIN PARA
#PARA i <- 1 HASTA limite HACER
#ESCRIBIR factores[i], resultados[i]
#FIN PARA
#FIN

