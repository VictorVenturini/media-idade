lista_idades = []
for i in range(0,10):
    idade = int(input("Digite a idade: "))
    lista_idades.append(idade)

soma_idades = sum(lista_idades)

media_idades = soma_idades/10

print("A media das idades é:" + str(media_idades))
