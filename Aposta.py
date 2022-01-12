from random import randint
from os import system
from time import sleep


def lotosena():
    escolha1 = int(input('Digite o 1º número: '))
    escolha2 = int(input('Digite o 2º número: '))
    escolha3 = int(input('Digite o 3º número: '))
    escolha4 = int(input('Digite o 4º número: '))
    escolha5 = int(input('Digite o 5º número: '))
    escolha6 = int(input('Digite o 6º número: '))
    print('\n')
    print('Números Sorteados:')
    contador_lotosena = 0
    while contador_lotosena < 6:
        num = randint(0, 20)
        print(f'{num}\t', end="")
        contador_lotosena += 1
    print(f'\n\nNúmeros Escolhidos:\n{escolha1}\t{escolha2}\t{escolha3}\n{escolha4}\t{escolha5}\t{escolha6}\n')


def lotogg():
    #Desculpe a quantidade de escolha que fiz, na hora não sabia o que fazer aqui :/
    escolha1 = int(input('Digite o 1º número: '))
    escolha2 = int(input('Digite o 2º número: '))
    escolha3 = int(input('Digite o 3º número: '))
    escolha4 = int(input('Digite o 4º número: '))
    escolha5 = int(input('Digite o 5º número: '))
    escolha6 = int(input('Digite o 6º número: '))
    escolha7 = int(input('Digite o 7º número: '))
    escolha8 = int(input('Digite o 8º número: '))
    escolha9 = int(input('Digite o 9º número: '))
    escolha10 = int(input('Digite o 10º número: '))
    escolha11 = int(input('Digite o 11º número: '))
    escolha12 = int(input('Digite o 12º número: '))
    escolha13 = int(input('Digite o 13º número: '))
    escolha14 = int(input('Digite o 14º número: '))
    escolha15 = int(input('Digite o 15º número: '))
    print('\n')
    print('Números Sorteados:')
    contador_lotogg = 0
    while contador_lotogg < 15:
        num = randint(0, 15)
        print(f'{num}\t', end="")
        contador_lotogg += 1
    print(f'\n\nNúmeros Escolhidos:\n{escolha1}\t{escolha2}\t{escolha3}\t{escolha4}\t{escolha5}\t{escolha6}\t{escolha7}\n{escolha8}\t{escolha9}\t{escolha10}\t{escolha11}\t{escolha12}\t{escolha13}\t{escolha14}\t{escolha15}')


def lotomana():
    #Denovo, so que maior :/
    escolha1 = int(input('Digite o 1º número: '))
    escolha2 = int(input('Digite o 2º número: '))
    escolha3 = int(input('Digite o 3º número: '))
    escolha4 = int(input('Digite o 4º número: '))
    escolha5 = int(input('Digite o 5º número: '))
    escolha6 = int(input('Digite o 6º número: '))
    escolha7 = int(input('Digite o 7º número: '))
    escolha8 = int(input('Digite o 8º número: '))
    escolha9 = int(input('Digite o 9º número: '))
    escolha10 = int(input('Digite o 10º número: '))
    escolha11 = int(input('Digite o 11º número: '))
    escolha12 = int(input('Digite o 12º número: '))
    escolha13 = int(input('Digite o 13º número: '))
    escolha14 = int(input('Digite o 14º número: '))
    escolha15 = int(input('Digite o 15º número: '))
    escolha16 = int(input('Digite o 16º número: '))
    escolha17 = int(input('Digite o 17º número: '))
    escolha18 = int(input('Digite o 18º número: '))
    escolha19 = int(input('Digite o 19º número: '))
    escolha20 = int(input('Digite o 20º número: '))
    print('\n')
    print('Números Sorteados:\n')
    contador_lotomana = 0
    while contador_lotomana < 20:
        num = randint(0, 20)
        print(f'{num}\t', end="")
        contador_lotomana += 1
    print(f'\n\nNúmeros Escolhidos:\n{escolha1}\t{escolha2}\t{escolha3}\t{escolha4}\t{escolha5}\t{escolha6}\t{escolha7}\n{escolha8}\t{escolha9}\t{escolha10}\t{escolha11}\t{escolha12}\t{escolha13}\t{escolha14}\t{escolha15}\n{escolha16}\t{escolha17}\t{escolha18}\t{escolha19}\t{escolha20}')

