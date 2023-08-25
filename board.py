class Tabuleiro:
    def __init__(self):
        self.pecas_esquerda = []
        self.pecas_direita = []


     #TODO LISTA:
     #1 - ARRANJAR ALGUM JEITO DE IMPRIMIR O TABULEIRO DE UMA FORMA MAIS BONITA OU CENTRALIZADA
     #2 - ADICIONAR CHECAGEM NOS METODOS DE ADICIONAR PEÇA PARA VER SE A PEÇA É VALIDA
     #3 - DESCOBRIR COMO INICIALIZAR COM 6,6 A PARTIR DA PILHA DE PEÇAS (SEM DAR ERRO)
     #4 - ACERTAR A DIREÇÃO DO FLUXO DE JOGO (<- ESQUERDA DIREITA -> |||||  AO INVES DE <- <-)
     #5 - ME MATAR (IMPORTANTE!!!!)
    

    def adicionarPecaInicial(self, peca):
        self.pecas_esquerda.append(peca)
        self.pecas_direita.append(peca)

    def adicionarPecaEsquerda(self, peca):
        self.pecas_esquerda.insert(0, peca)

    def adicionarPecaDireita(self, peca):
        self.pecas_direita.append(peca)

    def printTabuleiro(self):
        print("Tabuleiro:")

        if self.pecas_esquerda:
            self._printBranch(self.pecas_esquerda[::-1])  # Print the left branch in reverse order
            print(f" {self.pecas_esquerda[-1][0]}-{self.pecas_esquerda[-1][1]}", end=" ")



        self._printBranch(self.pecas_direita)
        print("\n")

    def _printBranch(self, branch):
        for peca in branch:
            print(f"{peca[0]}-{peca[1]}", end="<-")
