while (True):
    print ("_________________")
    print ("escolha um exercio")
    print ("'1'idade")
    print ("'2'velocidade")
    print ("'3'salario")
    print ("'4'bonus")
    print ("_________________")

    pergunta = int(input())

    if pergunta == 1:
        idade= int(input("insira sua idade: "))

        if idade>=18:
            print("acesso liberado")
            
        elif idade<18:
            print ("acesso negado")
    


    elif pergunta == 2:
        velocidade=int(input("insira a velociade do carro: "))
        if velocidade > 80:
          print("multado")
          print ("limite de velocidade ultrapassado")
        elif velocidade <=80:
         print ("ta de boa🤙🚗")







    elif pergunta == 3:
        salario = int(input("insira seu salario: "))


        reajuste1= salario *1.10
        reajuste2= salario *1.15


        if salario>=8250:
            print("valor do seu antigo salario", salario)
            print("valor do seu salario com reajuste de 10%:",reajuste1)
    

        elif salario<8250:
            print("valor do seu antigo salario", salario)
            print("valor do seu salario com reajuste de 15%:",reajuste2)


    elif pergunta == 4:
        print("so eram 3 exercicios kkkk")

        break


