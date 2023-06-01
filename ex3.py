mulher = 0
homem = 0
grupo = 0
idadeM = 0
idadeH = 0
idadeG = 0
for i in range(1,3):
    print("Informe os dados: \n f \n m")
    sexo = str(input("Digite o gênero: "))
    idade = int(input("Digite a idade: "))
    idadeG += idade
    if sexo == "f":
     mulher +=1
     idadeM += idade
    elif sexo == "m":
     homem +=1
     idadeH += idade

mediaM = idadeM / mulher
mediaH = idadeH / homem
mediag = idadeG / 10
print("Média das mulheres: ",mediaM,"Média dos Homens", mediaH, "Média do grupo",mediag)
