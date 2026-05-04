def leer_nota(msg):
    while True:
        n = float(input(msg))
        if 0 <= n <= 20:
            return n
        else:
            print("Nota inválida")

def es_aprobado(nota):
    return nota >= 11

def clasificar_nota(nota):
    if nota >= 17:
        return "Excelente"
    elif nota >= 14:
        return "Bueno"
    elif nota >= 11:
        return "Aprobado"
    else:
        return "Desaprobado"

def calcular_promedio(suma, n):
    return suma / n

def mostrar_estadisticas(prom, mayor, menor, aprobados, total):
    print("Promedio:", prom)
    print("Mayor:", mayor)
    print("Menor:", menor)
    print("Aprobados:", aprobados)
    print("Total:", total)

# MAIN
n = int(input("Cantidad de notas: "))
suma = 0
mayor = -1
menor = 21
aprobados = 0

for i in range(n):
    nota = leer_nota("Ingrese nota: ")
    suma += nota
    
    if nota > mayor:
        mayor = nota
    if nota < menor:
        menor = nota
    
    if es_aprobado(nota):
        aprobados += 1

prom = calcular_promedio(suma, n)

mostrar_estadisticas(prom, mayor, menor, aprobados, n)