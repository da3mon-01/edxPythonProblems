import string

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    allLetters = string.ascii_lowercase

    for l in lettersGuessed:
          allLetters = allLetters.replace(l, '')

    return allLetters

print(getAvailableLetters(lettersGuessed))
