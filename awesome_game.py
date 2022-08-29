import random 
user_score = 0
computer_score = 0
options = ['Rock', 'Paper', 'Scissors']

while True:
    user_input = input('Type Rock/ Paper / Scissors or Q to quit:  ').lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue


    random_number = random.randint(0, 2)
    # rock is 0, paper is 1, scissors is 2
    computer_choice = options[random_number]
    print('computer picked', computer_choice + ".")

    if (user_input == 'Rock') and (computer_choice == 'Scissors'):
        print('you won! ')
        user_score += 1
        

    elif user_input == 'Paper' and computer_choice == 'Rock':
        print('you won! ')
        user_score += 1
        

    elif user_input == 'Paper' and computer_choice == 'Scissors':
        print('you won! ')
        user_score += 1
        
    else:
        print('you lost')
        computer_score +=1
print('you won', user_score , 'times')

print('computer won', computer_score ,'times.')

print('thanks for playing this game. ')


