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
    quit()

# cabeçalho do programa


def cabecalho_programa():
    print('-' * 81)
    print(f'{"E-learning : DIVERSIDADE E EQUIDADE NAS ORGANIZAÇÕES":^81}')
    print('-' * 81)


def cabecalho_fase_um():
    print('-' * 100)
    print(f'{"PRIMEIRA FASE - Introdução de Conceitos ":^100}')
    print('-' * 100)


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


# função que válida se o usuário deseja continuar ou não com o avatar escolhido

def jogar_com_avatar(jogador):
    op = str(input('Vamos continuar [S/N] : ')).upper()
    limpar_tela()
    if op == "S":
        conteudo_fase_um(jogador)
    elif op == "N":
        encerrar_jogo()
    elif op != "S":
        while True:
            print(f'A opção {op} não existe.')
            op = str(input('Deseja continuar?[S/N]: ')).upper()
            limpar_tela()
            if op == "S":
                conteudo_fase_um(jogador)
            elif op == "N":
                encerrar_jogo()
                break

# função que permite que o usuário escolha com qual avatar ele deseja jogar no e-learning.


def escolher_avatar():
    limpar_tela()
    print('-' * 74)
    print("| Seja bem-vinde ao E-learning DIVERSIDADE E EQUIDADE NAS ORGANIZAÇÕES   |")
    print('-' * 74)
    print(f'{"selecione abaixo o(a) personagem que irá lhe apresentar nosso conteúdo":^74}')
    while True:
        personagem = str(input('[0] Gabriela\n[1] Paulo\n[2] Denise\n[3] Sair do programa\nInforme sua opção: '))
        limpar_tela()
        if personagem == '0':
            personagem = "Gabriela"
            print('Olá, eu sou a Gabriela !\n'
                  'Estarei contigo nesta jornada de conhecimento sobre\n'
                  'esse mundo da diversidade. Haverá textos para introdução\n'
                  'do assunto e Quiz, para testar se você está craque no assunto.')
            jogar_com_avatar(personagem)

        elif personagem == '1':
            personagem = 'Paulo'
            print('Olá, eu sou o Paulo !\n'
                  'Estarei contigo nesta jornada de conhecimento sobre\n'
                  'esse mundo da diversidade. Haverá textos para introdução\n'
                  'do assunto e Quiz, para testar se você está craque no assunto.')
            jogar_com_avatar(personagem)

        elif personagem == '2':
            personagem = 'Denise'
            print('Olá, eu sou a Denise !\n'
                  'Estarei contigo nesta jornada de conhecimento sobre\n'
                  'esse mundo da diversidade. Haverá textos para introdução\n'
                  'do assunto e Quiz, para testar se você está craque no assunto.')
            jogar_com_avatar(personagem)

        elif personagem == '3':
            encerrar_jogo()
        elif personagem > '3':
            print(f"Personagem {personagem} não existe!")
            print("Escolha uma opção da lista abaixo:")


