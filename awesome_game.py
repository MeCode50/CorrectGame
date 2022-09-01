import random 
user_score = 0
computer_score = 0
# list of options for the user to ick from
options = ['beans', 'bread', 'rice']
print()
while True:
    # user input, to know what the user would like to eat
    user_input = input('What would you like to eat ? Beans/Bread/Rice: or Q to quit:  ').lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue

 #  a variable (random_number) where beans is 0, bread is 1, rice is 2
    random_number = random.randint(0, 2)
# variable to know the computer's choice from the list of options
    computer_choice = options[random_number]
    print('computer picked', computer_choice + ".")

    if (user_input == 'beans') and (computer_choice == 'bread'):
        print('you won! ')
        user_score += 1
        

    elif user_input == 'rice' and computer_choice == 'bread':
        print('you won! ')
        user_score += 1
        

    elif user_input == 'bread' and computer_choice == 'rice':
        print('you won! ')
        user_score += 1
        
    else:
        print('you lost')
        computer_score +=1
print('you won', user_score , 'times')

print('computer won', computer_score ,'times.')

print('thanks for playing this game. ')




