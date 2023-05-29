salario = int(input("insira seu salario: "))


reajuste1= salario *1.10
reajuste2= salario *1.15


if salario>=8250:
    print("valor do seu salario com reajuste de 10%:",reajuste1)

elif salario<8250:
    print("valor do seu salario com reajuste de 15%:",reajuste2)
    
   