def conteudo_fase_um(avatar):
    cabecalho_fase_um()
    # apresentação do tema DIVERSIDADE

    texto_diversiade = '-- DIVERSIDADE --' + '\n' + 'O que é diverso, diferença, dessemelhança, variedade, multiplicidade.' + '\n' + 'As diferenças entre  as pessos podem ser de muitas ordens' + '\n' + 'Física, Morais, Religosas, Culturais , Ideologicas.'
    print(f'{avatar} diz:')
    escrever(texto_diversiade)
    sleep(1)

    # Quiz do tema DIVERSIDADE

    op = str(input("\nTopa um Quiz sobre este tema [S/N]: ")).upper()
    if op == "S":
        limpar_tela()
        quiz_diversidade()
    elif op == "N":
        encerrar_jogo()

    # Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

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

    # apresentação do tema EQUIDADE

    texto_equidade = '-- EQUIDADE --' + '\n' + 'Significa a promoção de iguais oportunidades para os membros desse grupo,' + '\n' + 'para isso, as diferenças entre as pessoas é considerada, a fim de deixa-la mais justa para as duas partes.'
    op = str(input('Vamos continuar?[S/N]: ')).upper()
    limpar_tela()
    cabecalho_fase_um()
    if op == 'S':
        print(f'{avatar} diz:')
        escrever(texto_equidade)
        sleep(1)
        op = str(input("\nTopa um Quiz sobre este tema [S/N]: ")).upper()

    # Quiz tema EQUIDADE

        if op == "S":
            limpar_tela()
            quiz_equidade()
        elif op == "N":
            encerrar_jogo()
        elif op != "S":
            while True:
                print(f'A opção {op} não existe.')
                op = str(input('Deseja continuar?[S/N]: ')).upper()
                limpar_tela()
                if op == "S":
                    quiz_equidade()
                    break
                elif op == "N":
                    encerrar_jogo()
                    break

    # apresentação  tema Grupos minoritários

    texto_grupo_minoritario = '-- GRUPOS MINORITÁRIOS --' + '\n' + 'A palavra minoria se refere a um grupo de pessoas que de algum modo' + '\n' + 'e em algum, setor das relações sociais se encontra numa situação de' + '\n' + 'dependência ou desvantage mem relação a um outro grupo “maioritário”,' + '\n' + 'ambos integrando uma sociedade mais ampla. As minorias recebem um' + '\n' + 'tratamento discriminatório por parte da maioria. Estre grupo é' + '\n' + 'representado por, Mulheres, Comunidade LGBTQIA+, Deficiêntes Físicos' + '\n' + 'ou Mentais, Negros (Homens e Mulheres).'
    op = str(input('Vamos continuar?[S/N]: ')).upper()
    limpar_tela()
    cabecalho_fase_um()
    if op == 'S':
        print(f'{avatar} diz:')
        escrever(texto_grupo_minoritario)
        sleep(1)
        op = str(input("\nTopa um Quiz sobre este tema [S/N]: ")).upper()

        # Quiz tema Grupos minoritários

        if op == "S":
            limpar_tela()
            quiz_grupo_minoritario()
        elif op == "N":
            encerrar_jogo()
        elif op != "S":
            while True:
                print(f'A opção {op} não existe.')
                op = str(input('Deseja continuar?[S/N]: ')).upper()
                limpar_tela()
                if op == "S":
                    quiz_grupo_minoritario()
                    break
                elif op == "N":
                    encerrar_jogo()
                    break

    texto_estrutura_opressoes = '--ESTRUTURA DE OPRESSÕES--' + '\n' + 'NOVO TEMA NOVO TEMA- NOVO TEMA- NOVO TEMA- NOVO TEMA- ' + '\n' + 'NOVO TEMA NOVO TEMA- NOVO TEMA- NOVO TEMA- NOVO TEMA-' + '\n' + 'NOVO TEMA NOVO TEMA- NOVO TEMA- NOVO TEMA- NOVO TEMA-' + '\n' + 'ambos integrando uma sociedade mais ampla. As minorias recebem um' + '\n' + 'tratamento discriminatório por parte da maioria. Estre grupo é' + '\n' + 'representado por, Mulheres, Comunidade LGBTQIA+, Deficiêntes Físicos' + '\n' + 'ou Mentais, Negros (Homens e Mulheres).'
    op = str(input('Vamos continuar?[S/N]: ')).upper()
    limpar_tela()
    cabecalho_fase_um()
    if op == 'S':
        print(f'{avatar} diz:')
        escrever(texto_estrutura_opressoes)
        sleep(1)
        op = str(input("\nTopa um Quiz sobre este tema [S/N]: ")).upper()

        # Quiz tema Grupos minoritários

        if op == "S":
            limpar_tela()
            quiz_estrutura_opressoes()
        elif op == "N":
            encerrar_jogo()
        elif op != "S":
            while True:
                print(f'A opção {op} não existe.')
                op = str(input('Deseja continuar?[S/N]: ')).upper()
                limpar_tela()
                if op == "S":
                    quiz_estrutura_opressoes()
                    break
                elif op == "N":
                    encerrar_jogo()
                    break


