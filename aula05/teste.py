with open("arquivo.txt", "w", encoding="UTF-8") as file:
    file.write("Olá, mundo!")

with open("arquivo.txt", "r+", encoding="UTF-8") as file:
    conteudo = file.read()
    file.write("\nAdicionando mais conteúdo.")

with open("arquivo.txt", "a", encoding="UTF-8") as file:
    file.write("\nMais uma linha no final do arquivo.")

with open("arquivo.txt", "w") as file:
    file.write("Linha 1\n")
    file.write("Linha 2\n")
    file.write("Linha 3\n")

with open("arquivo.txt", "r") as file:
    conteudo = file.read()
    print(conteudo)

with open("arquivo.txt", "r") as file:
    linha1 = file.readline()
    linha2 = file.readline()
    linha3 = file.readline()
    print(linha1)
    print(linha2)
    print(linha3)
