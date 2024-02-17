def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))

area_triangulo = calcular_area_triangulo(base, altura)

print("El área es:", area_triangulo)
