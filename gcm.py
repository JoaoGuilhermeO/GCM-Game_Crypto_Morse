import random
from tabulate import tabulate

# Tabela de código Morse
morse_code = {
    'A': '.-    ', 'B': '-...   ', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..    ', 'J': '.---   ', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-  ', 'R': '.-.    ', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--  ', 'Z': '--..   ', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '..... ', '6': '-....  ', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

#Função para mostrar o padrão ASCII do nome do jogo
def show_game_name():
    game_name_ascii = '''
   ggggggggg   ggggg         cccccccccccccccc        mmmmmmm    mmmmmmm
  g:::::::::ggg::::g       cc:::::::::::::::c      mm:::::::m  m:::::::mm
 g:::::::::::::::::g      c:::::::::::::::::c     m::::::::::mm::::::::::m
g::::::ggggg::::::gg     c:::::::cccccc:::::c     m::::::::::::::::::::::m
g:::::g     g:::::g      c::::::c     ccccccc     m:::::mmm::::::mmm:::::m
g:::::g     g:::::g      c:::::c                  m::::m   m::::m   m::::m
g:::::g     g:::::g      c:::::c                  m::::m   m::::m   m::::m
g::::::g    g:::::g      c::::::c     ccccccc     m::::m   m::::m   m::::m
g:::::::ggggg:::::g      c:::::::cccccc:::::c     m::::m   m::::m   m::::m
 g::::::::::::::::g       c:::::::::::::::::c     m::::m   m::::m   m::::m
  gg::::::::::::::g        cc:::::::::::::::c     m::::m   m::::m   m::::m
    gggggggg::::::g          cccccccccccccccc     mmmmmm   mmmmmm   mmmmmm
            g:::::g
gggggg      g:::::g
g:::::gg   gg:::::g
 g::::::ggg:::::::g
  gg:::::::::::::g
    ggg::::::ggg
       gggggg
'''
    game_name_text = "  GAME                  CRYPTO                         MORSE"

    print(game_name_ascii)
    print(game_name_text)

    print("=============================================================================")
    print("=============================================================================")
from tabulate import tabulate

# Tabela de código Morse
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

# Função para exibir a tabela de código Morse em três colunas
def show_morse_table():
    table_data = list(morse_code.items())
    num_rows = len(table_data)
    num_columns = 8

    # Calcular o número de linhas necessário
    num_rows_per_column = (num_rows + num_columns - 1) // num_columns

    # Criar as colunas
    columns = [table_data[i:i+num_rows_per_column] for i in range(0, num_rows, num_rows_per_column)]

    # Imprimir as colunas lado a lado
    for i in range(num_rows_per_column):
        row = ""
        for column in columns:
            if i < len(column):
                row += f"{column[i][0]}: {column[i][1]}\t"
        print(row)



# Função para obter a resposta correta para um código Morse
def get_correct_answer(question, answer):
    if question in morse_code:
        return morse_code[question]
    for letter, morse in morse_code.items():
        if morse == answer:
            return letter
    for letter, morse in morse_code.items():
        if morse == question:
            return letter
    return None

# Função principal do jogo
def morse_game():
    show_game_name()
    show_morse_table()

    try:
        player_name = input("Digite o nome do jogador: ")
    except KeyboardInterrupt:
        print("\nJogo interrompido. Obrigado por jogar!")
        return

    score = 0

    while score < 100:
        # Selecionar aleatoriamente uma letra ou código Morse
        question_type = random.choice(['letter', 'morse'])
        if question_type == 'letter':
            question = random.choice(list(morse_code.keys()))
            correct_answer = morse_code[question]
            user_answer = input(f"Qual é o código Morse para a letra '{question}'? ")
        else:
            question = random.choice(list(morse_code.values()))
            correct_answer = get_correct_answer(question, '')
            user_answer = input(f"Qual é a letra correspondente ao código Morse '{question}'? ")

        if user_answer.upper() == correct_answer:
            score += 10
            print("Resposta correta!")
        else:
            print("Resposta incorreta!")
            print(f"A resposta correta é: {correct_answer}")

        print(f"Pontuação atual: {score}\n")

    print(f"Parabéns, {player_name}! Você alcançou 100 pontos e venceu o jogo!")

# Executar o jogo
morse_game()
