nome = input("Digite seu nome: ")

with open("meuarquivo.txt", "w", encoding="UTF-8") as arquivo:
    arquivo.write("Olá, mundo!\n")
    arquivo.write("Este é um arquivo de texto\n")
    arquivo.write(f"Criado por {nome}")

