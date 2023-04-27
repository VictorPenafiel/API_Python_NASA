""" def validate(options, choice):
    if choice in options:
        print(f'You chose option {choice}.')
    else:
        print('Invalid option. Please try again.')

if __name__ == '__main__':
    options = ['1', '2', '3']
    choice = input('Choose an option: ')
    validate(options, choice) """