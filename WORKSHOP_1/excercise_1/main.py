from sum import sum_of_two_numbers

if __name__=="__main__":
    """
    main para ejecturar el programa
    """
    number_1 = int(input('Ingrese el primer numero: '))
    number_2 = int(input('Ingrese el segundo numero: '))

    result = sum_of_two_numbers(number_1,number_2)


    print(f'El resultado es: {result}')
