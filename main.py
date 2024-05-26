# Importando os módulos
import jogo as j
import fileHandler as fh

# Menu principal
def menu():
    print('=' * 30)
    print(' ' * 7 + 'JOGO DA FORCA')
    print('=' * 30)
    print('\n1 - JOGAR')
    print('2 - SCORE')
    print('3 - SAIR\n')
    print('=' * 30)
    
# Criando e localizando o arquivo "score.txt"
arquivo = 'score.txt'
if fh.existeArquivo(arquivo):
    print('Arquivo localizado.')
else:
    print('Arquivo não existe.')
    fh.criarArquivo(arquivo)
    
# Laço de repetição principal 
while True:
    menu()
    opcao = int(input('Escolha a opção (1/2/3): '))
    
    match opcao:
        case 1:
            print('Iniciar jogo!')
            j.jogar()
        case 2:
            print('SCORE')
            dados = fh.listarArquivo('score.txt')
            if not dados:
                    print('Score vazio.')
            else:
                i = 1
                for jogador in dados:
                    jogador = jogador.split(';')
                    print(f'{i} -> {jogador[0]}, Pontuação: {jogador[1]}')
                    i += 1
        case 3:
            print('Saindo do jogo...')
            break
        case _:
            print('Opção inválida. Tente outra opção.')