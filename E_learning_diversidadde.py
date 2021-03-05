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


# imprime mensagem quando o jogador perder


#  def imprime_mensagem_perdedor():
# print("Puxa, você foi enforcado!")
#   print("    _______________        ")
#    print("   /               \       ")
#    print("  /                 \      ")
#    print("//                   \/\   ")
#    print("\|   XXXX     XXXX   | /   ")
#    print(" |   XXXX     XXXX   |/    ")
#    print(" |   XXX       XXX   |     ")
#    print(" |                   |     ")
#    print(" \__      XXX      __/     ")
#    print("   |\     XXX     /|       ")
#    print("   | |           | |       ")
#    print("   | I I I I I I I |       ")
#    print("   |  I I I I I I  |       ")
#    print("   \_             _/       ")
#   print("     \_         _/         ")
#    print("       \_______/           ")


# cabeçalho do programa


def cabecalho_programa():
    print('-' * 81)
    print(f'{"E-learning : DIVERSIDADE E EQUIDADE NAS ORGANIZAÇÕES":^81}')
    print('-' * 81)


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
    print('-' * 81)
    print(texto_introducao_jogo)
    print('-' * 81)


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
                 '\n' + 'Para vencer neste QUIZ é preciso fazer 80 pontos, teremos' + \
                 '\n' + '4 Perguntas PERIGOSAS, você pontuará 10 pontos se acertar e -80 pontos se errar. ' + \
                 '\n' + '2 Perguntas OURO, você pontuará 80 pontos em cada, ou seja acertando uma delas, você vencerá o QUIZ.' + \
                 '\n' + '4 Perguntas PRATA, você pontuará 10 pontos em cada resposta certa.'
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
    pontos = 0
    limpar_tela()
    pergunta1 = str(input("Escolha uma alternativa que melhor represente a DIVERSIDADE: \n[A] Física, Morais, Religosas, Culturais , Musicalidade.\n[B] Física, Morais, Religosas, Artística , Ideologicas.\n[C] Física, Morais, Temporal, Culturais , Ideologicas.\n[D] Física, Morais, Religosas, Culturais , Ideologicas.\nEscolha  uma  alternativa:")).upper()
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
        pontos += 10
        print(f'Você ACERTOU!\nO seu placar é de {pontos} pontos.')

    # Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta1 != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta1} não exite. Tente novamente.\n')
            pergunta1 = str(input("Escolha uma alternativa que melhor represente a DIVERSIDADE: \n[A] Física, Morais, Religosas, Culturais , Musicalidade.\n[B] Física, Morais, Religosas, Artística , Ideologicas.\n[C] Física, Morais, Temporal, Culturais , Ideologicas.\n[D] Física, Morais, Religosas, Culturais , Ideologicas.\nEscolha  uma  alternativa:")).upper()
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
                pontos += 10
                print(f'Você ACERTOU!\nO seu placar é de {pontos} pontos.\n')
                break


#  Quiz do tema EQUIDADE


def quiz_equidade():
    eq_pontos = 0
    limpar_tela()
    pergunta2 = str(input(
        "Escolha uma alternativa que melhor represente a EQUIDADDE: \n[A] Equidade é adaptar  as oportunidades  deixando-as justas.\n[B] Desigualdade é o antônimo de equidade.\n[C] Equidade tem o mesmo significado que igualdade.\n[D] Equidade é dar as mesmas oportunidades..\nEscolha  uma  alternativa:")).upper()
    if pergunta2 == "A":
        limpar_tela()
        eq_pontos += 10
        print(f'Você ACERTOU!\nO seu placar é de {eq_pontos} pontos.')
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
                eq_pontos += 10
                print(f'Você ACERTOU!\nO seu placar é de {eq_pontos} pontos.')
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
    minoritario_pontos = 0
    limpar_tela()
    pergunta3 = str(input(
        "Escolha uma alternativa que melhor represente a GRUPO MINORITÁRIO: \n[A] Homem Branco, Mulher Negra, Homem Negro, LGBTQIA+.\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n[C] Mulheres, Heterosexual, Deficiente, LGBTQIA+.\n[D] Homem Branco, Heterosexual, Deficiente, LGBTQIA+.\nEscolha  uma  alternativa:")).upper()
    if pergunta3 == "A":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')
    elif pergunta3 == "B":
        limpar_tela()
        minoritario_pontos += 10
        print(f'Você ACERTOU!\nO seu placar é de {minoritario_pontos} pontos.')
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
            pergunta3 = str(input("Escolha uma alternativa que melhor represente a GRUPO MINORITÁRIO: \n[A] Homem Branco, Mulher Negra, Homem Negro, LGBTQIA+.\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n[C] Mulheres, Heterosexual, Deficiente, LGBTQIA+.\n[D] Homem Branco, Heterosexual, Deficiente, LGBTQIA+.\nEscolha  uma  alternativa:")).upper()
            if pergunta3 == "A":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')
                break
            elif pergunta3 == "B":
                limpar_tela()
                minoritario_pontos += 10
                print(f'Você ACERTOU!\nO seu placar é de {minoritario_pontos} pontos.')
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
    opressoes_pontos = 0
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
        opressoes_pontos += 10
        print(f'Você ACERTOU!\nO seu placar é de {opressoes_pontos} pontos.')
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
                opressoes_pontos += 10
                print(f'Você ACERTOU!\nO seu placar é de {opressoes_pontos} pontos.')
                break
            elif pergunta4 == "D":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Não existe estrutura de opressão.\n')
                break


