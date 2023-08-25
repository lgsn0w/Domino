import listaPecas
import random


class Player:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []

    def adicionarPeca(self, peca):
        self.mao.append(peca)

    def jogarPeca(self, peca):
        if lado == "esquerda":
            self.mao.remove(peca)
            tabuleiro.adicionarPecaEsquerda(peca)
        elif lado == "direita":
            self.mao.remove(peca)
            game_board.adicionarPecaDireita(peca)

    def drawHand(self):
        pecas_draw = 7
        pecas_aleatorias = random.sample(listaPecas.pecas, pecas_draw)
        for peca in pecas_aleatorias:
            self.adicionarPeca(peca)
            listaPecas.pecas.remove(peca)

    def printMao(self):
        print("Mão do jogador: ", self.nome)
        for index,peca in enumerate(self.mao):
            print(f"{index + 1} - {peca[0]}-{peca[1]}")

    @classmethod
    def numero_jogadores(cls):
        numero_jogadores = int(input("Quantos jogadores?"))
        jogadores = []
        for i in range(numero_jogadores):
            nome = input(f"Qual o nome do jogador {i + 1}?")
            jogador = cls(nome)
            jogadores.append(jogador)
        return jogadores

    def setupMoes(jogadores):
        for jogador in jogadores:
            jogador.drawHand()
            jogador.printMao()
            print("")

    def checkDuploSeis(jogadores):
        for jogador in jogadores:
            for peca in jogador.mao:
                if peca == (6,6):
                    print(f"O jogador {jogador.nome} começa o jogo!")
                    return
        else:
            print("Nenhum jogador tem o duplo seis, a peça sera jogada diretamente no tabuleiro")

    def turnoJogador(self):
        index_peca = int(input("Escolha o index de uma peça para jogar:"))
        if index_peca >= 1 and index_peca <= len(self.mao):
            peca = self.mao[index_peca - 1]
            self.jogarPeca(peca)
            return peca
