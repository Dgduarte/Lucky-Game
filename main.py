from time import sleep
from random import randint

# Textos do jogo centralizados por idioma
TEXTOS = {
    'P': {
        'instrucoes': 'Escolha de 1 a 5. Se acertar o número do computador, você vence!',
        'pedir_num': 'Digite um número entre 1 e 5: ',
        'erro_num': '❌ Digite um número INTEIRO válido entre 1 e 5!\n',
        'sorte': 'Testando sua sorte',
        'resultado': '\nComputador escolheu {} e você escolheu {}',
        'vitoria': '🎉 Você venceu!!',
        'derrota': '💻 O computador venceu!!',
        'placar': 'PLACAR: Jogador {} x {} Computador',
        'continuar': '\nDeseja jogar novamente? [S/N]: ',
        'opcoes_cont': 'SN',
        'tchau': 'Obrigado por jogar!'
    },
    'E': {
        'instrucoes': 'Pick a number from 1 to 5. If you match the computer, you win!',
        'pedir_num': 'Type a number between 1 and 5: ',
        'erro_num': '❌ Please enter a VALID integer between 1 and 5!\n',
        'sorte': 'Testing your luck',
        'resultado': '\nComputer chose {} and you chose {}',
        'vitoria': '🎉 You win!!',
        'derrota': '💻 Computer wins!!',
        'placar': 'SCORE: Player {} x {} Computer',
        'continuar': '\nDo you want to play again? [Y/N]: ',
        'opcoes_cont': 'YN',
        'tchau': 'Thanks for playing!'
    }
}

def animacao_pontos(qtd=3, tempo=0.4):
    for _ in range(qtd):
        print('.', end='', flush=True)
        sleep(tempo)
    print()

# Cabeçalho
print("-=" * 25)
print("JOGO DA SORTE / GAME OF LUCK".center(50))
print("-=" * 25)

# Seleção segura de idioma
while True:
    lingua = input("Language / Idioma ([P]ortuguês / [E]nglish): ").strip().upper()
    if lingua in ('P', 'E'):
        break
    print("Opção inválida! / Invalid option!\n")

t = TEXTOS[lingua]
print(f"\n{t['instrucoes']}")
animacao_pontos(3, 0.4)

# Placar
vitorias_jogador = 0
vitorias_pc = 0

# Loop principal do jogo (apenas UM para ambos os idiomas!)
while True:
    # Validação segura do número
    while True:
        try:
            n1 = int(input(f"\n{t['pedir_num']}"))
            if 1 <= n1 <= 5:
                break
            print(t['erro_num'])
        except ValueError:
            print(t['erro_num'])

    print(t['sorte'], end='')
    animacao_pontos(3, 0.3)

    alea = randint(1, 5)
    print(t['resultado'].format(alea, n1))
    sleep(0.5)

    if n1 == alea:
        print(t['vitoria'])
        vitorias_jogador += 1
    else:
        print(t['derrota'])
        vitorias_pc += 1

    # Mostra o placar atualizado
    print(t['placar'].format(vitorias_jogador, vitorias_pc))

    # Pergunta se quer continuar de forma segura
    while True:
        resp = input(t['continuar']).strip().upper()
        if resp and resp[0] in t['opcoes_cont']:
            break

    if resp[0] == 'N':
        break
    print("=-" * 25)

print(f"\n{t['tchau']}")
