while True:
    idade= int(input("insira sua idade: "))

    if idade>=18:
        print("acesso liberado")
        break
    elif idade<18:
        print ("acesso negado")