secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    hiddenWord = secretWord
    for l in secretWord:
         if l not in lettersGuessed:
            hiddenWord =  hiddenWord.replace(l, '_ ')
    return hiddenWord


print(getGuessedWord(secretWord, lettersGuessed))
