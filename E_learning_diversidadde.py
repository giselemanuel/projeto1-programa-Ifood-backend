"""
Nome : Gisele Manuel
Nome do Jogo: E-learning - Diversidade nas Organizações empresariais
Descrição: A proposta deste e-learning é apresentar o tema Diversidade nas Organizações Empresariais.
Falaremos dos conceitos sobre equidade, grupos minoritários, estruturas de opressões, grupo homogêneos,
grupos heterogêneos e como a diversidade influência nos resultados e desempenho das organizações
empresariais e seus impactos na sociedade. Todo conteúdo conta com um QUIZ para que essa jornada
de conhecimento sobre o mundo da diversidade fique ainda mais interessante
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


# exibe gradualmente o texto


def escrever(texto):

    for letra in texto:
        time.sleep(0.01)
        print(f'{letra}', end='')
        time.sleep(0.01)


# encerrar o programa


def encerrar_jogo():
    limpar_tela()
    print('Encerrando o jogo...')
    sleep(2)
    print('Obrigada por Jogar !')
    quit()


# imprime mensagem quando o jogador vencer


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

    continuar_jogo()

# imprime mensagem quando o jogador perder


def imprime_mensagem_perdedor():

    print("   Puxa, você PERDEU!")
    print("    _______________        ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\   ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/    ")
    print(" |   XXX       XXX   |     ")
    print(" |                   |     ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |       ")
    print("   | I I I I I I I |       ")
    print("   |  I I I I I I  |       ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

    continuar_jogo()


# cabeçalho do programa


def cabecalho_programa():
    print('-' * 110)
    print(f'{"E-learning : DIVERSIDADE E EQUIDADE NAS ORGANIZAÇÕES":^110}')
    print('-' * 110)


# cabeçalho da fase um


def cabecalho_fase_um():
    print('-' * 110)
    print(f'{"PRIMEIRA FASE - Introdução de Conceitos ":^110}')
    print('-' * 110)


# cabeçalho da fase dois


def cabecalho_fase_dois():
    limpar_tela()
    print('-' * 110)
    print(f'{"SEGUNDA FASE - DIVERSIDADE NO MUNDO DOS NEGÓCIOS ":^110}')
    print('-' * 110)


# cabeçalho da fase três


def cabecalho_fase_tres():
    limpar_tela()
    print('-' * 110)
    print(f'{"TERCEIRA FASE - O GRANDE DESAFIO ":^110}')
    print('-' * 110)


# resumo do tema do e-learning


def introducao_jogo():
    texto_introducao_jogo = 'A proposta deste e-learning é apresentar o tema Diversidade nas Organizações Empresariais. Falaremos dos ' + \
                            '\n' + 'conceitos sobre  equidade, grupos minoritários, estruturas de opressões, grupo homogêneos, grupos ' + \
                            '\n' + 'heterogêneos e como a diversidade influência nos resultados e desempenho das organizações empresariais e ' + \
                            '\n' + 'seus impactos na sociedade. Todo contéudo conta com um QUIZ para que essa jornada de conhecimento sobre o ' + \
                            '\n' + 'mundo da diversidade fique ainda mais interessante.'
    print('-' * 110)
    print(texto_introducao_jogo)
    print('-' * 110)


# função que pergunta ao usuário se ele deseja continuar o jogo e avança para  escolher um avatar


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


# função que válida se o usuário deseja continuar  a primeira fase


def jogar_na_fase_um(jogador):
    print('\n')
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


# função que válida se o usuário deseja continuar  a segunda fase


def jogar_na_fase_dois(jogador):
    print('\n')
    op = str(input('Parabéns você concluiu a PRIMEIRA FASE !\nVamos continuar [S/N] : ')).upper()
    limpar_tela()
    if op == "S":
        conteudo_fase_dois(jogador)
    elif op == "N":
        encerrar_jogo()
    elif op != "S":
        while True:
            print(f'A opção {op} não existe.')
            op = str(input('Deseja continuar?[S/N]: ')).upper()
            limpar_tela()
            if op == "S":
                conteudo_fase_dois(jogador)
            elif op == "N":
                encerrar_jogo()
                break


# função que válida se o usuário deseja continuar  a terceira fase


def jogar_na_fase_tres(jogador):
    print('\n')
    op = str(input('Parabéns você concluiu a SEGUNDA FASE !\nVamos continuar [S/N] : ')).upper()
    limpar_tela()
    if op == "S":
        conteudo_fase_tres(jogador)
    elif op == "N":
        encerrar_jogo()
    elif op != "S":
        while True:
            print(f'A opção {op} não existe.')
            op = str(input('Deseja continuar?[S/N]: ')).upper()
            limpar_tela()
            if op == "S":
                conteudo_fase_tres(jogador)
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
            jogar_na_fase_um(personagem)

        elif personagem == '1':
            personagem = 'Paulo'
            print('Olá, eu sou o Paulo !\n'
                  'Estarei contigo nesta jornada de conhecimento sobre\n'
                  'esse mundo da diversidade. Haverá textos para introdução\n'
                  'do assunto e Quiz, para testar se você está craque no assunto.')
            jogar_na_fase_um(personagem)

        elif personagem == '2':
            personagem = 'Denise'
            print('Olá, eu sou a Denise !\n'
                  'Estarei contigo nesta jornada de conhecimento sobre\n'
                  'esse mundo da diversidade. Haverá textos para introdução\n'
                  'do assunto e Quiz, para testar se você está craque no assunto.')
            jogar_na_fase_um(personagem)

        elif personagem == '3':
            encerrar_jogo()
        elif personagem > '3':
            print(f"Personagem {personagem} não existe!")
            print("Escolha uma opção da lista abaixo:")


# apresenta o contéudo teórico da PRIMEIRA FASE


def conteudo_fase_um(avatar):
    cabecalho_fase_um()
    # apresentação do tema DIVERSIDADE

    texto_diversiade = '-- DIVERSIDADE --' + \
                       '\n' + 'O que é diverso, diferença, dessemelhança, variedade, multiplicidade. As diferenças entre as pessoas podem' + \
                       '\n' + 'ser de muitas ordens Física, Morais, Religosas, Culturais , Ideologicas.'
    print(f'{avatar} diz:')
    escrever(texto_diversiade)
    print('\n')
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

    texto_equidade = '-- EQUIDADE --' + \
                     '\n' + 'Significa a promoção de iguais oportunidades para os membros desse grupo, para isso, as diferenças entre as' + \
                     '\n' + 'pessoas é considerada, a fim de deixa-la mais justa para as duas partes.'
    op = str(input('Vamos continuar?[S/N]: ')).upper()
    limpar_tela()
    cabecalho_fase_um()
    if op == 'S':
        print(f'{avatar} diz:')
        escrever(texto_equidade)
        print('\n')
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

    texto_grupo_minoritario = '-- GRUPOS MINORITÁRIOS --' + \
                              '\n' + 'A palavra minoria se refere a um grupo de pessoas que de algum modo e em algum, setor das relações sociais' + \
                              '\n' + 'se encontram em uma situação de dependência ou desvantagem em relação a um outro grupo “maioritário”, ambos ' + \
                              '\n' + 'integrando uma sociedade mais ampla. As minorias recebem um tratamento discriminatório por parte da maioria.' + \
                              '\n' + 'Neste grupo estão  Mulheres, Comunidade LGBTQIA+, Deficiêntes Físicos ou Mentais, Negros (Homens e Mulheres).'
    op = str(input('Vamos continuar?[S/N]: ')).upper()
    limpar_tela()
    cabecalho_fase_um()
    if op == 'S':
        print(f'{avatar} diz:')
        escrever(texto_grupo_minoritario)
        print('\n')
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

    texto_estrutura_opressoes = '-- ESTRUTURA DE OPRESSÕES --' + \
                                '\n' + 'Precisamos combater as estruturas de opressões como racismo, machismo, transfobia, homofobia, gordofobia,' + \
                                '\n' + 'discriminação de pessoas com limitações físicas e mentais, pessoas mais velhas , pessoas religiosas e de' + \
                                '\n' + 'origem e cultura diferentes. No Brasil muitas pessoas sofrem violência ou morrem por ser mulher, negro,' + \
                                '\n' + 'por ser parte da comunidade LGBTQIA+ ou por ser pobre. Portanto este deve ser um tema central na discussão' + \
                                '\n' + 'da diversidade.'
    op = str(input('Vamos continuar?[S/N]: ')).upper()
    limpar_tela()
    cabecalho_fase_um()
    if op == 'S':
        print(f'{avatar} diz:')
        escrever(texto_estrutura_opressoes)
        sleep(1)
        op = str(input("\nTopa um Quiz sobre este tema [S/N]: ")).upper()

        # Quiz tema Estrutura de Opressões

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

    jogar_na_fase_dois(avatar)


# apresenta o contéudo teórico da SEGUNDA FASE


def conteudo_fase_dois(avatar):
    cabecalho_fase_dois()
    # apresentação do tema GRUPO HOMOGÊNEO

    texto_gp_homogeneos = '-- GRUPOS HOMOGÊNEOS  --' + \
                          '\n' + 'São pessoas com as mesmas origens e vivivências. Estrutura familiar parecida. Mesma formação escolar e' + \
                          '\n' + 'universitária. Visitaram os mesmos lugares e possuem as mesmas crenças. Pessoas deste grupo tem ideias' + \
                          '\n' + 'parecidas portanto o repertório deste determinado grupo é limitado e distante de outros grupos sociais.' + \
                          '\n' + 'Jamais compreendendo a vivência de um outro grupo.'
    print(f'{avatar} diz:')
    escrever(texto_gp_homogeneos)
    print('\n')
    sleep(1)

    # Quiz do tema  GRUPO HOMOGÊNEO

    op = str(input("\nTopa um Quiz sobre este tema [S/N]: ")).upper()
    if op == "S":
        limpar_tela()
        quiz_gp_homogeneos()
    elif op == "N":
        encerrar_jogo()

    # Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif op != "S":
        while True:
            print(f'A opção {op} não existe.')
            op = str(input('Deseja continuar?[S/N]: ')).upper()
            limpar_tela()
            if op == "S":
                quiz_gp_homogeneos()
                break
            elif op == "N":
                encerrar_jogo()
                break

    # apresentação do tema GRUPO HETEROGÊNEO

    texto_gp_heterogeneos = '--  GRUPOS HETEROGÊNEOS --' + \
                            '\n' + 'São pessoas que possuem idade, costumes e experiências acentuadamente diversificada, possuem uma visão mais' + \
                            '\n' + 'complexa da sociedade, buscam soluções inovadoras e próximo da realidade de outros grupos sociais e ' + \
                            '\n' + 'consumidores. Consumidores tem um papel fundamental na movimentação das empresas, visando iniciativar e ' + \
                            '\n' + 'espaços que favorecem a Diversidade.'
    op = str(input('Vamos continuar?[S/N]: ')).upper()
    limpar_tela()
    cabecalho_fase_dois()
    if op == 'S':
        print(f'{avatar} diz:')
        escrever(texto_gp_heterogeneos)
        print('\n')
        sleep(1)
        op = str(input("\nTopa um Quiz sobre este tema [S/N]: ")).upper()

    # Quiz tema GRUPO HETEROGÊNEO

        if op == "S":
            limpar_tela()
            quiz_gp_heterogeneos()
        elif op == "N":
            encerrar_jogo()
        elif op != "S":
            while True:
                print(f'A opção {op} não existe.')
                op = str(input('Deseja continuar?[S/N]: ')).upper()
                limpar_tela()
                if op == "S":
                    quiz_gp_heterogeneos()
                    break
                elif op == "N":
                    encerrar_jogo()
                    break

    # apresentação  tema RESULTADO DA DIVERSIDADE NAS ORGANIZAÇÕES

    texto_resultado_diversidade = '-- RESULTADO DA DIVERSIDADE NAS ORGANIZAÇÕES --' + \
                                  '\n' + 'Diversidade esta diretamente relacionada à sobrevivência e ao crescimento de organizações empresariais. ' + \
                                  '\n' + 'Um estudo sobre a entrega de resultados pela diversidade, realizado em 12 países, aponta: "As companhias com' + \
                                  '\n' + 'maior diversidade de gênero da amostra tem 21% mais chances de apresentar resultados acima da média do mercado' + \
                                  '\n' + 'que outras empresas com menor diversidade e  no caso da diversidade cultural e étnica, a variedade é ainda mais' + \
                                  '\n' + 'premiada e esse número sobe para 33%. ' + '\n' + \
                                  '                                                                                Fonte: McKinsey & Company Inc.'

    op = str(input('Vamos continuar?[S/N]: ')).upper()
    limpar_tela()
    cabecalho_fase_dois()
    if op == 'S':
        print(f'{avatar} diz:')
        escrever(texto_resultado_diversidade)
        print('\n')
        sleep(1)
        op = str(input("\nTopa um Quiz sobre este tema [S/N]: ")).upper()

        # Quiz tema  RESULTADO DA DIVERSIDADE NAS ORGANIZAÇÕES

        if op == "S":
            limpar_tela()
            quiz_resultado_diversidade()
        elif op == "N":
            encerrar_jogo()
        elif op != "S":
            while True:
                print(f'A opção {op} não existe.')
                op = str(input('Deseja continuar?[S/N]: ')).upper()
                limpar_tela()
                if op == "S":
                    quiz_resultado_diversidade()
                    break
                elif op == "N":
                    encerrar_jogo()
                    break

    # apresentação  tema AMBIENTE DIVERSO NAS ORGANIZAÇÕES

    texto_ambiente_diverso = '-- AMBIENTE DIVERSO NAS ORGANIZAÇÕES --' + \
                             '\n' + 'Organizações empresariais são agentes importantes dentro do sistema que vivemos, por isso o seu engajamento' + \
                             '\n' + 'em prol de ambientes mais diversos e de direitos iguais tem tanto impacto na sociedade. Um bom começo para' + \
                             '\n' + 'agir é através de contratações. Uma empresa só consegue evoluir se o RH em parceria com líderes e gestores de' + \
                             '\n' + 'equipe entenderem a diversidadde como valor.'
    op = str(input('Vamos continuar?[S/N]: ')).upper()
    limpar_tela()
    cabecalho_fase_dois()
    if op == 'S':
        print(f'{avatar} diz:')
        escrever(texto_ambiente_diverso)
        sleep(1)
        op = str(input("\nTopa um Quiz sobre este tema [S/N]: ")).upper()

        # Quiz tema AMBIENTE DIVERSO NAS ORGANIZAÇÕES

        if op == "S":
            limpar_tela()
            quiz_ambiente_diverso()
        elif op == "N":
            encerrar_jogo()
        elif op != "S":
            while True:
                print(f'A opção {op} não existe.')
                op = str(input('Deseja continuar?[S/N]: ')).upper()
                limpar_tela()
                if op == "S":
                    quiz_ambiente_diverso()
                    break
                elif op == "N":
                    encerrar_jogo()
                    break
    jogar_na_fase_tres(avatar)


# apresenta o contéudo teórico da terceira FASE


def conteudo_fase_tres(avatar):
    cabecalho_fase_tres()
    print(f'{avatar} diz:')
    texto_quiz = 'Parabéns,Você chegou na terceira fase, onde teremos um grande desafio com um QUIZ, com 10 perguntas.' + \
                 '\n' + 'REGRAS:' + \
                 '\n' + 'Neste QUIZ teremos' + \
                 '\n' + '4 Perguntas PERIGOSAS, serão perguntas TUDO OU NADA, acerte e VENÇA, erre e PERCA ' + \
                 '\n' + '6 Perguntas PRATA, serão perguntas que permitirão avançar para as próximas.' \

    print(texto_quiz)
    print('\n')
    sleep(1)

    # Quiz do DESAFIO FINAL

    op = str(input("\nTopa este DESAFIO [S/N]: ")).upper()
    if op == "S":
        limpar_tela()
        quiz_final()
    elif op == "N":
        encerrar_jogo()

    # Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif op != "S":
        while True:
            print(f'A opção {op} não existe.')
            op = str(input("\nTopa este DESAFIO [S/N]: ")).upper()
            limpar_tela()
            if op == "S":
                quiz_final()
                break
            elif op == "N":
                encerrar_jogo()
                break


# Quiz do tema DIVERSIDADE


def quiz_diversidade():
    limpar_tela()
    pergunta1 = str(input("Escolha uma alternativa que melhor represente as origens da DIVERSIDADE: \n[A] Física, Morais, Religosas, Culturais , Musicalidade.\n[B] Física, Morais, Religosas, Artística , Ideologicas.\n[C] Física, Morais, Temporal, Culturais , Ideologicas.\n[D] Física, Morais, Religosas, Culturais , Ideologicas.\nEscolha  uma  alternativa:")).upper()
    if pergunta1 == "A":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Física, Morais, Religosas, Culturais\n')
    elif pergunta1 == "B":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Física, Morais, Religosas, Culturais\n')
    elif pergunta1 == "C":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Física, Morais, Religosas, Culturais\n')
    elif pergunta1 == "D":
        limpar_tela()
        print(f'Você ACERTOU!\n')

    # Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta1 != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta1} não exite. Tente novamente.\n')
            pergunta1 = str(input("Escolha uma alternativa que melhor represente as origens da DIVERSIDADE: \n[A] Física, Morais, Religosas, Culturais , Musicalidade.\n[B] Física, Morais, Religosas, Artística , Ideologicas.\n[C] Física, Morais, Temporal, Culturais , Ideologicas.\n[D] Física, Morais, Religosas, Culturais , Ideologicas.\nEscolha  uma  alternativa:")).upper()
            if pergunta1 == "A":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Física, Morais, Religosas, Culturais')
                break
            elif pergunta1 == "B":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Física, Morais, Religosas, Culturais')
                break
            elif pergunta1 == "C":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Física, Morais, Religosas, Culturais')
                break
            elif pergunta1 == "D":
                limpar_tela()
                print(f'Você ACERTOU!\n')
                break


#  Quiz do tema EQUIDADE


def quiz_equidade():
    limpar_tela()
    pergunta2 = str(input(
        "Escolha uma alternativa que melhor represente a EQUIDADDE: \n[A] Equidade é adaptar  as oportunidades  deixando-as justas.\n[B] Desigualdade é o antônimo de equidade.\n[C] Equidade tem o mesmo significado que igualdade.\n[D] Equidade é dar as mesmas oportunidades..\nEscolha  uma  alternativa:")).upper()
    if pergunta2 == "A":
        limpar_tela()
        print(f'Você ACERTOU!\n')
    elif pergunta2 == "B":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[A] Equidade é adaptar  as oportunidades  deixando-as justas\n')
    elif pergunta2 == "C":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[A] Equidade é adaptar  as oportunidades  deixando-as justas\n')
    elif pergunta2 == "D":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[A] Equidade é adaptar  as oportunidades  deixando-as justas\n')

    #  Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta2 != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta2} não exite. Tente novamente.\n')
            pergunta2 = str(input(
                "PERGUNTA SOBRE EQUIDADE.\nEscolha uma alternativa que melhor represente a EQUIDADDE: \n[A] ALTERNATIVA CERTA.\n[B] ALTERNATIVA ERRADA.\n[C] ALTERNATIVA ERRADA.\n[D] ALTERNATIVA ERRADA.\nEscolha  uma  alternativa:")).upper()
            if pergunta2 == "A":
                limpar_tela()
                print(f'Você ACERTOU!\n')
                break
            elif pergunta2 == "B":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[A] Equidade é adaptar  as oportunidades  deixando-as justas\n')
                break
            elif pergunta2 == "C":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[A] Equidade é adaptar  as oportunidades  deixando-as justas\n')
                break
            elif pergunta2 == "D":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[A] Equidade é adaptar  as oportunidades  deixando-as justas\n')
                break


# Quiz do tema GRUPOS MINORITÁRIOS


def quiz_grupo_minoritario():
    limpar_tela()
    pergunta3 = str(input("Escolha uma alternativa que melhor represente o GRUPO MINORITÁRIO: \n[A] Homem Branco, Mulher Negra, Homem Negro, LGBTQIA+.\n[B] Mulheres, Homem Negro, Deficientes, LGBTQIA+.\n[C] Mulheres, Heterosexual, Deficientes, LGBTQIA+.\n[D] Homem Branco, Heterosexual, Deficientes, LGBTQIA+.\nEscolha  uma  alternativa:")).upper()
    if pergunta3 == "A":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')
    elif pergunta3 == "B":
        limpar_tela()
        print(f'Você ACERTOU!\n')
    elif pergunta3 == "C":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')
    elif pergunta3 == "D":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')

    #  Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta3 != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta3} não exite. Tente novamente.\n')
            pergunta3 = str(input("Escolha uma alternativa que melhor represente o GRUPO MINORITÁRIO: \n[A] Homem Branco, Mulher Negra, Homem Negro, LGBTQIA+.\n[B] Mulheres, Homem Negro, Deficientes, LGBTQIA+.\n[C] Mulheres, Heterosexual, Deficientes, LGBTQIA+.\n[D] Homem Branco, Heterosexual, Deficientes, LGBTQIA+.\nEscolha  uma  alternativa:")).upper()
            if pergunta3 == "A":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')
                break
            elif pergunta3 == "B":
                limpar_tela()
                print(f'Você ACERTOU!\n')
                break
            elif pergunta3 == "C":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')
                break
            elif pergunta3 == "D":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')
                break


# Quiz do tema ESTRTUTURAS DE OPRESSÕES


def quiz_estrutura_opressoes():
    limpar_tela()
    pergunta4 = str(input("Escolha uma alternativa incorreta sobre o tema  ESTRUTURA DE OPRESSÕES: \n[A] Mulheres são atingidas pelo machismo.\n[B] A comunidade LGBTQIA+ é atingida pela Homofobia e Transfobia.\n[C] Não existe estrutura de opressão.\n[D] A comunidade negra é atingida pelo racismo.\nEscolha  uma  alternativa:")).upper()
    if pergunta4 == "A":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Não existe estrutura de opressão.\n')
    elif pergunta4 == "B":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Não existe estrutura de opressão.\n')
    elif pergunta4 == "C":
        limpar_tela()
        print(f'Você ACERTOU!\n')
    elif pergunta4 == "D":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Não existe estrutura de opressão.\n')

    #  Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta4 != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta4 } não exite. Tente novamente.\n')
            pergunta4 = str(input("Escolha uma alternativa incorreta sobre o tema  ESTRUTURA DE OPRESSÕES: \n[A] Mulheres são atingidas pelo machismo.\n[B] A comunidade LGBTQIA+ é atingida pela Homofobia e Transfobia.\n[C] Não existe estrutura de opressão.\n[D] A comunidade negra é atingida pelo racismo.\nEscolha  uma  alternativa:")).upper()
            if pergunta4 == "A":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Não existe estrutura de opressão.\n')
                break
            elif pergunta4 == "B":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Não existe estrutura de opressão.\n')
                break
            elif pergunta4 == "C":
                limpar_tela()
                print(f'Você ACERTOU!\n')
                break
            elif pergunta4 == "D":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Não existe estrutura de opressão.\n')
                break


#  Quiz do tema GRUPOS HOMOGÊNEOS


def quiz_gp_homogeneos():
    limpar_tela()
    pergunta5 = str(input(
        "Escolha uma alternativa incorreta sobre o tema  GRUPO HOMOGÊNEO: \n[A] Pessoas deste grupo possuem crenças diferentes.\n[B] Pessoas deste grupo são da mesma origem.\n[C] Pessoas deste grupo possuem a mesma formação educacional.\n[D] Pessoas deste grupo possuem estrutura familiar parecida.\nEscolha  uma  alternativa:")).upper()
    if pergunta5 == "A":
        limpar_tela()
        print(f'Você ACERTOU!\n')
    elif pergunta5 == "B":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[A] Pessoas deste grupo possuem crenças diferentes.\n')
    elif pergunta5 == "C":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[A] Pessoas deste grupo possuem crenças diferentes.\n')
    elif pergunta5 == "D":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[A] Pessoas deste grupo possuem crenças diferentes.\n')

    #  Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta5 != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta5} não exite. Tente novamente.\n')
            pergunta5 = str(input(
                "Escolha uma alternativa incorreta sobre o tema  GRUPO HOMOGÊNEO: \n[A] Pessoas deste grupo possuem crenças diferentes.\n[B] Pessoas deste grupo são da mesma origem.\n[C] Pessoas deste grupo possuem a mesma formação educacional.\n[D] Pessoas deste grupo possuem estrutura familiar parecida.\nEscolha  uma  alternativa:")).upper()
            if pergunta5 == "A":
                limpar_tela()
                print(f'Você ACERTOU!\n')
                break
            elif pergunta5 == "B":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[A] Pessoas deste grupo possuem crenças diferentes.\n')
                break
            elif pergunta5 == "C":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[A] Pessoas deste grupo possuem crenças diferentes.\n')
                break
            elif pergunta5 == "D":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[A] Pessoas deste grupo possuem crenças diferentes.\n')
                break


#  Quiz do tema GRUPOS HETEROGÊNEOS


def quiz_gp_heterogeneos():
    limpar_tela()
    pergunta6 = str(input(
        "Escolha uma alternativa incorreta sobre o tema  GRUPO HETEROGÊNEO: \n[A] Pessoas deste grupo possuem crenças diferentes.\n[B] Pessoas deste grupo são de origem diferentes.\n[C] Pessoas deste grupo possuem a mesma formação educacional.\n[D] Pessoas deste grupo possuem estrutura familiar diferentes.\nEscolha  uma  alternativa:")).upper()
    if pergunta6 == "A":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Pessoas deste grupo possuem a mesma formação educacional.\n')
    elif pergunta6 == "B":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Pessoas deste grupo possuem a mesma formação educacional.\n')
    elif pergunta6 == "C":
        limpar_tela()
        print(f'Você ACERTOU!\n')
    elif pergunta6 == "D":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Pessoas deste grupo possuem a mesma formação educacional.\n')

    #  Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta6 != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta6} não exite. Tente novamente.\n')
            pergunta6 = str(input(
                "Escolha uma alternativa incorreta sobre o tema  GRUPO HETEROGÊNEO: \n[A] Pessoas deste grupo possuem crenças diferentes.\n[B] Pessoas deste grupo são de origem diferentes.\n[C] Pessoas deste grupo possuem a mesma formação educacional.\n[D] Pessoas deste grupo possuem estrutura familiar diferentes.\nEscolha  uma  alternativa:")).upper()
            if pergunta6 == "A":
                limpar_tela()
                print(
                    'Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Pessoas deste grupo possuem a mesma formação educacional.\n')
                break
            elif pergunta6 == "B":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Pessoas deste grupo possuem a mesma formação educacional.\n')
                break
            elif pergunta6 == "C":
                limpar_tela()
                print(f'Você ACERTOU!\n')
                break
            elif pergunta6 == "D":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Pessoas deste grupo possuem a mesma formação educacional.\n')
                break


#  Quiz do tema RESULTADO DA DIVERSIDADE NAS ORGANIZAÇÕES


def quiz_resultado_diversidade():
    limpar_tela()
    pergunta7 = str(input(
        "Escolha uma alternativa correta sobre o tema  RESULTADO DA DIVERSIDADE NAS ORGANIZAÇÕES: \n[A] Uma Organição empresarial não precisa de Diversidade  para atingir melhores resultados.\n[B] A Diversidade não é um diferencial competitivo entre organizações empresariais.\n[C] Organizações empresariais que não possuem Diversidade atingem melhores resultados.\n[D] Diversidade esta  relacionada à sobrevivência e ao crescimento de organizações empresariais.\nEscolha  uma  alternativa:")).upper()
    if pergunta7 == "A":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Diversidade esta relacionada à sobrevivência e ao crescimento de organizações empresariais.\n')
    elif pergunta7 == "B":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Diversidade esta relacionada à sobrevivência e ao crescimento de organizações empresariais.\n')
    elif pergunta7 == "C":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Diversidade esta relacionada à sobrevivência e ao crescimento de organizações empresariais.\n')
    elif pergunta7 == "D":
        limpar_tela()
        print(f'Você ACERTOU!\n')

    #  Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta7 != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta7} não exite. Tente novamente.\n')
            pergunta7 = str(input(
                "Escolha uma alternativa correta sobre o tema  RESULTADO DA DIVERSIDADE NAS ORGANIZAÇÕES: \n[A] Uma Organição empresarial não precisa de Diversidade  para atingir melhores resultados.\n[B] A Diversidade não é um diferencial competitivo entre organizações empresariais.\n[C] Organizações empresariais que não possuem Diversidade atingem melhores resultados.\n[D] Diversidade esta  relacionada à sobrevivência e ao crescimento de organizações empresariais.\nEscolha  uma  alternativa:")).upper()
            if pergunta7 == "A":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Diversidade esta relacionada à sobrevivência e ao crescimento de organizações empresariais.\n')
                break
            elif pergunta7 == "B":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Diversidade esta relacionada à sobrevivência e ao crescimento de organizações empresariais.\n')
                break
            elif pergunta7 == "C":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Diversidade esta relacionada à sobrevivência e ao crescimento de organizações empresariais.\n')
                break
            elif pergunta7 == "D":
                limpar_tela()
                print(f'Você ACERTOU!\n')
                break


#  Quiz do tema AMBIENTE DIVERSO NAS ORGANIZAÇÕES

def quiz_ambiente_diverso():
    limpar_tela()
    pergunta8 = str(input(
        "Escolha uma alternativa correta sobre o tema  AMBIENTE DIVERSO NAS ORGANIZAÇÕES: \n[A] A contratação de pessoas diversas não precisa da parceria do RH e Gestores.\n[B] A Diversidade dentro das Organizações empresariais impactam a sociedade.\n[C] Organizações empresariais não precisam de Diversidade.\n[D] A sociedade não é impactada com a Diversidade dentro das organizações empresariais.\nEscolha  uma  alternativa:")).upper()
    if pergunta8 == "A":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] A Diversidade dentro das Organizações empresariais impactam a sociedade.\n')
    elif pergunta8 == "B":
        limpar_tela()
        print(f'Você ACERTOU!\n')
    elif pergunta8 == "C":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] A Diversidade dentro das Organizações empresariais impactam a sociedade.\n')
    elif pergunta8 == "D":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] A Diversidade dentro das Organizações empresariais impactam a sociedade.\n')

    #  Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta8 != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta8} não exite. Tente novamente.\n')
            pergunta8 = str(input("Escolha uma alternativa correta sobre o tema  AMBIENTE DIVERSO NAS ORGANIZAÇÕES: \n[A] A contratação de pessoas diversas não precisa da parceria do RH e Gestores.\n[B] A Diversidade dentro das Organizações empresariais impactam a sociedade.\n[C] Organizações empresariais não precisam de Diversidade.\n[D] A sociedade não é impactada com a Diversidade dentro das organizações empresariais.\nEscolha  uma  alternativa:")).upper()
            if pergunta8 == "A":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] A Diversidade dentro das Organizações empresariais impactam a sociedade.\n')
                break
            elif pergunta8 == "B":
                limpar_tela()
                print(f'Você ACERTOU!\n')
                break
            elif pergunta8 == "C":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] A Diversidade dentro das Organizações empresariais impactam a sociedade.\n')
                break
            elif pergunta8 == "D":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] A Diversidade dentro das Organizações empresariais impactam a sociedade.\n')
                break


def quiz_final():

    cabecalho_fase_tres()

    # variáveis declaradas pois na segunda versão do programa a condição de vitória se dará através de uma regra de pontuação.

    acertos = 0
    acerto_prata = 20
    erro_prata = 10
    acerto_ouro = 200
    erro_ouro = 10
    acerto_perigosa = 10
    erro_perigosa = 100

    # 01 Pergunta sobre  Diversidade

    limpar_tela()
    pergunta9 = str(input("01 - PERGUNTA PRATA - \nEscolha uma alternativa incorreta sobre o tema  DIVERSIDADE: \n[A] Ao falar de diversidade estamos nos referindo ao direito dos grupos minoritários.\n[B] A Diversidade é um assunto que NÃO precisa ser debatido.\n[C] A Diversidade é um assunto que precisa ser debatido.\n[D] A Diversidade pode ser Física, Morais, Religosas, Culturais , Ideologicas.\nEscolha  uma  alternativa:")).upper()
    if pergunta9 == "A":
        limpar_tela()
        acertos -= erro_prata
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[D] Física, Morais, Religosas, Culturais\n')
    elif pergunta9 == "B":
        limpar_tela()
        acertos += acerto_prata
        print(f'Você ACERTOU!\n')
    elif pergunta9 == "C":
        limpar_tela()
        acertos -= erro_prata
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[D] Física, Morais, Religosas, Culturais\n')
    elif pergunta9 == "D":
        limpar_tela()
        acertos -= erro_prata
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[D] Física, Morais, Religosas, Culturais\n')

    # Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta9 != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta9} não exite. Tente novamente.\n')
            pergunta9 = str(input("01 - PERGUNTA PRATA - \nEscolha uma alternativa incorreta sobre o tema  DIVERSIDADE: \n[A] Ao falar de diversidade estamos nos referindo ao direito dos grupos minoritários\n[B] A Diversidade é um assunto que NÃO precisa ser debatido.\n[C] A Diversidade é um assunto que  precisa ser debatido.\n[D] A Diversidade pode ser Física, Morais, Religosas, Culturais , Ideologicas.\nEscolha  uma  alternativa:")).upper()
            if pergunta9 == "A":
                limpar_tela()
                acertos -= erro_prata
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[D] Física, Morais, Religosas, Culturais')
                break
            elif pergunta9 == "B":
                limpar_tela()
                acertos += acerto_prata
                print(f'Você ACERTOU!\n')
                break
            elif pergunta9 == "C":
                limpar_tela()
                acertos -= erro_prata
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[D] Física, Morais, Religosas, Culturais')
                break
            elif pergunta9 == "D":
                limpar_tela()
                acertos -= erro_prata
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[D] Física, Morais, Religosas, Culturais')
                break

    cabecalho_fase_tres()


    # 02 Pergunta Equidade

    # limpar_tela()
    pergunta10 = str(input("02 - PERGUNTA PERIGOSA - \nEscolha uma alternativa correta sobre o tema  EQUIDADE:: \n[A] Equidade é dar oportunidades.\n[B] Desigualdade é o antônimo de equidade.\n[C] Equidade e igualdade são as mesmas coisas.\n[D] Equidade é adaptar as oportunidades  deixando-as justas.\nEscolha  uma  alternativa:")).upper()
    if pergunta10 == "A":
        limpar_tela()
        acertos -= erro_perigosa
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Equidade é adaptar as oportunidades  deixando-as justas.\n')
        imprime_mensagem_perdedor()
    elif pergunta10 == "B":
        limpar_tela()
        acertos -= acerto_perigosa
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Equidade é adaptar as oportunidades  deixando-as justas.\n')
        imprime_mensagem_perdedor()
    elif pergunta10 == "C":
        limpar_tela()
        acertos -= erro_perigosa
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Equidade é adaptar as oportunidades  deixando-as justas.\n')
        imprime_mensagem_perdedor()
    elif pergunta10 == "D":
        limpar_tela()
        acertos += erro_perigosa
        print(f'Você ACERTOU!\n')
        imprime_mensagem_vencedor()

    #  Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta10 != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta10} não exite. Tente novamente.\n')
            pergunta10 = str(input("02  - PERGUNTA PERIGOSA - \nEscolha uma alternativa correta sobre o tema  EQUIDADE:: \n[A] Equidade é dar oportunidades.\n[B] Desigualdade é o antônimo de equidade.\n[C] Equidade e igualdade são as mesmas coisas.\n[D] Equidade é adaptar as oportunidades  deixando-as justas.\nEscolha  uma  alternativa:")).upper()
            if pergunta10 == "A":
                limpar_tela()
                acertos -= erro_perigosa
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Equidade é adaptar as oportunidades  deixando-as justas.\n')
                imprime_mensagem_perdedor()
                break
            elif pergunta10 == "B":
                limpar_tela()
                acertos -= erro_perigosa
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Equidade é adaptar as oportunidades  deixando-as justas.\n')
                imprime_mensagem_perdedor()
                break
            elif pergunta10 == "C":
                limpar_tela()
                acertos -= erro_perigosa
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Equidade é adaptar as oportunidades  deixando-as justas.\n')
                imprime_mensagem_perdedor()
                break
            elif pergunta10 == "D":
                limpar_tela()
                acertos += acerto_perigosa
                print(f'Você ACERTOU!\n')
                imprime_mensagem_vencedor()
                break

    # 03 Pergunta Grupos Minoritários

    # limpar_tela()
    pergunta11 = str(input("03 - PERGUNTA PRATA - \nEscolha uma alternativa que melhor represente a GRUPO MINORITÁRIO: \n[A] Homem Branco, Mulher Negra, Homem Negro, LGBTQIA+.\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n[C] Mulheres, Heterosexual, Deficientes, LGBTQIA+.\n[D] Homem Branco, Heterosexual, Deficiente, LGBTQIA+.\nEscolha  uma  alternativa:")).upper()
    if pergunta11 == "A":
        limpar_tela()
        acertos -= erro_prata
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')
    elif pergunta11 == "B":
        limpar_tela()
        acertos += acerto_prata
        print(f'Você ACERTOU!\n')
    elif pergunta11 == "C":
        limpar_tela()
        acertos -= erro_prata
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')
    elif pergunta11 == "D":
        limpar_tela()
        acertos -= erro_prata
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')

    #  Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta11 != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta11} não exite. Tente novamente.\n')
            pergunta11 = str(input("03 - PERGUNTA PRATA - \nEscolha uma alternativa que melhor represente a GRUPO MINORITÁRIO: \n[A] Homem Branco, Mulher Negra, Homem Negro, LGBTQIA+.\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n[C] Mulheres, Heterosexual, Deficientes, LGBTQIA+.\n[D] Homem Branco, Heterosexual, Deficiente, LGBTQIA+.\nEscolha  uma  alternativa:")).upper()
            if pergunta11 == "A":
                limpar_tela()
                acertos -= erro_prata
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')
                break
            elif pergunta11 == "B":
                limpar_tela()
                acertos += acerto_prata
                print(f'Você ACERTOU!\n.')
                break
            elif pergunta11 == "C":
                limpar_tela()
                acertos -= erro_prata
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')
                break
            elif pergunta11 == "D":
                limpar_tela()
                acertos -= erro_prata
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')
                break

    cabecalho_fase_tres()

    # 04 Pergunta Estrutura de Opressões

    pergunta12 = str(input("04 - PERGUNTA PRATA - \nEscolha uma alternativa incorreta sobre o tema  ESTRUTURA DE OPRESSÕES: \n[A] A descontrução do processo da estrutura de opresão se da através da visibilidade do tema.\n[B] A descontrução do processo da estrutura de opresão se da através da representatividade do tema.\n[C] Não existe estrutura de opressão.\n[D] Todos somos responsáveis pelo combate da estrutura de opressão.\nEscolha  uma  alternativa:")).upper()
    if pergunta12 == "A":
        limpar_tela()
        acertos -= erro_prata
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Não existe estrutura de opressão.\n')
    elif pergunta12 == "B":
        limpar_tela()
        acertos -= erro_prata
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Não existe estrutura de opressão.\n')
    elif pergunta12 == "C":
        limpar_tela()
        acertos += acerto_prata
        print(f'Você ACERTOU!\n')
    elif pergunta12 == "D":
        limpar_tela()
        acertos -= erro_prata
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Não existe estrutura de opressão.\n')

    #  Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta12 != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta12} não exite. Tente novamente.\n')
            pergunta12 = str(input("04 - PERGUNTA PRATA - )\nEscolha uma alternativa incorreta sobre o tema  ESTRUTURA DE OPRESSÕES: \n[A] A descontrução do processo da estrutura de opresão se da através da visibilidade do tema.\n[B] A descontrução do processo da estrutura de opresão se da através da representatividade do tema.\n[C] Não existe estrutura de opressão.\n[D] Todos somos responsáveis pelo combate da estrutura de opressão.\nEscolha  uma  alternativa:")).upper()
            if pergunta12 == "A":
                limpar_tela()
                acertos -= erro_prata
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Não existe estrutura de opressão.\n')
                break
            elif pergunta12 == "B":
                limpar_tela()
                acertos -= erro_prata
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Não existe estrutura de opressão.\n')
                break
            elif pergunta12 == "C":
                limpar_tela()
                acertos += acerto_prata
                print(f'Você ACERTOU!\n.')
                break
            elif pergunta12 == "D":
                limpar_tela()
                acertos -= erro_prata
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Não existe estrutura de opressão.\n')
                break

    cabecalho_fase_tres()

    # 05 Pergunta Grupo Homogêneo

    pergunta13 = str(input("05 - PERGUNTA PERIGOSA - \nEscolha uma alternativa incorreta sobre o tema  GRUPO HOMOGÊNEO: \n[A] Pessoas deste grupo possuem ideias diferentes.\n[B] Pessoas deste grupo são da mesma origem.\n[C] Pessoas deste grupo possuem a mesma formação educacional.\n[D] Pessoas deste grupo possuem estrutura familiar parecida.\nEscolha  uma  alternativa:")).upper()
    if pergunta13 == "A":
        limpar_tela()
        acertos += acerto_perigosa
        print(f'Você ACERTOU!\n')
        imprime_mensagem_vencedor()
    elif pergunta13 == "B":
        limpar_tela()
        acertos -= erro_perigosa
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[A] Pessoas deste grupo possuem ideias diferentes.\n')
        imprime_mensagem_perdedor()
    elif pergunta13 == "C":
        limpar_tela()
        acertos -= erro_perigosa
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[A] Pessoas deste grupo possuem ideias diferentes.\n')
        imprime_mensagem_perdedor()
    elif pergunta13 == "D":
        limpar_tela()
        acertos -= erro_perigosa
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[A] Pessoas deste grupo possuem ideias diferentes.\n')
        imprime_mensagem_perdedor()

    #  Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta13 != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta13} não exite. Tente novamente.\n')
            pergunta13 = str(input("05 - PERGUNTA PERIGOSA - \nEscolha uma alternativa incorreta sobre o tema  GRUPO HOMOGÊNEO: \n[A] Pessoas deste grupo possuem ideias diferentes.\n[B] Pessoas deste grupo são da mesma origem.\n[C] Pessoas deste grupo possuem a mesma formação educacional.\n[D] Pessoas deste grupo possuem estrutura familiar parecida.\nEscolha  uma  alternativa:")).upper()
            if pergunta13 == "A":
                limpar_tela()
                acertos += acerto_perigosa
                print(f'Você ACERTOU!\n.')
                imprime_mensagem_vencedor()
                break
            elif pergunta13 == "B":
                limpar_tela()
                acertos -= erro_perigosa
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[A] Pessoas deste grupo possuem ideias diferentes.\n')
                imprime_mensagem_perdedor()
                break
            elif pergunta13 == "C":
                limpar_tela()
                acertos -= erro_perigosa
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[A] Pessoas deste grupo possuem ideias diferentes.\n')
                imprime_mensagem_perdedor()
                break
            elif pergunta13 == "D":
                limpar_tela()
                acertos -= erro_perigosa
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[A] Pessoas deste grupo possuem ideias diferentes.\n')
                imprime_mensagem_perdedor()
                break


    # 06 Pergunta Grupo Heterogêneo

    pergunta14 = str(input("06 - PERGUNTA PRATA - \nEscolha uma alternativa incorreta sobre o tema  GRUPO HETEROGÊNEO: \n[A] Pessoas deste grupo possuem crenças diferentes.\n[B] Pessoas deste grupo são de origem diferentes.\n[C] Pessoas deste grupo possuem a mesma crença.\n[D] Pessoas deste grupo possuem estrutura familiar diferentes.\nEscolha  uma  alternativa:")).upper()
    if pergunta14 == "A":
        limpar_tela()
        acertos -= erro_prata
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Pessoas deste grupo possuem a mesma crença.\n')
    elif pergunta14 == "B":
        limpar_tela()
        acertos -= erro_prata
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Pessoas deste grupo possuem a mesma crença.\n')
    elif pergunta14 == "C":
        limpar_tela()
        acertos += acerto_prata
        print(f'Você ACERTOU!\n.')
    elif pergunta14 == "D":
        limpar_tela()
        acertos -= erro_prata
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Pessoas deste grupo possuem a mesma crença.\n')

    #  Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta14 != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta14} não exite. Tente novamente.\n')
            pergunta14 = str(input("06 - PERGUNTA PRATA - \nEscolha uma alternativa incorreta sobre o tema  GRUPO HETEROGÊNEO: \n[A] Pessoas deste grupo possuem crenças diferentes.\n[B] Pessoas deste grupo são de origem diferentes.\n[C] Pessoas deste grupo possuem a mesma crença.\n[D] Pessoas deste grupo possuem estrutura familiar diferentes.\nEscolha  uma  alternativa:")).upper()
            if pergunta14 == "A":
                limpar_tela()
                acertos -= erro_prata
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Pessoas deste grupo possuem a mesma crença.\n')
                break
            elif pergunta14 == "B":
                limpar_tela()
                acertos -= erro_prata
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Pessoas deste grupo possuem a mesma crença.\n')
                break
            elif pergunta14 == "C":
                limpar_tela()
                acertos += acerto_prata
                print(f'Você ACERTOU!\n.')
                break
            elif pergunta14 == "D":
                limpar_tela()
                acertos -= erro_prata
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Pessoas deste grupo possuem a mesma crença.\n')
                break

    cabecalho_fase_tres()

    # 07 Pergunta Resultado de Diversidade nas organizações

    pergunta15 = str(input("07 - PERGUNTA PERIGOSA - \nEscolha uma alternativa correta sobre o tema  RESULTADO DA DIVERSIDADE NAS ORGANIZAÇÕES: \n[A] Os melhores resultados de um organização empresarial não esta relacionado a diversidade.\n[B] A Diversidade NÃO é um diferencial competitivo entre organizações empresariais.\n[C] Organizações empresariais que não possuem Diversidade atingem melhores resultados.\n[D] Diversidade traz crescimento e melhores resultados para organizações empresariais.\nEscolha  uma  alternativa:")).upper()
    if pergunta15 == "A":
        limpar_tela()
        acertos -= erro_perigosa
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Diversidade traz crescimento e melhores resultados para organizações empresariais.\n')
        imprime_mensagem_perdedor()
    elif pergunta15 == "B":
        limpar_tela()
        acertos -= erro_perigosa
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Diversidade traz crescimento e melhores resultados para organizações empresariais.\n')
        imprime_mensagem_perdedor()
    elif pergunta15 == "C":
        limpar_tela()
        acertos -= erro_perigosa
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Diversidade traz crescimento e melhores resultados para organizações empresariais.\n')
        imprime_mensagem_perdedor()
    elif pergunta15 == "D":
        limpar_tela()
        acertos += acerto_perigosa
        print(f'Você ACERTOU!\n')
        imprime_mensagem_vencedor()

    #  Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta15 != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta15} não exite. Tente novamente.\n')
            pergunta15 = str(input("07 - PERGUNTA PERIGOSA - \nEscolha uma alternativa correta sobre o tema  RESULTADO DA DIVERSIDADE NAS ORGANIZAÇÕES: \n[A] Os melhores resultados de um organização empresarial não esta relacionado a diversidade.\n[B] A Diversidade NÃO é um diferencial competitivo entre organizações empresariais.\n[C] Organizações empresariais que não possuem Diversidade atingem melhores resultados.\n[D] Diversidade traz crescimento e melhores resultados para organizações empresariais.\nEscolha  uma  alternativa:")).upper()
            if pergunta15 == "A":
                limpar_tela()
                acertos -= erro_perigosa
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Diversidade traz crescimento e melhores resultados para organizações empresariais.\n')
                imprime_mensagem_perdedor()
                break
            elif pergunta15 == "B":
                limpar_tela()
                acertos -= erro_perigosa
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Diversidade traz crescimento e melhores resultados para organizações empresariais.\n')
                imprime_mensagem_perdedor()
                break
            elif pergunta15 == "C":
                limpar_tela()
                acertos -= erro_perigosa
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Diversidade traz crescimento e melhores resultados para organizações empresariais.\n')
                imprime_mensagem_perdedor()
                break
            elif pergunta15 == "D":
                limpar_tela()
                acertos += acerto_perigosa
                print(f'Você ACERTOU!\n')
                imprime_mensagem_vencedor()
                break

    # 08 Pergunta Ambiente Diverso

    pergunta16 = str(input("08 - PERGUNTA PERIGOSA - \nEscolha uma alternativa correta sobre o tema  AMBIENTE DIVERSO NAS ORGANIZAÇÕES: \n[A] A contratação de pessoas diversas não precisa da parceria do RH e Gestores.\n[B] A Diversidade dentro das Organizações empresariais impactam a sociedade.\n[C] Organizações empresariais não precisam de Diversidade.\n[D] A sociedade não é impactada com a Diversidade dentro das organizações empresariais.\nEscolha  uma  alternativa:")).upper()
    if pergunta16 == "A":
        limpar_tela()
        acertos -= erro_perigosa
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] A Diversidade dentro das Organizações empresariais impactam a sociedade.\n')
        imprime_mensagem_perdedor()
    elif pergunta16 == "B":
        limpar_tela()
        acertos += acerto_perigosa
        print(f'Você ACERTOU!\n')
        imprime_mensagem_vencedor()
    elif pergunta16 == "C":
        limpar_tela()
        acertos -= erro_perigosa
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] A Diversidade dentro das Organizações empresariais impactam a sociedade.\n')
        imprime_mensagem_perdedor()
    elif pergunta16 == "D":
        limpar_tela()
        acertos -= erro_perigosa
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] A Diversidade dentro das Organizações empresariais impactam a sociedade.\n')
        imprime_mensagem_perdedor()

    #  Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta16 != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta16} não exite. Tente novamente.\n')
            pergunta16 = str(input("08 - PERGUNTA PERIGOSA - \nEscolha uma alternativa correta sobre o tema  AMBIENTE DIVERSO NAS ORGANIZAÇÕES: \n[A] A contratação de pessoas diversas não precisa da parceria do RH e Gestores.\n[B] A Diversidade dentro das Organizações empresariais impactam a sociedade.\n[C] Organizações empresariais não precisam de Diversidade.\n[D] A sociedade não é impactada com a Diversidade dentro das organizações empresariais.\nEscolha  uma  alternativa:")).upper()
            if pergunta16 == "A":
                limpar_tela()
                acertos -= erro_perigosa
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] A Diversidade dentro das Organizações empresariais impactam a sociedade.\n')
                imprime_mensagem_perdedor()
                break
            elif pergunta16 == "B":
                limpar_tela()
                acertos += acerto_perigosa
                print(f'Você ACERTOU!\n.')
                imprime_mensagem_vencedor()
                break
            elif pergunta16 == "C":
                limpar_tela()
                acertos -= erro_perigosa
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] A Diversidade dentro das Organizações empresariais impactam a sociedade.\n')
                imprime_mensagem_perdedor()
                break
            elif pergunta16 == "D":
                limpar_tela()
                acertos -= erro_perigosa
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] A Diversidade dentro das Organizações empresariais impactam a sociedade.\n')
                imprime_mensagem_perdedor()
                break


    # 09 Pergunta Ambiente Diverso programas de inclusão de diversidade ( Trainee Magalu, Empretece, VamoAI, PROA, Reprograma)

    pergunta16 = str(input("09 - PERGUNTA PRATA - \nEmpresas como Ifood  tem um grande sonho e vontade de promover mudanças e impactar\n"
                           "a sociedade, gerando oportunidade por meio da educação e promovendo programas de inclusão de grupos minoritários\n"
                           "em sua organização, assinale a alternativa de um  programa que não tem  relação com o Ifood:\n[A] VamoAi | Programa de formação de Backend focado  em Dados.\n[B] PrograMARIA - emponderar mulheres no meio da tecnologia.\n[C] PROA | Curso de Educação Profissionalizante em parceria com o Instituto Proa.\n[D] REPROGRAMA | Capacitação para programadoras mulheres.\nEscolha  uma  alternativa:")).upper()
    if pergunta16 == "A":
        limpar_tela()
        acertos -= erro_ouro
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[B] PrograMARIA - emponderar mulheres no meio da tecnologia\n')
    elif pergunta16 == "B":
        limpar_tela()
        acertos += acerto_ouro
        print(f'Você ACERTOU!\n')
    elif pergunta16 == "C":
        limpar_tela()
        acertos -= erro_ouro
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[B] PrograMARIA - emponderar mulheres no meio da tecnologia\n')
    elif pergunta16 == "D":
        limpar_tela()
        acertos -= erro_ouro
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[B] PrograMARIA - emponderar mulheres no meio da tecnologia\n')

    #  Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta16 != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta16} não exite. Tente novamente.\n')
            pergunta16 = str(input("09 - PERGUNTA PRATA - \nEmpresas como Ifood  tem um grande sonho e vontade de promover mudanças e impactar\n"
                                   "a sociedade, gerando oportunidade por meio da educação e promovendo programas de inclusão de grupos minoritários\n"
                                   "em sua organização, assinale a alternativa de um programa que não tem  relação com o Ifood:\n[A] VamoAi | Programa de formação de Backend focado  em Dados.\n[B] PrograMARIA - emponderar mulheres no meio da tecnologia.\n[C] PROA | Curso de Educação Profissionalizante em parceria com o Instituto Proa.\n[D] REPROGRAMA | Capacitação para programadoras mulheres.\nEscolha  uma  alternativa:")).upper()
            if pergunta16 == "A":
                limpar_tela()
                acertos -= erro_ouro
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[B] PrograMARIA - emponderar mulheres no meio da tecnologia\n')
                break
            elif pergunta16 == "B":
                limpar_tela()
                acertos += acerto_ouro
                print(f'Você ACERTOU!\n.')
                imprime_mensagem_vencedor()
                break
            elif pergunta16 == "C":
                limpar_tela()
                acertos -= erro_ouro
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[B] PrograMARIA - emponderar mulheres no meio da tecnologia\n')
                break
            elif pergunta16 == "D":
                limpar_tela()
                acertos -= erro_ouro
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[B] PrograMARIA - emponderar mulheres no meio da tecnologia\n')
                break

    cabecalho_fase_tres()

    # 10 Pergunta Ambiente Diverso ( Detalhar sobre os programas Empretece, VamoAI, PROA, Reprograma)

    pergunta16 = str(input("10 - PERGUNTA PRATA - \nQual o nome do programa de contratação exclusivo para pessoas negras do Grupo Movile no qual o Ifood faz parte:\n[A] Trainee para pessoas negras.\n[B] Empretece - Programa para pessoas negras.\n[C] Nós codamos -  inclusão da comunidade negra.\n[D] Protagonismo Preto - programa para pessoas negras.\nEscolha  uma  alternativa:")).upper()
    if pergunta16 == "A":
        limpar_tela()
        acertos -= erro_ouro
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Empretece - Programa para pessoas negras.\n')
    elif pergunta16 == "B":
        limpar_tela()
        acertos += acerto_ouro
        print(f'Você ACERTOU!\n')
        imprime_mensagem_vencedor()
    elif pergunta16 == "C":
        limpar_tela()
        acertos -= erro_ouro
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Empretece - Programa para pessoas negras.\n')
    elif pergunta16 == "D":
        limpar_tela()
        acertos -= erro_ouro
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Empretece - Programa para pessoas negras.\n')

    #  Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta16 != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta16} não exite. Tente novamente.\n')
            pergunta16 = str(input("10 - PERGUNTA PRATA - \nQual o nome do programa de contratação exclusivo para pessoas negras do Grupo Movile no qual o Ifood faz parte.  .\n[A] Trainee para pessoas negras.\n[B] Empretece - Programa para pessoas negras.\n[C] Nós codamos -  inclusão da comunidade negra.\n[D] Protagonismo Preto - programa para pessoas negras.\nEscolha  uma  alternativa:")).upper()
            if pergunta16 == "A":
                limpar_tela()
                acertos -= erro_ouro
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Empretece - Programa para pessoas negras.\n')
                break
            elif pergunta16 == "B":
                limpar_tela()
                acertos += acerto_ouro
                print(f'Você ACERTOU!\n.')
                break
            elif pergunta16 == "C":
                limpar_tela()
                acertos -= erro_ouro
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Empretece - Programa para pessoas negras.\n')
                break
            elif pergunta16 == "D":
                limpar_tela()
                acertos -= erro_ouro
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Empretece - Programa para pessoas negras.\n')
                break

    continuar_jogo()


cabecalho_programa()
introducao_jogo()
continuar_jogo()