#  Quiz do tema GRUPOS HOMOGÊNEOS


def quiz_gp_homogeneos():
    homogeneos_pontos = 0
    limpar_tela()
    pergunta5 = str(input(
        "Escolha uma alternativa incorreta sobre o tema  GRUPO HOMOGÊNEO: \n[A] Pessoas deste grupo possuem crenças diferentes.\n[B] Pessoas deste grupo são da mesma origem.\n[C] Pessoas deste grupo possuem a mesma formação educacional.\n[D] Pessoas deste grupo possuem estrutura familiar parecida.\nEscolha  uma  alternativa:")).upper()
    if pergunta5 == "A":
        limpar_tela()
        homogeneos_pontos += 10
        print(f'Você ACERTOU!\nO seu placar é de {homogeneos_pontos} pontos.')
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
                homogeneos_pontos += 10
                print(f'Você ACERTOU!\nO seu placar é de {homogeneos_pontos} pontos.')
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
    heterogeneos_pontos = 0
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
        heterogeneos_pontos += 10
        print(f'Você ACERTOU!\nO seu placar é de {heterogeneos_pontos} pontos.')
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
                heterogeneos_pontos += 10
                print(f'Você ACERTOU!\nO seu placar é de {heterogeneos_pontos} pontos.')
                break
            elif pergunta6 == "D":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[C] Pessoas deste grupo possuem a mesma formação educacional.\n')
                break


#  Quiz do tema RESULTADO DA DIVERSIDADE NAS ORGANIZAÇÕES


def quiz_resultado_diversidade():
    result_diversidade_pontos = 0
    limpar_tela()
    pergunta7 = str(input(
        "Escolha uma alternativa correta sobre o tema  RESULTADO DA DIVERSIDADE NAS ORGANIZAÇÕES: \n[A] Uma Organição empresarial não precisa de Diversidade  para atingir melhores resultados.\n[B] A Diversidade não é um diferencial competitivo entre organizações empresariais.\n[C] Organizações empresariais que não possuem Diversidade atingem melhores resultados.\n[D] Diversidade esta  relacionada à sobrevivência e ao crescimento de organizações empresariais.\nEscolha  uma  alternativa:")).upper()
    if pergunta7 == "A":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Diversidade esta relacionada à sobrevivência e ao crescimento de organizações empresariais..\n')
    elif pergunta7 == "B":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Diversidade esta relacionada à sobrevivência e ao crescimento de organizações empresariais.\n')
    elif pergunta7 == "C":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Diversidade esta relacionada à sobrevivência e ao crescimento de organizações empresariais.\n')
    elif pergunta7 == "D":
        limpar_tela()
        result_diversidade_pontos += 10
        print(f'Você ACERTOU!\nO seu placar é de {result_diversidade_pontos} pontos.')

    #  Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta7 != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta7} não exite. Tente novamente.\n')
            pergunta7 = str(input(
                "Escolha uma alternativa correta sobre o tema  RESULTADO DA DIVERSIDADE NAS ORGANIZAÇÕES: \n[A] Uma Organição empresarial não precisa de Diversidade  para atingir melhores resultados.\n[B] A Diversidade não é um diferencial competitivo entre organizações empresariais.\n[C] Organizações empresariais que não possuem Diversidade atingem melhores resultados.\n[D] Diversidade esta  relacionada à sobrevivência e ao crescimento de organizações empresariais.\nEscolha  uma  alternativa:")).upper()
            if pergunta7 == "A":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Diversidade esta relacionada à sobrevivência e ao crescimento de organizações empresariais..\n')
                break
            elif pergunta7 == "B":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Diversidade esta relacionada à sobrevivência e ao crescimento de organizações empresariais..\n')
                break
            elif pergunta7 == "C":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Diversidade esta relacionada à sobrevivência e ao crescimento de organizações empresariais..\n')
                break
            elif pergunta7 == "D":
                limpar_tela()
                result_diversidade_pontos += 10
                print(f'Você ACERTOU!\nO seu placar é de {result_diversidade_pontos} pontos.')
                break


