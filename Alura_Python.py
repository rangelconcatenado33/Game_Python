def jogar():
    import random


    print("Bem vindos ao Jogo de adivinhação")
    print("***********************************")
    print("Escolha um nível:")
    print("***********************************")
    print("Níveis:")
    print("1 (Fácil) 2(Médio) 3(Díficil)")
    nivel = input('Digite aqui o número escolhido: ')
    nivel_formt = int(nivel)

    if nivel_formt == 1:
            chances = 10
            pontos = 1000
    elif nivel_formt == 2:
            chances = 6
            pontos = 1000
    elif nivel_formt == 3:
            chances = 3
            pontos = 1000

    for tentativa in range(1, chances + 1):

            print(f'Tentativa: {tentativa} de {chances}')
            print(f'Pontos: {pontos}')

            numero_tentativa_formatado = int(tentativa)

            numero = input("Digite um número de 1 à 100:")

            numero_formatado = int(numero)

            if numero_formatado < 1 or numero_formatado > 100:
                print('Por favor, digite um número de 1 à 100');
                continue

            else:

                resposta = random.randrange(1, 101)
                if numero_formatado != resposta:
                    pontos = pontos - 50
                elif numero_formatado == resposta:
                    pontos = pontos + 50

                print(f'você digitou o numero: {numero}')

                acertou = numero_formatado == resposta
                menos = numero_formatado < resposta
                mais = numero_formatado > resposta

                if acertou:
                    print("você acertou!")
                    print('***********************************')
                    print("Obrigado pela participação")
                    break
                elif mais:
                    print("Errou! Valor maior que o correto")
                elif menos:
                    print("Errado! Valor menor que o esperado!")

            print('***********************************')
            print("Obrigado pela participação")
if (__name__=='__main__'):
    jogar()

