# Write a Python function called
# is_palindrome that checks if a given word is a
# palindrome. The function should have proper error handling and be tested with
# unittest


def is_palindrome(word:str):
    word = word.replace(' ','')
    word = word.lower()
    lista_1=[]
    lista_2=[]
    for caracter in range(len(word )): 
        lista_1+=word[caracter]

    y=len(lista_1)

    for i in range(len(lista_1)):
        lista_2+=lista_1[y-1]
        y=y-1

    if lista_1==lista_2:
        return True
    else:
        return False