def quiz_diversidade():
    pontos = 0
    limpar_tela()
    pergunta_um = str(input("Escolha uma alternativa que melhor represente a DIVERSIDADE: \n[A] Física, Morais, Religosas, Culturais , Musicalidade.\n[B] Física, Morais, Religosas, Artística , Ideologicas.\n[C] Física, Morais, Temporal, Culturais , Ideologicas.\n[D] Física, Morais, Religosas, Culturais , Ideologicas.\nEscolha  uma  alternativa:")).upper()
    if pergunta_um == "A":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Física, Morais, Religosas, Culturais\n')
    elif pergunta_um == "B":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Física, Morais, Religosas, Culturais\n')
    elif pergunta_um == "C":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Física, Morais, Religosas, Culturais\n')
    elif pergunta_um == "D":
        limpar_tela()
        pontos += 10
        print(f'Você ACERTOU!\nO seu placar é de {pontos} pontos.')

    # Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta_um != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta_um} não exite. Tente novamente.\n')
            pergunta_um = str(input("Escolha uma alternativa que melhor represente a DIVERSIDADE: \n[A] Física, Morais, Religosas, Culturais , Musicalidade.\n[B] Física, Morais, Religosas, Artística , Ideologicas.\n[C] Física, Morais, Temporal, Culturais , Ideologicas.\n[D] Física, Morais, Religosas, Culturais , Ideologicas.\nEscolha  uma  alternativa:")).upper()
            if pergunta_um == "A":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Física, Morais, Religosas, Culturais')
                break
            elif pergunta_um == "B":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Física, Morais, Religosas, Culturais')
                break
            elif pergunta_um == "C":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Física, Morais, Religosas, Culturais')
                break
            elif pergunta_um == "D":
                limpar_tela()
                pontos += 10
                print(f'Você ACERTOU!\nO seu placar é de {pontos} pontos.\n')
                break


def quiz_equidade():
    eq_pontos = 0
    limpar_tela()
    pergunta_dois = str(input(
        "Escolha uma alternativa que melhor represente a EQUIDADDE: \n[A] Equidade é adaptar  as oportunidades  deixando-as justas.\n[B] Desigualdade é o antônimo de equidade.\n[C] Equidade tem o mesmo significado que igualdade.\n[D] Equidade é dar as mesmas oportunidades..\nEscolha  uma  alternativa:")).upper()
    if pergunta_dois == "A":
        limpar_tela()
        eq_pontos += 10
        print(f'Você ACERTOU!\nO seu placar é de {eq_pontos} pontos.')
    elif pergunta_dois == "B":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[A] Equidade é adaptar  as oportunidades  deixando-as justas\n')
    elif pergunta_dois == "C":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[A] Equidade é adaptar  as oportunidades  deixando-as justas\n')
    elif pergunta_dois == "D":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[A] Equidade é adaptar  as oportunidades  deixando-as justas\n')

    #  Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta_dois != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta_dois} não exite. Tente novamente.\n')
            pergunta_dois = str(input(
                "PERGUNTA SOBRE EQUIDADE.\nEscolha uma alternativa que melhor represente a EQUIDADDE: \n[A] ALTERNATIVA CERTA.\n[B] ALTERNATIVA ERRADA.\n[C] ALTERNATIVA ERRADA.\n[D] ALTERNATIVA ERRADA.\nEscolha  uma  alternativa:")).upper()
            if pergunta_dois == "A":
                limpar_tela()
                eq_pontos += 10
                print(f'Você ACERTOU!\nO seu placar é de {eq_pontos} pontos.')
                break
            elif pergunta_dois == "B":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[A] Equidade é adaptar  as oportunidades  deixando-as justas\n')
                break
            elif pergunta_dois == "C":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[A] Equidade é adaptar  as oportunidades  deixando-as justas\n')
                break
            elif pergunta_dois == "D":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[A] Equidade é adaptar  as oportunidades  deixando-as justas\n')
                break


