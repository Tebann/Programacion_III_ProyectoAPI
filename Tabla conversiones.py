print("Tabla de conversión de Celsius a Fahrenheit")

print("Celsius    Fahrenheit")

for celsius in range(0, 101, 10): #Utilizo range() para cumplir que las temperaturas sean multiplos de 10  
    fahrenheit = (celsius * 9/5) + 32
    print(celsius,"------->",fahrenheit)
