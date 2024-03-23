# write 'hello world' to the console
#print('hello world')

# create a function that randomly selects an element from the array
# Path: app.py
""" import random
choices = ['rock', 'paper', 'scissors']

def computer_choice():
    return random.choice(choices)
print(computer_choice())
 """
#create app game rock, paper, scissors
# Path: app.py
import random
choices = ['rock', 'paper', 'scissors']
# declare variables for user and computer puntos
qty_rounds = 0
user_puntos = 0
computer_puntos = 0
empates = 0


# create a function that randomly selects an element from the array
def computer_choice():
    return random.choice(choices)

# create a function that determines the winner
def determine_winner(user_choice, computer_choice):
    global user_puntos
    global computer_puntos
    global qty_rounds
    global empates
    qty_rounds += 1
    if user_choice == computer_choice:
        empates += 1
        return 'Empataron!'
    if user_choice == 'rock' and computer_choice == 'scissors':
        user_puntos += 1
        return 'User Winner!'
    if user_choice == 'paper' and computer_choice == 'rock':
        user_puntos += 1
        return 'User Winner!'
    if user_choice == 'scissors' and computer_choice == 'paper':
        user_puntos += 1
        return 'User Winner!'
    computer_puntos += 1
    return 'Computer Winners!'

# create function validate input user
def validate_input(user_choice):
    if user_choice not in choices:
        return False
    return True


# create a function that evalue if the user wants to continue playing
def continuar_jugando():
    continuar = input('Desea continuar jugando? (y/n): ')
    if continuar == 'y':
        return True
    else:
        #imprimir puntos
        print('*******************')
        print('***Fin del juego***')
        print(f'Cantidad de rondas: {qty_rounds}')
        print(f'User puntos: {user_puntos}')
        print(f'Computer puntos: {computer_puntos}')
        print(f'Empates: {empates}')
        print('*******************')
        return False

# create a function that runs the game
def run_game():
    continuar_bol = True
    while continuar_bol:
        print('*******************')
        user_choice = input('Enter rock, paper, or scissors: ')
        validate = validate_input(user_choice)
        if not validate:
            print('Invalid input')
            """ print('*******************')
            continuar = input('Desea continuar jugando? (y/n): ')
            if continuar == 'y':
                run_game()
            else:
                #imprimir puntos
                print('*******************')
                print('***Fin del juego***')
                print(f'User puntos: {user_puntos}')
                print(f'Computer puntos: {computer_puntos}')
                print('*******************')
                return  """
        else:
            computer = computer_choice()
            print(f'Computer chose {computer}')
            print(determine_winner(user_choice, computer))
        continuar_bol = continuar_jugando()
run_game()
