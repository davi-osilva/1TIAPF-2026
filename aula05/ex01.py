with open("exercicio.txt", "r", encoding="UTF-8") as arquivo:
    conteudo = arquivo.read().replace(" ", "")
    letras = len(conteudo)
    print(f"Existem {letras} letras neste arquivo")