'''
Collaborators: Karime, Jaoudat, Ryan
               maamari@usc.edu, ...
'''

from getpass import getpass

def main():
    user1input = getpass("Welcome to Hangman!\nUser 1, please enter keyword: ")
    num_underscore = len(user1input)
    
    for i in num_underscore:
        print('_ ', end='')
    print('')
    user2input = input("User2, please enter guess: ")


if __name__ == "__main__":
    main()
