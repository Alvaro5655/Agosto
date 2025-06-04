def imprimir(altura):
    for i in range(altura):
        print(' '*(altura-i-1) + '*'*(2*i+1))

    for _ in range(max(1, altura//3)):
        print(' '*(altura-1) + '|')  

imprimir(int(input("Ingresa su Tamaño: ")))