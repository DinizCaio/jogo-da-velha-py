tabuleiro = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
    ]

jogador = "X"

def exibirTabuleiro():
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 10)

def jogada(linha, coluna):
    if (tabuleiro[linha][coluna] != ""):
        print("Jogada inválida, a casa já está ocupada.")
        return jogador
    
    if(
        not 0 <= linha <= 2 or
        not 0 <= coluna <= 2
    ):
        print("Jogada inválida, digite um valor númerico entre 0 e 2.")
        return jogador
    
    tabuleiro[linha][coluna] = jogador
    return "O" if jogador == "X" else "X"

def verificadorLinhas():
    """Verifica se houve ganhador nas linhas"""
    for linha in range(3):
        if(
            tabuleiro[linha][0] ==
            tabuleiro[linha][1] ==
            tabuleiro[linha][2] != ""
        ):
            print(f"Jogador {tabuleiro[linha][0]} ganhou, VITÓRIA!")
            return True
        
def verificadorColunas():
    """Verifica se houve ganhador nas colunas"""
    for coluna in range(3):
        if(
            tabuleiro[0][coluna] ==
            tabuleiro[1][coluna] ==
            tabuleiro[2][coluna] != ""
        ):
            print(f"Jogador {tabuleiro[0][coluna]} ganhou, VITÓRIA!")
            return True
        
def verificadorDiagonais():
    """Verifica se houve ganhador nas diagonais"""
    if(
        tabuleiro[1][1] ==
        tabuleiro[0][0] ==
        tabuleiro[2][2] != ""
    )or(
        tabuleiro[1][1] ==
        tabuleiro[0][2] ==
        tabuleiro[2][0] != ""
    ): 
        print(f"Jogador {tabuleiro[1][1]} ganhou, VITÓRIA!")
        return True

def verificadorEmpate():
    """Verifica se o jogo terminou empatado"""
    for linha in range(3):
        for coluna in range(3):
            if(tabuleiro[linha][coluna] == ""):
                return False
    print("Eita! Deu velha!")
    return True       

def verificador():
    """Função para chamar todos os verificadores"""
    if(
        verificadorLinhas() or
        verificadorColunas() or
        verificadorDiagonais()or
        verificadorEmpate() ==
        True
    ):
        return True

while True:
    print(f"Vez do jogador {jogador}")
    try:
        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))
        jogador = jogada(linha, coluna)

    except IndexError:
        print("Jogada inválida, digite um valor númerico entre 0 e 2.")

    except ValueError:
        print("Jogada inválida, digite um valor númerico entre 0 e 2.")

    exibirTabuleiro()

    if verificador():
        break