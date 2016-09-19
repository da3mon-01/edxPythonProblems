secretWord = 'apple'
lettersGuessed = ['e', 'a', 'l', 'p', 'r', 's']

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    isGuessed = False
    correctLetters = 0
    for l in secretWord:
          if l in lettersGuessed:
               correctLetters += 1
    if correctLetters == len(secretWord):
        return True
    else:
        return False



print(isWordGuessed(secretWord, lettersGuessed))
