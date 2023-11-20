dinero=600.00
v=50.00
# El precio no debe omitirse.
# El precio debe ser un número.
# El precio debe ser mayor a cero.
# El programa no deja de preguntar el precio, sino hasta que
# está correcto.
# Me debe mostrar errores específicos (error, causa, acción).

while True:
    _precio=input("Dame el precio por litro de gasolina: ")
    if (_precio==''):
        print("Entrada incorrecta. El precio no puede omitirse. Intenta de nuevo.")
        continue
    try:
        precio=float(_precio)
    except:
        print("Entrada incorrecta. El precio debe ser un número. Intenta de nuevo.")
        continue
    # Si llego aquí, ya tengo un valor numérico en precio.
    if (not precio>0):
        print("Entrada incorrecta. El precio debe ser mayor a cero. Intenta de nuevo.")
        continue
    # Si todo salió bien, se sale del while
    break
    
    litros=dinero/precio
    _rendimiento=input("Dame el rendimiento del coche: ")
    rendimiento=float(_rendimiento)
    d=rendimiento*litros
    t=d/v
    hh=int(t)
    mm=int((t-hh)*60)
    print(f"El recorrido será de {d:.2f} km, en {hh} horas y {mm} minutos")