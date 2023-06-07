from farentheit_celsius import fahrenheit_to_celsius


if __name__=="__main__":

    tempeture_fahrenheit = float(input('Ingrese la temperatura en grados fahrenheit: '))

    result = fahrenheit_to_celsius(tempeture_fahrenheit)

    print(f'El equivalente en grados celsius de {tempeture_fahrenheit} F° es: {result}')