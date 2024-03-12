def main(print, input, total_testes, numero_secreto):
    print('****************************************')
    print('Bem vindo ao meu joguinho de adivinhação')
    print('****************************************')

    # total_testes = 3
    teste = 1
    # numero_secreto = 5

    for teste in range(1, total_testes + 1):
        print(f'Teste: {teste} de {total_testes}')

        tentativa = int(input('Digite seu numero: '))
        print(f'Voce digitou: {tentativa}')

        if(tentativa < 1 or tentativa > 50):
            print('\n ---ATENCAO: DIGITE UM NUMERO ENTRE 1 E 50---')
            continue

        acertou = tentativa == numero_secreto
        maior = tentativa >numero_secreto
        menor = tentativa< numero_secreto

        if (acertou):
            print('\n-----Acertou-----')
            break
        else:
            if (maior):
                print('Errou, seu chute foi maior do que o numero secreto.')
            elif(menor):
                print('Errou, seu chute foi menor do que o numero secreto.')

        teste = teste +1
        
    print('\nFim de jogo!!!')