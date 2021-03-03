"""
Nome : Gisele Manuel
Objetivo: Criar um Jogo com as expecificações abaixo:
Descrição:
Fazer um jogo com vários finais baseados em escolhas.
O jogo precisa ter mais de um final e precisa seguir este fluxo padrão:
Fluxo: 1. Mostrar o texto explicando o cenário atual
2. Fornecer opções de tomada de decisão
3. Receber a escolha da pessoa usuária
4. Se for um final de jogo, mostrar mensagem de fim de jogo (venceu, ganhou etc)
e mostrar pelo menos uma única opção, que é a de jogar novamente
5. Se não, voltar para o primeiro passo

A história do jogo precisa ter:

* Um tema específico : Diversidade
* Enredo : E-learning
* Título: Diversidadde e Equidade nas organizações
* Locais diferentes (pelo menos 3)
* Personagens diferentes (pelo menos 3)
* Condições de vitória (pelo menos 2)
* Condições de derrota (pelo menos 4)

string = 'Python é vida'

for letra in string:
    time.sleep(0.10)
    print(f'{letra}', end='')
    time.sleep(0.10)

"""
import os
import time
from time import sleep

# função que limpa as informação inseridas e exibidas no terminal


def limpar_tela():
    if os.name == 'nt':  # limpa tela para sistemas windows
        os.system("cls")
    else:
        os.system("clear")


def escrever(texto):

    for letra in texto:
        time.sleep(0.01)
        print(f'{letra}', end='')
        time.sleep(0.01)


def encerrar_jogo():
    limpar_tela()
    print('Encerrando o jogo...')
    sleep(2)
    print('Obrigada por Jogar !')

# cabeçalho do programa


def cabecalho_programa():
    print('-' * 81)
    print(f'{"E-learning : DIVERSIDADE E EQUIDADE NAS ORGANIZAÇÕES":^81}')
    print('-' * 81)


# resumo do tema do e-learning


def introducao_jogo():
    print('-' * 81)
    print("| A proposta deste e-learning é apresentar  o tema diversidade nas organizações  |")
    print("| apresentaremos conceitos sobre noção de Cultura Organizacional para entender   |")
    print("| como agir em relação ao tema. O objetivo é trazer orientação para identificar  |")
    print("| o que pode ser revisto nas rotinas das empresas e quais são as melhores formas |")
    print("| de proporcionar relações (não somente no trabalho) que valorizem as diferenças.|")
    print('-' * 81)

# função que pergunta ao usuário se ele deseja continuar o jogo


def continuar_jogo():

    while True:
        opcao = str(input('Deseja continuar [S/N]: ')).upper()
        if opcao == "S":
            escolher_avatar()
            break
        elif opcao == "N":
            encerrar_jogo()
            break
        elif opcao != "S":
            limpar_tela()
            print(f'A opção {opcao} não existe, tente novamente.')

# função que permite que o usuário escolha com qual avatar ele deseja jogar no e-learning.


def escolher_avatar():
    limpar_tela()
    print('-' * 74)
    print("| Seja bem-vinde ao E-learning DIVERSIDADE E EQUIDADE NAS ORGANIZAÇÕES   |")
    print('-' * 74)
    print(f'{"selecione abaixo o(a) personagem que irá lhe apresentar nosso conteúdo":^74}')
    while True:
        personagem = int(input('[0] Gabriela\n[1] Paulo\n[2] Denise\n[3] Sair do programa\nInforme sua opção: '))
        limpar_tela()
        if personagem == 0:
            personagem = "Gabriela"
            print('Olá, eu sou a Gabriela !\n'
                  'Estarei contigo nesta jornada de conhecimento sobre\n'
                  'esse mundo da diversidade. Haverá textos para introdução\n'
                  'do assunto e Quiz, para testar se você está craque no assunto.')
            op = str(input('Vamos continuar [S/N] : ')).upper()
            limpar_tela()
            if op == "S":
                conteudo_fase_um(personagem)
            elif op != "S":
                while True:
                    print(f'A opção {op} não existe.')
                    op = str(input('Deseja continuar?[S/N]: ')).upper()
                    limpar_tela()
                    if op == "S":
                        conteudo_fase_um(personagem)
                    elif op == "N":
                        encerrar_jogo()
                        break
            else:
                encerrar_jogo()
            break
        elif personagem == 1:
            personagem = 'Paulo'
            print('Olá, eu sou o Paulo !\n'
                  'Estarei contigo nesta jornada de conhecimento sobre\n'
                  'esse mundo da diversidade. Haverá textos para introdução\n'
                  'do assunto e Quiz, para testar se você está craque no assunto.')
            op = str(input('Vamos continuar [S/N] : ')).upper()
            limpar_tela()
            if op == "S":
                conteudo_fase_um(personagem)
            elif op != "S":
                while True:
                    print(f'A opção {op} não existe.')
                    op = str(input('Deseja continuar?[S/N]: ')).upper()
                    limpar_tela()
                    if op == "S":
                        conteudo_fase_um(personagem)
                    elif op == "N":
                        encerrar_jogo()
                        break
            else:
                encerrar_jogo()
            break
        elif personagem == 2:
            personagem = 'Denise'
            print('Olá, eu sou a Denise !\n'
                  'Estarei contigo nesta jornada de conhecimento sobre\n'
                  'esse mundo da diversidade. Haverá textos para introdução\n'
                  'do assunto e Quiz, para testar se você está craque no assunto.')
            op = str(input('Vamos continuar [S/N] : ')).upper()
            limpar_tela()
            if op == "S":
                conteudo_fase_um(personagem)
            elif op != "S":
                while True:
                    print(f'A opção {op} não existe.')
                    op = str(input('Deseja continuar?[S/N]: ')).upper()
                    limpar_tela()
                    if op == "S":
                        conteudo_fase_um(personagem)
                    elif op == "N":
                        encerrar_jogo()
                        break
            else:
                encerrar_jogo()
            break
        elif personagem > 3:
            print(f"Personagem {personagem} não existe!")


