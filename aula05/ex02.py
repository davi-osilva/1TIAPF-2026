with open("texto1.txt", "r", encoding="UTF-8") as arquivo:
    conteudo1 = arquivo.read()

with open("texto2.txt", "r", encoding="UTF-8") as arquivo:
    conteudo2 = arquivo.read()

with open("texto3.txt", "w", encoding="UTF-8") as arquivo:
    concatenacao = conteudo1 + "\n" + conteudo2
    arquivo.write(concatenacao)
