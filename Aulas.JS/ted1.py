pessoas = []

for i in range(1, 5):
    print(f"\ninforme a altura e o genero da pessoa {i}!")
    altura = float(input("altura: "))
    genero = input("genero (M/F): ").upper()

    pessoas.append({"altura": altura, "genero": genero})

contador_feminino = 0
for pessoa in pessoas:
    if pessoa in pessoas:
        if pessoa["genero"] == "F":
            contador_feminino += 1


menor = pessoas[0]["altura"]
maior = pessoas[0]["altura"]
for pessoa in pessoas:
    if pessoa["altura"] < menor:
        menor = pessoa["altura"]
    if pessoa["altura"] > maior:
        maior = pessoa["altura"]

media_homens = (
    sum(p["altura"] for p in pessoas if p["genero"] == "M")
    / sum(1 for p in pessoas if p["genero"] == "M")
)


print(f"\nMédia de altura dos homens: {media_homens:.2f} m")


print(f"\nA maior e a menor altura das pessoas: {maior} e {menor}")



print(f"\nNúmero de pessoas do gênero feminino: {contador_feminino}")