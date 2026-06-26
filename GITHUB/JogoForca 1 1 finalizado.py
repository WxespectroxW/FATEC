import random, os.path, time

#Definição boneco
def desenhar_forca(erros):

    estagios = [
        """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
        """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
        """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
        """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
        """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
        """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
        """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
""",
        """
  +---+
  |   |
  X   |
 /|\\  |
 / \\  |
      |
=========
"""
    ]

    print(estagios[erros])

#Vai mostrar o nome e o RA no programa
print("Nome: Arthur da Silva\nRA: 1680972611001")
print("Nome: Guilherme Carniel\nRA: 1680972611006")
print("Nome: Isaac Eustáquio\nRA: 1680972611034")

print("|-------------------------|")
print("| JOGO [X]")
print("| DICAS [X]")
print("| CONTROLE DE TEMPO [X]")
print("|-------------------------|")

#verifica se o arquivo existe ou não
if not os.path.exists("Jogo.txt".upper()) :
    print("O arquivo jogo.txt, não existe")
    exit() #encerra o programa

#Executam a ação de abrir o arquivo Jogo.txt
arquivo = open("Jogo.txt".upper(), "r")

#Definir variáveis
palavras = []
dicas = []
indice_palavra_atual = -1
indice_dica = 0
dicas_usadas = []
r_usuario = ""
letras_acertadas = []
letras_erradas = []
erros = 0
max_erros = 7

# Lê o arquivo linha por linha
for linha in arquivo.readlines():
    linha = linha.strip()

    # Ignora linhas vazias
    if linha != "":

        # Se a linha começar com P:, é uma palavra
        if linha[0:2] == "P:":
            if len(palavras) < 100:
                palavra_lida = linha[2:].strip().upper()

                palavras.append(palavra_lida)

                # Cria uma lista vazia para as dicas dessa palavra
                dicas.append([])

                # Atualiza o índice da palavra atual
                indice_palavra_atual = len(palavras) - 1

        # Se a linha começar com D:, é uma dica
        elif linha[0:2] == "D:":
            if indice_palavra_atual != -1:

                # Limita até 10 dicas por palavra
                if len(dicas[indice_palavra_atual]) < 10:
                    dica_lida = linha[2:].strip()

                    dicas[indice_palavra_atual].append(dica_lida)



entrada = input("Você quer jogar? (S/N)\n").upper()

while entrada == "S":

    tempo_maximo = 60
    inicio = time.time()

    indice_sorteado = random.randint(0, len(palavras) - 1)
    palavra_sort = palavras[indice_sorteado]
    dicas_palavra = dicas[indice_sorteado]

    # Sorteia a primeira dica da rodada
    if len(dicas_palavra) > 0:
        indice_dica = random.randint(0, len(dicas_palavra) - 1)
        dicas_usadas.append(indice_dica)
    else:
        indice_dica = -1

    while erros < max_erros:

        tempo_decorrido = time.time() - inicio

        if tempo_decorrido >= tempo_maximo:
            print("\nTempo esgotado!")
            erros = max_erros
            break

        print(f"Tempo restante: {int(tempo_maximo - tempo_decorrido)} segundos")

        desenhar_forca(erros)

        ganhou = True

        for letra in palavra_sort:
            if letra in letras_acertadas:
                print(letra, end=" ")
            else:
                print("_", end=" ")
                ganhou = False

        print("")

        if ganhou == True:
            print("Você venceu! Palavra:", palavra_sort)
            break

        if indice_dica != -1:
            print("Dica:", dicas_palavra[indice_dica])

        print("Letras erradas:", letras_erradas)
        print("Erros:", erros, "/", max_erros)

        resposta = input("Digite uma letra, palavra ou DICA: ").strip().upper()

        if resposta == "DICA":
            erros = erros + 1

            if len(dicas_usadas) < len(dicas_palavra):
                while True:
                    indice_dica = random.randint(0, len(dicas_palavra) - 1)

                    if indice_dica not in dicas_usadas:
                        dicas_usadas.append(indice_dica)
                        break
            else:
                print("Não há mais dicas.")

        elif resposta == palavra_sort:
            print("Você acertou! A palavra era:", palavra_sort)
            break

        elif len(resposta) == 1:

            if resposta in letras_acertadas or resposta in letras_erradas:
                print("Letra repetida. Ignorada.")

            elif resposta in palavra_sort:
                letras_acertadas.append(resposta)

            else:
                letras_erradas.append(resposta)
                erros = erros + 1

        else:
            erros += 1
            print("Palavra errada.")

    if erros >= max_erros:
        print(f"Você perdeu! A palavra era: {palavra_sort}")

    entrada = input("\nDeseja jogar novamente? (S/N)\n").upper()
    if entrada == "S":
        erros = 0
        letras_erradas = []
        letras_acertadas = []
        dicas_usadas = []

        indice_sorteado = random.randint(0, len(palavras) - 1)