saldo = 0.00
contador_menu = 0
while contador_menu == 0:
    cont = 0
    print('\n===========================================================')
    print('\n\t\tApostas - Loteria')
    print('\n===========================================================')
    sleep(1)
    print('\n\nEscolha uma das opções:\n1 - Jogar\t2 - Saldo\t3 - Depositar\t4 - Sacar\n\n')
    escolha_usuario = input('Qual das opções acima o senhor vai querer? ')
    escolha_usuario = escolha_usuario.lower()
    if escolha_usuario == "jogar" or escolha_usuario == "jogo" or escolha_usuario == "1":
        os = input('Digite qual é o seu sistema operacional: ')
        os = os.lower()
        if os == "windows":
            while cont == 0:
                print('\nApostas:\n1 - LotoSena R$15.00\t2 - LotoGG R$5.00\t3 - LotoMana R$13.00\n')
                escolha = input('Digite o nome da aposta selecionada: ')
                escolha = escolha.lower()
                if escolha == "lotosena" or escolha == "1":
                    saldo -= 15.00
                    codigo_aposta = randint(18763, 198264839823)
                    print('\nLotoSena - Você escolhe 6 números de 0 até 20, e caso acerte os 6 números que o sistema irá sortear, você irá ganhar R$31.000.000 no seu saldo atual, caso acerte 5 números, você ganha R$100.000, caso acerte 4 números, você ganha R$10.000,00 e se você acertar abaixo desses números, você perde! boa sorte!\n\n')
                    sleep(3)
                    print(f'Seu saldo atual é de R${saldo}\nAposta número {codigo_aposta}\n\n')
                    sleep(5)
                    lotosena()
                    numeros_acertados = int(input('\nQuantos números você acertou? '))
                    if numeros_acertados == 6:
                        print('Parabéns!!! Você marcou uma sena na sua aposta, acertou todos os números, você acaba de ganhar os R$31.000.000,00!!!!')
                        codigo = int(input('Para isso, por favor, digite o código da sua aposta corretamente! ou então será anulada: '))
                        if codigo == codigo_aposta:
                            system("cls")
                            print('Verificando o código, aguarde...')
                            sleep(4)
                            saldo += 31000000.00
                            print('Transferência realizada com sucesso!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("cls")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("cls")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("cls")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')
                        else:
                            system("cls")
                            print('Verificando o código, aguarde...')
                            sleep(6)
                            print('Código da aposta incorreto! aposta anulada!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("cls")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("cls")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("cls")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                    elif numeros_acertados == 5:
                        print('Parabéns! Você acertou 5 números, marcando assim uma quina e ganhando R$100.000,00')
                        codigo = int(input('Para isso, por favor, digite o código da sua aposta corretamente! ou então será anulada: '))
                        if codigo == codigo_aposta:
                            system("cls")
                            print('Verificando o código, aguarde...')
                            sleep(4)
                            saldo += 100000.00
                            print('Tranferência realizada com sucesso!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("cls")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("cls")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("cls")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')
                        else:
                            system("cls")
                            print('Verificando o código, aguarde...')
                            sleep(6)
                            print('Código da aposta incorreto! aposta anulada!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("cls")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("cls")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("cls")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                    elif numeros_acertados == 4:
                        print('Você marcou uma quadra, Parabéns! ganhando R$10.000,00 em sua conta')
                        codigo = int(input('Para isso, por favor, digite o código da sua aposta corretamente! ou então será anulada: '))
                        if codigo == codigo_aposta:
                            system("cls")
                            print('Verificando o código, aguarde...')
                            sleep(4)
                            saldo += 10000.00
                            print('Transferência realizada com sucesso!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("cls")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("cls")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("cls")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                        else:
                            system("cls")
                            print('Verificando o código, aguarde...')
                            sleep(6)
                            print('Código da aposta incorreto! aposta anulada!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("cls")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("cls")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("cls")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                    elif numeros_acertados < 4:
                        system("cls")
                        print('Infelizmente, você não ganhou dessa vez, mas não desista, tente novamente! Boa Sorte :)\n\n')
                        apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                        apostar_novamente = apostar_novamente.lower()
                        if apostar_novamente == "sim":
                            system("cls")
                            cont = 0
                            contador_menu = 0
                        elif apostar_novamente == "nao" or apostar_novamente == "não":
                            menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                            menu = menu.lower()
                            if menu == "s" or menu == "sim":
                                system("cls")
                                cont = 1
                                contador_menu = 0
                            else:
                                system("cls")
                                cont = 1
                                contador_menu = 1
                        else:
                            print('Resposta incorreta ou inválida!')
                    else:
                        system("cls")
                        print('Valor incorreto, aposta anulada!\n\n')
                        apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                        apostar_novamente = apostar_novamente.lower()
                        if apostar_novamente == "sim":
                            system("cls")
                            cont = 0
                            contador_menu = 0
                        elif apostar_novamente == "nao" or apostar_novamente == "não":
                            menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                            menu = menu.lower()
                            if menu == "s" or menu == "sim":
                                system("cls")
                                cont = 1
                                contador_menu = 0
                            else:
                                system("cls")
                                cont = 1
                                contador_menu = 1
                        else:
                            print('Resposta incorreta ou inválida!')

                if escolha == "lotogg" or escolha == "2":
                    saldo -= 5.00
                    codigo_aposta = randint(32182643, 2747232668172)
                    print('\nLotoGG - Você deve apostar 15 números para esse jogo, caso acerte 11 números, você ganha R$5,00, o dinheiro de volta basicamente, e caso seja 12 números você ganha R$1.000,00, caso acerte 13 você ganha R$20.000,00, caso acerte 14 números você ganha R$50.000,00 e caso acerte todos os 15 números sorteados, você ganha R$100.000,00 em seu saldo aqui no nosso sistema. Boa Sorte!\n\n')
                    sleep(3)
                    print(f'Seu saldo atual é de R${saldo}\nAposta número {codigo_aposta}\n\n')
                    sleep(5)
                    lotogg()
                    numeros_acertados = int(input('\nQuantos números você acertou? '))
                    if numeros_acertados == 15:
                        print('Parabéns!!! Você marcou uma sena na sua aposta, acertou todos os números, você acaba de ganhar os R$100.000,00!!!!')
                        codigo = int(input('Para isso, por favor, digite o código da sua aposta corretamente! ou então será anulada: '))
                        if codigo == codigo_aposta:
                            system("cls")
                            print('Verificando o código, aguarde...')
                            sleep(4)
                            saldo += 100000.00
                            print('Transferência realizada com sucesso!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("cls")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("cls")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("cls")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')
                        else:
                            system("cls")
                            print('Verificando o código, aguarde...')
                            sleep(6)
                            print('Código da aposta incorreto! aposta anulada!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("cls")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("cls")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("cls")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                    elif numeros_acertados == 14:
                        print('Parabéns!! Você acertou 14 números, marcando e ganhando R$50000,00')
                        codigo = int(input('Para isso, por favor, digite o código da sua aposta corretamente! ou então será anulada: '))
                        if codigo == codigo_aposta:
                            system("cls")
                            print('Verificando o código, aguarde...')
                            sleep(4)
                            saldo += 50000.00
                            print('Tranferência realizada com sucesso!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("cls")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("cls")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("cls")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')
                        else:
                            system("cls")
                            print('Verificando o código, aguarde...')
                            sleep(6)
                            print('Código da aposta incorreto! aposta anulada!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("cls")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("cls")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("cls")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                    elif numeros_acertados == 13:
                        print('Meus Parabéns! Acertando os 13 números sorteados, você ganhará R$20.000,00 na sua conta!!')
                        codigo = int(input('Para isso, por favor, digite o código da sua aposta corretamente! ou então será anulada: '))
                        if codigo == codigo_aposta:
                            system("cls")
                            print('Verificando o código, aguarde...')
                            sleep(4)
                            saldo += 20000.00
                            print('Transferência realizada com sucesso!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("cls")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("cls")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("cls")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                        else:
                            system("cls")
                            print('Verificando o código, aguarde...')
                            sleep(6)
                            print('Código da aposta incorreto! aposta anulada!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("cls")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("cls")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("cls")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                    elif numeros_acertados == 12:
                        print('Parabéns! Você acertou 12 números sorteados e ganhou R$1.000,00 em seu saldo!')
                        codigo = int(input('Para isso, por favor, digite o código da sua aposta corretamente! ou então será anulada: '))
                        if codigo == codigo_aposta:
                            system("cls")
                            print('Verificando o código, aguarde...')
                            sleep(4)
                            saldo += 1000.00
                            print('Transferência realizada com sucesso!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("cls")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("cls")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("cls")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')
                        else:
                            system("cls")
                            print('Verificando o código, aguarde...')
                            sleep(6)
                            print('Código da aposta incorreto! aposta anulada!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("cls")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("cls")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("cls")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                    elif numeros_acertados == 11:
                        print('Muito bom! você acertando os 11 números sorteados, você tem o seu dinheiro de volta, ou seja, R$5,00 de volta na sua conta!')
                        codigo = int(input('Para isso, por favor, digite o código da sua aposta corretamente! ou então será anulada: '))
                        if codigo == codigo_aposta:
                            system("cls")
                            print('Verificando o código, aguarde...')
                            sleep(4)
                            saldo += 5.00
                            print('Transferência realizada com sucesso!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("cls")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("cls")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("cls")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')
                        else:
                            system("cls")
                            print('Verificando o código, aguarde...')
                            sleep(6)
                            print('Código da aposta incorreto! aposta anulada!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("cls")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("cls")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("cls")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                    elif numeros_acertados < 11:
                        system("cls")
                        print('Infelizmente, você não ganhou dessa vez, mas não desista, tente novamente! Boa Sorte :)\n\n')
                        apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                        apostar_novamente = apostar_novamente.lower()
                        if apostar_novamente == "sim":
                            system("cls")
                            cont = 0
                            contador_menu = 0
                        elif apostar_novamente == "nao" or apostar_novamente == "não":
                            menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                            menu = menu.lower()
                            if menu == "s" or menu == "sim":
                                system("cls")
                                cont = 1
                                contador_menu = 0
                            else:
                                system("cls")
                                cont = 1
                                contador_menu = 1
                        else:
                            print('Resposta incorreta ou inválida!')

                    else:
                        system("cls")
                        print('Valor incorreto, aposta anulada!\n\n')
                        apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                        apostar_novamente = apostar_novamente.lower()
                        if apostar_novamente == "sim":
                            system("cls")
                            cont = 0
                            contador_menu = 0
                        elif apostar_novamente == "nao" or apostar_novamente == "não":
                            menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                            menu = menu.lower()
                            if menu == "s" or menu == "sim":
                                system("cls")
                                cont = 1
                                contador_menu = 0
                            else:
                                system("cls")
                                cont = 1
                                contador_menu = 1
                        else:
                            print('Resposta incorreta ou inválida!')

                if escolha == "lotomana" or escolha == "3":
                    saldo -= 13.00
                    codigo_aposta = randint(21983675, 672838029463845)
                    print('\nLotoMana - Escolha 20 números para realizar a aposta, irá ser sorteado os 20 números, caso você acerte todos os 20 números, você ganha R$1.000.000,00, caso acerte 15 números, você ganha R$500.000,00 e se você acertar 10 números, ganha R$250.000,00\n\n')
                    sleep(3)
                    print(f'Seu saldo atual é de R${saldo}\nAposta número {codigo_aposta}\n\n')
                    sleep(5)
                    lotomana()
                    numeros_acertados = int(input('\nQuantos números você acertou? '))
                    if numeros_acertados == 20:
                        print('Parabéns!!! Você acertou todos os números, sendo assim, será adicionado R$1.000.000,00 na sua conta!!!!\n')
                        codigo = int(input('Para isso, por favor, digite o código da sua aposta corretamente! ou então será anulada: '))
                        if codigo == codigo_aposta:
                            system("cls")
                            print('Verificando o código, aguarde...')
                            sleep(4)
                            saldo += 1000000.00
                            print('Transferência realizada com sucesso!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("cls")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("cls")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("cls")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')
                        else:
                            system("cls")
                            print('Verificando o código, aguarde...')
                            sleep(6)
                            print('Código da aposta incorreto! aposta anulada!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("cls")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("cls")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("cls")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                    elif numeros_acertados == 15:
                        print('Parabéns!! Você acertou os 15 números, o saldo de R$500.000,00 será adicionado a sua conta!\n')
                        codigo = int(input('Para isso, por favor, digite o código da sua aposta corretamente! ou então será anulada: '))
                        if codigo == codigo_aposta:
                            system("cls")
                            print('Verificando o código, aguarde...')
                            sleep(4)
                            saldo += 500000.00
                            print('Tranferência realizada com sucesso!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("cls")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("cls")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("cls")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')
                        else:
                            system("cls")
                            print('Verificando o código, aguarde...')
                            sleep(6)
                            print('Código da aposta incorreto! aposta anulada!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("cls")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("cls")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("cls")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                    elif numeros_acertados == 10:
                        print('Meus Parabéns! Acertando os 10 números sorteados, você ganhará R$250.000,00 na sua conta!!')
                        codigo = int(input('Para isso, por favor, digite o código da sua aposta corretamente! ou então será anulada: '))
                        if codigo == codigo_aposta:
                            system("cls")
                            print('Verificando o código, aguarde...')
                            sleep(4)
                            saldo += 250000.00
                            print('Transferência realizada com sucesso!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("cls")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("cls")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("cls")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                        else:
                            system("cls")
                            print('Verificando o código, aguarde...')
                            sleep(6)
                            print('Código da aposta incorreto! aposta anulada!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("cls")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("cls")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("cls")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                    elif numeros_acertados < 10:
                        system("cls")
                        print('Infelizmente, você não ganhou dessa vez, mas não desista, tente novamente! Boa Sorte :)\n\n')
                        apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                        apostar_novamente = apostar_novamente.lower()
                        if apostar_novamente == "sim":
                            system("cls")
                            cont = 0
                            contador_menu = 0
                        elif apostar_novamente == "nao" or apostar_novamente == "não":
                            menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                            menu = menu.lower()
                            if menu == "s" or menu == "sim":
                                system("cls")
                                cont = 1
                                contador_menu = 0
                            else:
                                system("cls")
                                cont = 1
                                contador_menu = 1
                        else:
                            print('Resposta incorreta ou inválida!')

                    else:
                        system("cls")
                        print('Valor incorreto, aposta anulada!\n\n')
                        apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                        apostar_novamente = apostar_novamente.lower()
                        if apostar_novamente == "sim":
                            system("cls")
                            cont = 0
                            contador_menu = 0
                        elif apostar_novamente == "nao" or apostar_novamente == "não":
                            menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                            menu = menu.lower()
                            if menu == "s" or menu == "sim":
                                system("cls")
                                cont = 1
                                contador_menu = 0
                            else:
                                system("cls")
                                cont = 1
                                contador_menu = 1
                        else:
                            print('Resposta incorreta ou inválida!')

        elif os == "linux":
            while cont == 0:
                print('\nApostas:\n1 - LotoSena R$15.00\t2 - LotoGG R$5.00\t3 - LotoMana R$13.00\n')
                escolha = input('Digite o nome da aposta selecionada: ')
                escolha = escolha.lower()
                if escolha == "lotosena" or escolha == "1":
                    saldo -= 15.00
                    codigo_aposta = randint(18763, 198264839823)
                    print('\nLotoSena - Você escolhe 6 números de 0 até 20, e caso acerte os 6 números que o sistema irá sortear, você irá ganhar R$31.000.000 no seu saldo atual, caso acerte 5 números, você ganha R$100.000, caso acerte 4 números, você ganha R$10.000,00 e se você acertar abaixo desses números, você perde! boa sorte!\n\n')
                    sleep(3)
                    print(f'Seu saldo atual é de R${saldo}\nAposta número {codigo_aposta}\n\n')
                    sleep(5)
                    lotosena()
                    numeros_acertados = int(input('\nQuantos números você acertou? '))
                    if numeros_acertados == 6:
                        print('Parabéns!!! Você marcou uma sena na sua aposta, acertou todos os números, você acaba de ganhar os R$31.000.000,00!!!!')
                        codigo = int(input('Para isso, por favor, digite o código da sua aposta corretamente! ou então será anulada: '))
                        if codigo == codigo_aposta:
                            system("clear")
                            print('Verificando o código, aguarde...')
                            sleep(4)
                            saldo += 31000000.00
                            print('Transferência realizada com sucesso!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("clear")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("clear")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("clear")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')
                        else:
                            system("clear")
                            print('Verificando o código, aguarde...')
                            sleep(6)
                            print('Código da aposta incorreto! aposta anulada!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("clear")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("clear")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("clear")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                    elif numeros_acertados == 5:
                        print('Parabéns! Você acertou 5 números, marcando assim uma quina e ganhando R$100.000,00')
                        codigo = int(input('Para isso, por favor, digite o código da sua aposta corretamente! ou então será anulada: '))
                        if codigo == codigo_aposta:
                            system("clear")
                            print('Verificando o código, aguarde...')
                            sleep(4)
                            saldo += 100000.00
                            print('Tranferência realizada com sucesso!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("clear")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("clear")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("clear")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')
                        else:
                            system("clear")
                            print('Verificando o código, aguarde...')
                            sleep(6)
                            print('Código da aposta incorreto! aposta anulada!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("clear")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("clear")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("clear")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                    elif numeros_acertados == 4:
                        print('Você marcou uma quadra, Parabéns! ganhando R$10.000,00 em sua conta')
                        codigo = int(input('Para isso, por favor, digite o código da sua aposta corretamente! ou então será anulada: '))
                        if codigo == codigo_aposta:
                            system("clear")
                            print('Verificando o código, aguarde...')
                            sleep(4)
                            saldo += 10000.00
                            print('Transferência realizada com sucesso!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("clear")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("clear")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("clear")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                        else:
                            system("clear")
                            print('Verificando o código, aguarde...')
                            sleep(6)
                            print('Código da aposta incorreto! aposta anulada!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("clear")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("clear")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("clear")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                    elif numeros_acertados < 4:
                        system("clear")
                        print('Infelizmente, você não ganhou dessa vez, mas não desista, tente novamente! Boa Sorte :)\n\n')
                        apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                        apostar_novamente = apostar_novamente.lower()
                        if apostar_novamente == "sim":
                            system("clear")
                            cont = 0
                            contador_menu = 0
                        elif apostar_novamente == "nao" or apostar_novamente == "não":
                            menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                            menu = menu.lower()
                            if menu == "s" or menu == "sim":
                                system("clear")
                                cont = 1
                                contador_menu = 0
                            else:
                                system("clear")
                                cont = 1
                                contador_menu = 1

                        else:
                            system("clear")
                            print('Resposta incorreta ou inválida!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("clear")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("clear")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("clear")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')
                    else:
                        system("clear")
                        print('Valor incorreto, aposta anulada!\n\n')
                        apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                        apostar_novamente = apostar_novamente.lower()
                        if apostar_novamente == "sim":
                            system("clear")
                            cont = 0
                            contador_menu = 0
                        elif apostar_novamente == "nao" or apostar_novamente == "não":
                            menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                            menu = menu.lower()
                            if menu == "s" or menu == "sim":
                                system("clear")
                                cont = 1
                                contador_menu = 0
                            else:
                                system("clear")
                                cont = 1
                                contador_menu = 1
                        else:
                            print('Resposta incorreta ou inválida!')
                if escolha == "lotogg" or escolha == "2":
                    saldo -= 5.00
                    codigo_aposta = randint(32182643, 2747232668172)
                    print('\nLotoGG - Você deve apostar 15 números para esse jogo, caso acerte 11 números, você ganha R$5,00, o dinheiro de volta basicamente, e caso seja 12 números você ganha R$1.000,00, caso acerte 13 você ganha R$20.000,00, caso acerte 14 números você ganha R$50.000,00 e caso acerte todos os 15 números sorteados, você ganha R$100.000,00 em seu saldo aqui no nosso sistema. Boa Sorte!\n\n')
                    sleep(3)
                    print(f'Seu saldo atual é de R${saldo}\nAposta número {codigo_aposta}\n\n')
                    sleep(5)
                    lotogg()
                    numeros_acertados = int(input('\nQuantos números você acertou? '))
                    if numeros_acertados == 15:
                        print('Parabéns!!! Você marcou uma sena na sua aposta, acertou todos os números, você acaba de ganhar os R$100.000,00!!!!')
                        codigo = int(input('Para isso, por favor, digite o código da sua aposta corretamente! ou então será anulada: '))
                        if codigo == codigo_aposta:
                            system("clear")
                            print('Verificando o código, aguarde...')
                            sleep(4)
                            saldo += 100000.00
                            print('Transferência realizada com sucesso!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("clear")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("clear")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("clear")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')
                        else:
                            system("clear")
                            print('Verificando o código, aguarde...')
                            sleep(6)
                            print('Código da aposta incorreto! aposta anulada!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("clear")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("clear")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("clear")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                    elif numeros_acertados == 14:
                        print('Parabéns!! Você acertou 14 números, marcando e ganhando R$50000,00')
                        codigo = int(input('Para isso, por favor, digite o código da sua aposta corretamente! ou então será anulada: '))
                        if codigo == codigo_aposta:
                            system("clear")
                            print('Verificando o código, aguarde...')
                            sleep(4)
                            saldo += 50000.00
                            print('Tranferência realizada com sucesso!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("clear")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("clear")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("clear")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')
                        else:
                            system("clear")
                            print('Verificando o código, aguarde...')
                            sleep(6)
                            print('Código da aposta incorreto! aposta anulada!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("clear")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("clear")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("clear")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                    elif numeros_acertados == 13:
                        print('Meus Parabéns! Acertando os 13 números sorteados, você ganhará R$20.000,00 na sua conta!!')
                        codigo = int(input('Para isso, por favor, digite o código da sua aposta corretamente! ou então será anulada: '))
                        if codigo == codigo_aposta:
                            system("clear")
                            print('Verificando o código, aguarde...')
                            sleep(4)
                            saldo += 20000.00
                            print('Transferência realizada com sucesso!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("clear")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("clear")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("clear")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                        else:
                            system("clear")
                            print('Verificando o código, aguarde...')
                            sleep(6)
                            print('Código da aposta incorreto! aposta anulada!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("clear")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("clear")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("clear")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                    elif numeros_acertados == 12:
                        print('Parabéns! Você acertou 12 números sorteados e ganhou R$1.000,00 em seu saldo!')
                        codigo = int(input('Para isso, por favor, digite o código da sua aposta corretamente! ou então será anulada: '))
                        if codigo == codigo_aposta:
                            system("clear")
                            print('Verificando o código, aguarde...')
                            sleep(4)
                            saldo += 1000.00
                            print('Transferência realizada com sucesso!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("clear")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("clear")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("clear")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')
                        else:
                            system("clear")
                            print('Verificando o código, aguarde...')
                            sleep(6)
                            print('Código da aposta incorreto! aposta anulada!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("clear")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("clear")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("clear")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                    elif numeros_acertados == 11:
                        print('Muito bom! você acertando os 11 números sorteados, você tem o seu dinheiro de volta, ou seja, R$5,00 de volta na sua conta!')
                        codigo = int(input('Para isso, por favor, digite o código da sua aposta corretamente! ou então será anulada: '))
                        if codigo == codigo_aposta:
                            system("clear")
                            print('Verificando o código, aguarde...')
                            sleep(4)
                            saldo += 5.00
                            print('Transferência realizada com sucesso!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("clear")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("clear")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("clear")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')
                        else:
                            system("clear")
                            print('Verificando o código, aguarde...')
                            sleep(6)
                            print('Código da aposta incorreto! aposta anulada!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("clear")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("clear")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("clear")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

                    elif numeros_acertados < 11:
                        system("clear")
                        print('Infelizmente, você não ganhou dessa vez, mas não desista, tente novamente! Boa Sorte :)\n\n')
                        apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                        apostar_novamente = apostar_novamente.lower()
                        if apostar_novamente == "sim":
                            system("clear")
                            cont = 0
                            contador_menu = 0
                        elif apostar_novamente == "nao" or apostar_novamente == "não":
                            menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                            menu = menu.lower()
                            if menu == "s" or menu == "sim":
                                system("clear")
                                cont = 1
                                contador_menu = 0
                            else:
                                system("clear")
                                cont = 1
                                contador_menu = 1

                    else:
                        system("clear")
                        print('Valor incorreto, aposta anulada!\n\n')
                        apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                        apostar_novamente = apostar_novamente.lower()
                        if apostar_novamente == "sim":
                            system("clear")
                            cont = 0
                            contador_menu = 0
                        elif apostar_novamente == "nao" or apostar_novamente == "não":
                            menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                            menu = menu.lower()
                            if menu == "s" or menu == "sim":
                                system("clear")
                                cont = 1
                                contador_menu = 0
                            else:
                                system("clear")
                                cont = 1
                                contador_menu = 1
                        else:
                            print('Resposta incorreta ou inválida!')

                    if escolha == "lotomana" or escolha == "3":
                        saldo -= 13.00
                        codigo_aposta = randint(21983675, 672838029463845)
                        print('\nLotoMana - Escolha 20 números para realizar a aposta, irá ser sorteado os 20 números, caso você acerte todos os 20 números, você ganha R$1.000.000,00, caso acerte 15 números, você ganha R$500.000,00 e se você acertar 10 números, ganha R$250.000,00\n\n')
                        sleep(3)
                        print(f'Seu saldo atual é de R${saldo}\nAposta número {codigo_aposta}\n\n')
                        sleep(5)
                        lotomana()
                        numeros_acertados = int(input('\nQuantos números você acertou? '))
                        if numeros_acertados == 20:
                            print('Parabéns!!! Você acertou todos os números, sendo assim, será adicionado R$1.000.000,00 na sua conta!!!!\n')
                            codigo = int(input('Para isso, por favor, digite o código da sua aposta corretamente! ou então será anulada: '))
                            if codigo == codigo_aposta:
                                system("clear")
                                print('Verificando o código, aguarde...')
                                sleep(4)
                                saldo += 1000000.00
                                print('Transferência realizada com sucesso!\n\n')
                                apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                                apostar_novamente = apostar_novamente.lower()
                                if apostar_novamente == "sim":
                                    system("clear")
                                    cont = 0
                                    contador_menu = 0
                                elif apostar_novamente == "nao" or apostar_novamente == "não":
                                    menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                    menu = menu.lower()
                                    if menu == "s" or menu == "sim":
                                        system("clear")
                                        cont = 1
                                        contador_menu = 0
                                    else:
                                        system("clear")
                                        cont = 1
                                        contador_menu = 1
                                else:
                                    print('Resposta incorreta ou inválida!')
                            else:
                                system("clear")
                                print('Verificando o código, aguarde...')
                                sleep(6)
                                print('Código da aposta incorreto! aposta anulada!\n\n')
                                apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                                apostar_novamente = apostar_novamente.lower()
                                if apostar_novamente == "sim":
                                    system("clear")
                                    cont = 0
                                    contador_menu = 0
                                elif apostar_novamente == "nao" or apostar_novamente == "não":
                                    menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                    menu = menu.lower()
                                    if menu == "s" or menu == "sim":
                                        system("clear")
                                        cont = 1
                                        contador_menu = 0
                                    else:
                                        system("clear")
                                        cont = 1
                                        contador_menu = 1
                                else:
                                    print('Resposta incorreta ou inválida!')

                        elif numeros_acertados == 15:
                            print('Parabéns!! Você acertou os 15 números, o saldo de R$500.000,00 será adicionado a sua conta!\n')
                            codigo = int(input('Para isso, por favor, digite o código da sua aposta corretamente! ou então será anulada: '))
                            if codigo == codigo_aposta:
                                system("clear")
                                print('Verificando o código, aguarde...')
                                sleep(4)
                                saldo += 500000.00
                                print('Tranferência realizada com sucesso!\n\n')
                                apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                                apostar_novamente = apostar_novamente.lower()
                                if apostar_novamente == "sim":
                                    system("clear")
                                    cont = 0
                                    contador_menu = 0
                                elif apostar_novamente == "nao" or apostar_novamente == "não":
                                    menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                    menu = menu.lower()
                                    if menu == "s" or menu == "sim":
                                        system("clear")
                                        cont = 1
                                        contador_menu = 0
                                    else:
                                        system("clear")
                                        cont = 1
                                        contador_menu = 1
                                else:
                                    print('Resposta incorreta ou inválida!')
                            else:
                                system("clear")
                                print('Verificando o código, aguarde...')
                                sleep(6)
                                print('Código da aposta incorreto! aposta anulada!\n\n')
                                apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                                apostar_novamente = apostar_novamente.lower()
                                if apostar_novamente == "sim":
                                    system("clear")
                                    cont = 0
                                    contador_menu = 0
                                elif apostar_novamente == "nao" or apostar_novamente == "não":
                                    menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                    menu = menu.lower()
                                    if menu == "s" or menu == "sim":
                                        system("clear")
                                        cont = 1
                                        contador_menu = 0
                                    else:
                                        system("clear")
                                        cont = 1
                                        contador_menu = 1
                                else:
                                    print('Resposta incorreta ou inválida!')

                        elif numeros_acertados == 10:
                            print('Meus Parabéns! Acertando os 10 números sorteados, você ganhará R$250.000,00 na sua conta!!')
                            codigo = int(input('Para isso, por favor, digite o código da sua aposta corretamente! ou então será anulada: '))
                            if codigo == codigo_aposta:
                                system("clear")
                                print('Verificando o código, aguarde...')
                                sleep(4)
                                saldo += 250000.00
                                print('Transferência realizada com sucesso!\n\n')
                                apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                                apostar_novamente = apostar_novamente.lower()
                                if apostar_novamente == "sim":
                                    system("clear")
                                    cont = 0
                                    contador_menu = 0
                                elif apostar_novamente == "nao" or apostar_novamente == "não":
                                    menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                    menu = menu.lower()
                                    if menu == "s" or menu == "sim":
                                        system("clear")
                                        cont = 1
                                        contador_menu = 0
                                    else:
                                        system("clear")
                                        cont = 1
                                        contador_menu = 1
                                else:
                                    print('Resposta incorreta ou inválida!')

                            else:
                                system("clear")
                                print('Verificando o código, aguarde...')
                                sleep(6)
                                print('Código da aposta incorreto! aposta anulada!\n\n')
                                apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                                apostar_novamente = apostar_novamente.lower()
                                if apostar_novamente == "sim":
                                    system("clear")
                                    cont = 0
                                    contador_menu = 0
                                elif apostar_novamente == "nao" or apostar_novamente == "não":
                                    menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                    menu = menu.lower()
                                    if menu == "s" or menu == "sim":
                                        system("clear")
                                        cont = 1
                                        contador_menu = 0
                                    else:
                                        system("clear")
                                        cont = 1
                                        contador_menu = 1
                                else:
                                    print('Resposta incorreta ou inválida!')

                        elif numeros_acertados < 10:
                            system("clear")
                            print('Infelizmente, você não ganhou dessa vez, mas não desista, tente novamente! Boa Sorte :)\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("clear")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("clear")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("clear")
                                    cont = 1
                                    contador_menu = 1

                        else:
                            system("clear")
                            print('Valor incorreto, aposta anulada!\n\n')
                            apostar_novamente = input('O senhor gostaria de apostar novamente? ')
                            apostar_novamente = apostar_novamente.lower()
                            if apostar_novamente == "sim":
                                system("clear")
                                cont = 0
                                contador_menu = 0
                            elif apostar_novamente == "nao" or apostar_novamente == "não":
                                menu = input('Você deseja voltar para o menu principal?[S/N]: ')
                                menu = menu.lower()
                                if menu == "s" or menu == "sim":
                                    system("clear")
                                    cont = 1
                                    contador_menu = 0
                                else:
                                    system("clear")
                                    cont = 1
                                    contador_menu = 1
                            else:
                                print('Resposta incorreta ou inválida!')

        else:
            print('Sistema Operacional inexistente ou não encontrado pelo nosso sistema :(\n\n')
            menu = input('Deseja voltar para o menu principal?[S/N]: ')
            menu = menu.lower()
            if menu == "s" or menu == "sim":
                contador_menu = 0
                cont = 1
            else:
                cont = 1
                contador_menu = 1


    elif escolha_usuario == "saldo" or escolha_usuario == "2":
        print('\n===========================================================')
        print('\n\t\tApostas - Loteria')
        print('\n===========================================================')
        sleep(1)
        print(f'\n\nO seu saldo é R${saldo} na sua carteira atual')
        menu = input('\n\nO senhor gostaria de voltar para o menu principal?[S/N]: ')
        menu = menu.lower()
        if menu == "s" or menu == "sim":
            contador_menu = 0
        else:
            contador_menu = 1

    elif escolha_usuario == "depositar" or escolha_usuario == "deposito" or escolha_usuario == "3":
        print('\n===========================================================')
        print('\n\t\tApostas - Loteria')
        print('\n===========================================================')
        sleep(1)
        deposito = float(input('\n\nDigite quanto você deseja depositar: R$'))
        saldo = saldo + deposito
        print(f'Saldo atual: R${saldo}')
        menu = input('\n\nO senhor gostaria de voltar para o menu principal?[S/N]: ')
        menu = menu.lower()
        if menu == "s" or menu == "sim":
            contador_menu = 0
        else:
            contador_menu = 1

    elif escolha_usuario == "sacar" or escolha_usuario == "saque" or escolha_usuario == "4":
        print('\n===========================================================')
        print('\n\t\tApostas - Loteria')
        print('\n===========================================================')
        sleep(1)
        saque = float(input('\n\nDigite quanto você deseja sacar: R$'))
        saldo = saldo - saque
        print(f'Saldo atual: R${saldo}')
        menu = input('\n\nO senhor gostaria de voltar para o menu principal?[S/N]: ')
        menu = menu.lower()
        if menu == "s" or menu == "sim":
            contador_menu = 0
        else:
            contador_menu = 1

    else:
        print('Opção incorreta ou não existe em nosso sistema :(\n\n')
        menu = input('O senhor gostaria de voltar para o menu principal?[S/N]: ')
        menu = menu.lower()
        if menu == "s" or menu == "sim":
            contador_menu = 0
        else:
            contador_menu = 1


#DevLuizDaniel ;)



