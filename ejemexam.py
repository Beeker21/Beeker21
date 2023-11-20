import re

class Lectura:
    def __init__(self, grados_f):
        self.grados_f=grados_f

    @property
    def grados_c(self):
        return (self.grados_f-32)/1.8

    @property
    def estado(self):
        if self.grados_f < 35:
            return "Hipotermia"
        elif 35 <= self.grados_f < 37:
            return "Normal"
        elif 37 <= self.grados_f < 38:
            return "Febrícula"
        elif 38 <= self.grados_f < 41:
            return "Fiebre"
        else:
            return "Hiperpirexia"

    def mostrar_lectura(self):
        print(f"Farenheit: {self.grados_f:.2f}")
        print(f"Centigrados: {self.grados_c:.2f}")
        print(f"Estado: {self.estado}\n")

def capturar_f(prompt="Dame un número flotante:"):
    while True:
        try:
            dato=input(prompt)
            if not dato:
                raise ValueError("Error: El dato no puede estar vacío.")
            if not re.match(r'^\d{1,3}\.\d{1,3}$', dato):
                raise ValueError("Error: El dato debe tener el formato X.X.")
            valor = float(dato)
            if valor < 0.0 or valor > 150.0:
                raise ValueError("Error: El valor debe estar entre 0.0 y 150.0.")
            return valor
        except ValueError as e:
            print("Error:", e)
            print("Detalle: Por favor, ingresa un número válido en el rango de 0.0 a 150.0.")

lecturas=[]

while True:
    grados_f=capturar_f("Dame la temperatura del paciente: ")
    lectura=Lectura(grados_f)
    lecturas.append(lectura)

    respuesta = input("¿Desea capturar otra lectura? (Si/No): ")
    if respuesta.lower() !='si':
        break

print("\nLecturas capturadas:")
for lectura in lecturas:
    lectura.mostrar_lectura()