def quiz_grupo_minoritario():
    gp_pontos = 0
    limpar_tela()
    pergunta_tres = str(input(
        "Escolha uma alternativa que melhor represente a GRUPO MINORITÁRIO: \n[A] Homem Branco, Mulher Negra, Homem Negro, LGBTQIA+.\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n[C] Mulheres, Heterosexual, Deficiente, LGBTQIA+.\n[D] Homem Branco, Heterosexual, Deficiente, LGBTQIA+.\nEscolha  uma  alternativa:")).upper()
    if pergunta_tres == "A":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')
    elif pergunta_tres == "B":
        limpar_tela()
        gp_pontos += 10
        print(f'Você ACERTOU!\nO seu placar é de {gp_pontos} pontos.')
    elif pergunta_tres == "C":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\nB] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')
    elif pergunta_tres == "D":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\nB] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')

    #  Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta_tres != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta_tres} não exite. Tente novamente.\n')
            pergunta_tres = str(input("Escolha uma alternativa que melhor represente a GRUPO MINORITÁRIO: \n[A] Homem Branco, Mulher Negra, Homem Negro, LGBTQIA+.\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n[C] Mulheres, Heterosexual, Deficiente, LGBTQIA+.\n[D] Homem Branco, Heterosexual, Deficiente, LGBTQIA+.\nEscolha  uma  alternativa:")).upper()
            if pergunta_tres == "A":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')
                break
            elif pergunta_tres == "B":
                limpar_tela()
                gp_pontos += 10
                print(f'Você ACERTOU!\nO seu placar é de {gp_pontos} pontos.')
                break
            elif pergunta_tres == "C":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')
                break
            elif pergunta_tres == "D":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')
                break


def quiz_estrutura_opressoes():
    gp_pontos = 0
    limpar_tela()
    pergunta_tres = str(input(
        "Escolha uma alternativa que melhor represente a ESTRUTURA DE OPRESSÕES: \n[A] ALTERNATIVA ERRADA.\n[B] ALTERNATIVA ERRADA.\n[C] ALTERNATIVA CERTA.\n[D] ALTERNATIVA ERRADA.\nEscolha  uma  alternativa:")).upper()
    if pergunta_tres == "A":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[C] ALTERNATIVA CERTA\n')
    elif pergunta_tres == "B":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[C] ALTERNATIVA CERTA\n')
    elif pergunta_tres == "C":
        limpar_tela()
        gp_pontos += 10
        print(f'Você ACERTOU!\nO seu placar é de {gp_pontos} pontos.')
    elif pergunta_tres == "D":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[C] ALTERNATIVA CERTA\n')

    #  Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta_tres != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta_tres} não exite. Tente novamente.\n')
            pergunta_tres = str(input(
                "Escolha uma alternativa que melhor represente a ESTRUTURA DE OPRESSÕES: \n[A] ALTERNATIVA ERRADA.\n[B] ALTERNATIVA ERRADA.\n[C] ALTERNATIVA CERTA.\n[D] ALTERNATIVA ERRADA.\nEscolha  uma  alternativa:")).upper()
            if pergunta_tres == "A":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[C] ALTERNATIVA CERTA\n')
                break
            elif pergunta_tres == "B":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[C] ALTERNATIVA CERTA\n')
                break
            elif pergunta_tres == "C":
                limpar_tela()
                gp_pontos += 10
                print(f'Você ACERTOU!\nO seu placar é de {gp_pontos} pontos.')
                break
            elif pergunta_tres == "D":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[C] ALTERNATIVA CERTA\n')
                break


cabecalho_programa()
introducao_jogo()
continuar_jogo()