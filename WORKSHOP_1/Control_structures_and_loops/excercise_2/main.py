from prime_number import prime_number

if __name__=='__main__':
    number = int(input('Ingrese un numero: '))

    result = prime_number(number)
    if result is True:
        print('Es primo')
    else:
        print('No es primo')