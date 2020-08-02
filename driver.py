'''
Collaborators: Karime, Jaoudat, Ryan
               maamari@usc.edu, ...
'''

from getpass import getpass

def checkGuess(keyword, guess, output):
    for i, letter in enumerate(keyword):
        if letter is guess:
            output[i] = guess+' '
    return output

def updateHangman(count):
    hangman = [
	"""
	 ------
	|     |
	|     
	|  	 
	|     
	|     
	|
	----------
	"""
	,
	"""
	 ------
	|     |
	|     0
	|  	 
	|     
	|     
	|
	----------
	"""
	,
	"""
	 ------
	|     |
	|     0
	|    -+-
	|     
	|     
	|
	----------
	"""
	,
	"""
	 ------
	|     |
	|     0
	|    -+-
	|     |
	|     
	|
	----------
	"""
	,
	"""
	 ------
	|     |
	|     0
	|    -+-
	|     |
	|    / \\
	|
	----------
	"""
	]
    print(hangman[count])

def main():
    user1input = getpass("Welcome to Hangman!\nUser 1, please enter keyword: \n")
    output = ['_ ' for i in range(len(user1input))]
    
    tempOutput = ['_ ' for i in range(len(user1input))]
    wrongGuessCount=0
    while wrongGuessCount<4 and ('_ ' in output):
        user2input = input("User 2, please enter guess: ")
        
        output = checkGuess(user1input,user2input,output)
        print(''.join(output))
        
        if tempOutput==output:
            wrongGuessCount += 1
        else:
            tempOutput = output.copy()
        updateHangman(wrongGuessCount)

    if wrongGuessCount==4:
        print("You lose! Correct word was", user1input)
    else:
        print("Congratulations! Correct word was", user1input)

if __name__ == "__main__":
    main()