#  Quiz do tema AMBIENTE DIVERSO NAS ORGANIZAÇÕES

def quiz_ambiente_diverso():
    ambiente_diverso_pontos = 0
    limpar_tela()
    pergunta8 = str(input(
        "Escolha uma alternativa correta sobre o tema  AMBIENTE DIVERSO NAS ORGANIZAÇÕES: \n[A] A contratação de pessoas diversas não precisa da parceria do RH e Gestores.\n[B] A Diversidade dentro das Organizações empresariais impactam a sociedade.\n[C] Organizações empresariais não precisam de Diversidade.\n[D] A sociedade não é impactada com a Diversidade dentro das organizações empresariais.\nEscolha  uma  alternativa:")).upper()
    if pergunta8 == "A":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] A Diversidade dentro das Organizações empresariais impactam a sociedade.\n')
    elif pergunta8 == "B":
        limpar_tela()
        ambiente_diverso_pontos += 10
        print(f'Você ACERTOU!\nO seu placar é de {ambiente_diverso_pontos} pontos.')
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
                ambiente_diverso_pontos += 10
                print(f'Você ACERTOU!\nO seu placar é de {ambiente_diverso_pontos} pontos.')
                break
            elif pergunta8 == "C":
                limpar_tela()
                ambiente_diverso_pontos += 10
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] A Diversidade dentro das Organizações empresariais impactam a sociedade.\n')
                break
            elif pergunta8 == "D":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] A Diversidade dentro das Organizações empresariais impactam a sociedade.\n')
                break


