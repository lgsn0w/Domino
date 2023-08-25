from player import Player
from board import Tabuleiro

def main():
    lista_jogadores = Player.numero_jogadores()
    for jogador in lista_jogadores:
        jogador.drawHand()
        jogador.printMao()
        print("")

    game_board = Tabuleiro() 
    game_board.adicionarPecaInicial((6,6)) #pq caralhos esta porra adiciona 3 peças?
    Player.checkDuploSeis(lista_jogadores)
    #TODO - FORÇAR O JOGADOR COM O DUPLO SEIS A SER O PRIMEIRO A JOGAR A PEÇA



    while True:
        game_board.printTabuleiro()

        player_index = int(input("Escolha o número do jogador: ")) - 1
        jogador_atual = lista_jogadores[player_index]

        tile_index = int(input("Escolha o número da peça: ")) - 1
        peca_escolhida = jogador_atual.mao[tile_index]

        lado_escolhido = input("Escolha o lado (esquerda/direita): ")

        jogador_atual.jogarPeca(peca_escolhida, lado_escolhido)

if __name__ == "__main__":
    main()
