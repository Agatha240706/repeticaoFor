z = int(input("Informe a quantidade de clientes:"))
soma =0
for n in range(1,z+1):
    temperatura = float(input("Digite a temperatura: "))
    soma += temperatura
    if temperatura <= 37.2:
        print("Esta normal")
    elif 37.3>=temperatura<38:
        print("Estado febril")
    elif  38>= temperatura <=39:
        print("com Febre")
    elif temperatura >39:
        print("Febre alta")
media = soma/z
print("A média das temperaturas é: ", media)