def quiz_final():

    print('QUIZ FINAL')

    texto_pontos = 'Parabéns,Você chegou na terceira fase, onde teremos um grande desafio com um QUIZ, com 10 perguntas.' + \
                   '\n' + 'REGRAS:' + \
                   '\n' + 'Para vencer neste QUIZ é preciso fazer 80 pontos, teremos' + \
                   '\n' + '4 Perguntas PERIGOSAS, você pontuará 10 pontos se acertar e -80 pontos se errar. ' + \
                   '\n' + '2 Perguntas OURO, você pontuará 80 pontos em cada, ou seja acertando uma delas, você vencerá o QUIZ.' + \
                   '\n' + '4 Perguntas PRATA, você pontuará 10 pontos em cada resposta certa.'

    # 01 Pergunta sobre  Diversidade

    acertos = 0

    limpar_tela()
    pergunta9 = str(input("- PERGUNTA PRATA - (Vale 10 PONTOS)\nEscolha uma alternativa incorreta sobre o tema  DIVERSIDADE: \n[A] Ao falar de diversidade estamos nos referindo ao direito dos grupos minoritários.\n[B] A Diversidade é um assunto que NÃO precisa ser debatido.\n[C] A Diversidade é um assunto que NÃO precisa ser debatido.\n[D] A Diversidade pode ser Física, Morais, Religosas, Culturais , Ideologicas.\nEscolha  uma  alternativa:")).upper()
    if pergunta9 == "A":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[D] Física, Morais, Religosas, Culturais\n')
    elif pergunta9 == "B":
        limpar_tela()
        acertos += 10
        print(f'Você ACERTOU!\n')
    elif pergunta9 == "C":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[D] Física, Morais, Religosas, Culturais\n')
    elif pergunta9 == "D":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[D] Física, Morais, Religosas, Culturais\n')

    # Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta9 != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta9} não exite. Tente novamente.\n')
            pergunta9 = str(input("- PERGUNTA PRATA - ( Vale 10 PONTOS )\nEscolha uma alternativa incorreta sobre o tema  DIVERSIDADE: \n[A] Ao falar de diversidade estamos nos referindo ao direito dos grupos minoritários\n[B] A Diversidade é um assunto que NÃO precisa ser debatido.\n[C] A Diversidade é um assunto que NÃO precisa ser debatido.\n[D] A Diversidade pode ser Física, Morais, Religosas, Culturais , Ideologicas.\nEscolha  uma  alternativa:")).upper()
            if pergunta9 == "A":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[D] Física, Morais, Religosas, Culturais')
                break
            elif pergunta9 == "B":
                limpar_tela()
                acertos += 10
                print(f'Você ACERTOU!\n')
                break
            elif pergunta9 == "C":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[D] Física, Morais, Religosas, Culturais')
                break
            elif pergunta9 == "D":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa incorreta é a:\n[D] Física, Morais, Religosas, Culturais')
                break

    print('-' * 30)
    print(f'{f"SEU PLACAR É DE {acertos} PONTOS":^30}')
    print('-' * 30)

    # 02 Pergunta Equidade

    # limpar_tela()
    pergunta10 = str(input("- PERGUNTA PRATA - ( Vale 10 PONTOS )\nEscolha uma alternativa correta sobre o tema  EQUIDADE:: \n[A] Equidade é dar oportunidades.\n[B] Desigualdade é o antônimo de equidade.\n[C] Equidade e igualdade são as mesmas coisas.\n[D] Equidade é adaptar as oportunidades  deixando-as justas.\nEscolha  uma  alternativa:")).upper()
    if pergunta10 == "A":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Equidade é adaptar as oportunidades  deixando-as justas.\n')
    elif pergunta10 == "B":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Equidade é adaptar as oportunidades  deixando-as justas.\n')
    elif pergunta10 == "C":
        limpar_tela()
        print(
            'Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Equidade é adaptar as oportunidades  deixando-as justas.\n')
    elif pergunta10 == "D":
        limpar_tela()
        acertos += 10
        print(f'Você ACERTOU!\n')

    #  Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta10 != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta10} não exite. Tente novamente.\n')
            pergunta10 = str(input("- PERGUNTA PRATA - ( Vale 10 PONTOS )\nEscolha uma alternativa correta sobre o tema  EQUIDADE:: \n[A] Equidade é dar oportunidades.\n[B] Desigualdade é o antônimo de equidade.\n[C] Equidade e igualdade são as mesmas coisas.\n[D] Equidade é adaptar as oportunidades  deixando-as justas.\nEscolha  uma  alternativa:")).upper()
            if pergunta10 == "A":
                limpar_tela()
                acertos += 10
                print(f'Você ACERTOU!\n.')
                break
            elif pergunta10 == "B":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Equidade é adaptar as oportunidades  deixando-as justas.\n')
                break
            elif pergunta10 == "C":
                limpar_tela()
                print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[D] Equidade é adaptar as oportunidades  deixando-as justas.\n')
                break
            elif pergunta10 == "D":
                limpar_tela()
                acertos += 10
                print(f'Você ACERTOU!\n')
                break

    print('-' * 30)
    print(f'{f"SEU PLACAR É DE {acertos} PONTOS":^30}')
    print('-' * 30)

    # 03 Pergunta Grupos Minoritários

    # limpar_tela()
    pergunta11 = str(input("- PERGUNTA PRATA - ( Vale 10 PONTOS )\n Escolha uma alternativa que melhor represente a GRUPO MINORITÁRIO: \n[A] Homem Branco, Mulher Negra, Homem Negro, LGBTQIA+.\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n[C] Mulheres, Heterosexual, Deficientes, LGBTQIA+.\n[D] Homem Branco, Heterosexual, Deficiente, LGBTQIA+.\nEscolha  uma  alternativa:")).upper()
    if pergunta11 == "A":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')
    elif pergunta11 == "B":
        limpar_tela()
        acertos += 10
        print(f'Você ACERTOU!\n')
    elif pergunta11 == "C":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')
    elif pergunta11 == "D":
        limpar_tela()
        print('Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')

    #  Caso o usuário informe uma opção que não existe , o programa irá solicita a inserção até que ele informe uma opção existente

    elif pergunta11 != "ABCD":
        while True:
            limpar_tela()
            print(f'A opção {pergunta11} não exite. Tente novamente.\n')
            pergunta11 = str(input(
                "Escolha uma alternativa que melhor represente a GRUPO MINORITÁRIO: \n[A] Homem Branco, Mulher Negra, Homem Negro, LGBTQIA+.\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n[C] Mulheres, Heterosexual, Deficiente, LGBTQIA+.\n[D] Homem Branco, Heterosexual, Deficiente, LGBTQIA+.\nEscolha  uma  alternativa:")).upper()
            if pergunta11 == "A":
                limpar_tela()
                print(
                    'Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')
                break
            elif pergunta11 == "B":
                limpar_tela()
                acertos += 10
                print(f'Você ACERTOU!\n.')
                break
            elif pergunta11 == "C":
                limpar_tela()
                print(
                    'Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')
                break
            elif pergunta11 == "D":
                limpar_tela()
                print(
                    'Poxaaaa, Foi quase !\nA alternativa correta é a:\n[B] Mulheres, Homem Negro, Deficiente, LGBTQIA+.\n')
                break

    print('-' * 30)
    print(f'{f"SEU PLACAR É DE {acertos} PONTOS":^30}')
    print('-' * 30)

    # 04 Pergunta Estrutura de Opressões

    # 05 Pergunta Grupo Homogêneo

    # 06 Pergunta Grupo Heterogêneo

    # 07 Pergunta Resultado de Diversidade nas organizações

    # 08 Pergunta Ambiente Diverso

    # 09 Pergunta Ambiente Diverso programas de inclusão de diversidade ( Trainee Magalu, Empretece, VamoAI, PROA, Reprograma)

    # 10 Pergunta Ambiente Diverso ( Detalhar sobre os programas Empretece, VamoAI, PROA, Reprograma)


cabecalho_programa()
introducao_jogo()
continuar_jogo()
