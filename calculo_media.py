lista_idades = []
quantidade_idades = int(input("Quantas idades serâo calculadas: "))

for i in range(0,quantidade_idades):
    idade = int(input("Digite a idade: "))
    lista_idades.append(idade)

soma_idades = sum(lista_idades)

media_idades = soma_idades/quantidade_idades

print("A media das idades é:" + str(media_idades))
