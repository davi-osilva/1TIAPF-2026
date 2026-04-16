with open("meuarquivo.txt", "r", encoding="UTF-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())