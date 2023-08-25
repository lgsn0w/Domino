class Tabuleiro:
    def __init__(self):
        self.pecas_esquerda = []
        self.pecas_direita = []

    def adicionarPecaEsquerda(self, peca):
        self.pecas_esquerda.insert(0, peca)

    def adicionarPecaDireita(self, peca):
        self.pecas_direita.append(peca)

    def printTabuleiro(self):
        print("Tabuleiro:")
        self._printBranch(self.pecas_esquerda[::-1])
        print(f" {self.pecas_esquerda[-1][0]}-{self.pecas_esquerda[-1][1]} ", end="->")
        self._printBranch(self.pecas_direita)
        print("\n")

    def _printBranch(self, branch):
        for peca in branch:
            print(f"{peca[0]}-{peca[1]}", end="<-")
