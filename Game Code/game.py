from models.calcular import Calcular

def Main() -> None:
    
    pontos: int = 0

    jogar(pontos)

def jogar(pontos: int) -> None:
    
    dificuldade: int = int(input("Informe o nível de dificuldade [1, 2, 3 ou 4]: "))

    calcular: Calcular = Calcular(dificuldade)

    print("Informe o seguinte resultado para a proxima operação: ")

    calcular.mostrar_operacao()

    resultado: int = int(input("Resposta: "))

    if calcular.checar_resultado(resultado):
        pontos += 1
        print(f"Você tem {pontos} pontos!")

    continuar: int = int(input("Deseja continuar no jogo [1 - sim, 0 - não]: "))

    if continuar:
        jogar(pontos)
    else:
        print(f"Você finalizou com {pontos} pontos!")
        print("Parabêns! Até a proxima...")


if __name__ == "__main__":
    Main()