def conteudo_fase_um(avatar):
    placar = 0
    limpar_tela()
    print('-' * 60)
    print(f'{"PRIMEIRA FASE - Introdução de Conceitos ":^60}')
    print('-' * 60)
    limpar_tela()

    # apresentação do tema DIVERSIDADE
    texto_diversiade = 'DIVERSIDADE, o que é diverso, diferença, dessemelhança, variação, variedade, multiplicidade.' + '\n' + 'As diferenças entre  as pessos podem ser de muitas ordens:' + '\n' + 'Física, Morais, Religosas, Culturais , Ideologicas.'
    print(f'{avatar} diz:')
    escrever(texto_diversiade)
    print('\n')
    sleep(1)

    op = str(input("Topa um Quiz sobre este tema [S/N]: ")).upper()
    if op == "S":  # Quiz do tema DIVERSIDADE
        limpar_tela()
        equiddade = str(input("A Diversidade pode ser de muitas orderns.\nEscolha uma alternativa que melhor represente a diversidade: \n[A] Física, Morais, Religosas, Culturais , Musicalidade.\n[B] Física, Morais, Religosas, Artística , Ideologicas.\n[C] Física, Morais, Temporal, Culturais , Ideologicas.\n[D] Física, Morais, Religosas, Culturais , Ideologicas.\nEscolha  uma  alternativa:")).upper()
        if equiddade == "A":
            print('Você errou!\nA alternativa correrta é a\n[D] Física, Morais, Religosas, Culturais')
        elif equiddade == "B":
            print('Você errou!\nA alternativa correrta é a\n[D] Física, Morais, Religosas, Culturais')
        elif equiddade == "C":
            print('Você errou!\nA alternativa correrta é a\n[D] Física, Morais, Religosas, Culturais')
        if equiddade == "D":
            placar += 10
            print(f'Você ACERTOU!O seu placar é de {placar} pontos.')
    elif op != "S":
        while True:
            print(f'A opção {op} não existe.')
            op = str(input('Deseja continuar?[S/N]: ')).upper()
            limpar_tela()
            if op == "S":
                quiz_diversidade()
                break
            elif op == "N":
                encerrar_jogo()
                break

    # apresentação do tema Grupo minoritários
    texto_grupo_minoritario = 'Olá Olá Olá'
    op = str(input('\nVamos continuar?[S/N]: ')).upper()
    limpar_tela()
    if op == 'S':
        print(f'{avatar} diz:')
        escrever(texto_grupo_minoritario)
    elif op != 'S':
        while True:
            print(f'A opção {op} não existe.\n')
            op = str(input('Deseja continuar?[S/N]: ')).upper()
            if op == 'S':
                print(f'{avatar} diz:')
                escrever(texto_grupo_minoritario)
                break
            elif op == 'N':
                encerrar_jogo()


def quiz_diversidade():
    pontos = 0
    limpar_tela()
    equiddade = str(input("A Diversidade pode ser de muitas orderns.\nEscolha uma alternativa que melhor represente a diversidade: \n[A] Física, Morais, Religosas, Culturais , Musicalidade.\n[B] Física, Morais, Religosas, Artística , Ideologicas.\n[C] Física, Morais, Temporal, Culturais , Ideologicas.\n[D] Física, Morais, Religosas, Culturais , Ideologicas.\nEscolha  uma  alternativa:")).upper()
    if equiddade == "A":
        print('Você errou!\nA alternativa correrta é a\n[D] Física, Morais, Religosas, Culturais')
    elif equiddade == "B":
        print('Você errou!\nA alternativa correrta é a\n[D] Física, Morais, Religosas, Culturais')
    elif equiddade == "C":
        print('Você errou!\nA alternativa correrta é a\n[D] Física, Morais, Religosas, Culturais')
    if equiddade == "D":
        pontos += 10
        print(f'Você ACERTOU!O seu placar é de {pontos} pontos.')


cabecalho_programa()
introducao_jogo()
continuar_jogo()