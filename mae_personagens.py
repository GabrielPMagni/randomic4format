from random import randint

# atributos
forca = 0
destreza = 0
constituicao = 0
inteligencia = 0
sabedoria = 0
carisma = 0

# passivas de raça
deslocamento_anao = {'Devagar e Sempre': 4}  # deslocamento 6 e sem penalidade de armadura (6 metros = 4 quadrados)
deslocamento_normal = {'Deslocamento Normal': 6, 'Deslocamento de Armadura (Média ou Pesada)': 4}  # deslocamento elfo, meio elfo, meio orc e humano (9 metros = 6 quadrados)
deslocamento_lento = {'Deslocamento Lento': 4, 'Deslocamento Lento de Armadura (Média ou Pesada)': 3}  #deslocamento gnomo e halfling (6 metros = 4 quadrados)
tamanho_pequeno = {'Bônus de Classe de Armadura': 1, 'Bônus de Ataque': 1, 'Bônus em Manobra de Combate': -1, 'Defesa Contra Manobra de Combate': -1, 'Furtividade': 4}


visao = {'Visão no Escuro': 18, }

def nomear():  # sobre o player
    nome = input('Digite o nome do personagem: ')
    jogador = input('Digite o nome do jogador: ')
    return nome, jogador


def rolar_dados(a):  # dados
    if a == 4:
        dado = randint(1, 4)
        return dado
    elif a == 6:
        dado = randint(1, 6)
        return dado
    elif a == 8:
        dado = randint(1, 8)
        return dado
    elif a == 10:
        dado = randint(1, 10)
        return dado
    elif a == 12:
        dado = randint(1, 12)
        return dado
    elif a == 16:
        dado = randint(1, 16)
        return dado
    elif a == 20:
        dado = randint(1, 20)
        return dado
    elif a == 30:
        dado = randint(1, 30)
        return dado
    elif a == 100:
        dado = randint(1, 100)
        return dado

'''

def criar_classe():  # escolha da classe
    try:
        num_classe = int(input('\n\tQual raça deseja criar?'
                               '\n\t1- Anão'
                               '\n\t2- Elfo'
                               '\n\t3- Gnomo'
                               '\n\t4- Halfling'
                               '\n\t5- Humano'
                               '\n\t6- Meio Elfo'
                               '\n\t7- Meio Orcs'))
        if num_classe not in range(1, 7):
            print('Valor  inválido, tente novamente.\n\n')
            return criar_classe()
        elif num_classe == 1:
            anao()
        elif num_classe == 2:
            elfo()
        elif num_classe == 3:
            gnomo()
        elif num_classe == 4:
            halfling()
        elif num_classe == 5:
            humano()
        elif num_classe == 6:
            meio_elfo()
        elif num_classe == 7:
            meio_orc()
        else:
            pass
    except ValueError:
        print('Valor inválido, deve ser um número inteiro. Tente novamente. \n\n')
        return criar_classe()
'''

def anao(constituicao, sabedoria, carisma):
    constituicao += 2
    sabedoria += 2
    carisma -= 2


def elfo(destreza, inteligencia, constituicao):
    destreza += 2
    inteligencia += 2
    constituicao -+ 2

def gnomo():
    pass

def rolar_atributos():
    try:
        lista_atributos = []
        escolha = int(input('Digite o tipo de rolagem de atributos \n1 = Padrão\n2 = Clássico\n3 = Heróico\n\n\t>'))
        if escolha == 1:
            print('Rolagem Padrão selecionada:\n')
            for i in range(6):
                linha = []
                for j in range(4):
                    linha.append(rolar_dados(6))

            lista_atributos.append(linha)
            return lista_atributos



            print(lista_atributos)


        elif escolha == 2:
            print('Rolagem Clássica selecionada\n')

        elif escolha == 3:
            print('Rolagem Heróica selecionada\n')

        else:
            print('Valor inválido, tente novamente Erro 2')
            return rolar_atributos()

    except ValueError:
        print('Valor inválido. Tente novamente. Erro 1')
        return rolar_atributos()

a = rolar_atributos()
print('valor de a:', a)