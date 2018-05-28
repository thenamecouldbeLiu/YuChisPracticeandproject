# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
def isWordGuessed(secretWord, lettersGuessed):
    global timeguessed
    if timeguessed<len(secretWord)+4:
        print("-"*10)
        inputletter = input('input your letter(one letter at a time): ')
        if inputletter not in getAvailableLetters(lettersGuessed):
            print("Oops, the letter is not available")
            isWordGuessed(secretWord, lettersGuessed)
        elif len(inputletter) >1:
            inputletter = input('one letter at a time!')
            isWordGuessed(secretWord, lettersGuessed)

        else:
            timeguessed += 1
            print('You have guessed', timeguessed, 'times.', "Got ", len(secretWord)+5 - timeguessed,'times left')
            inputletter= inputletter.lower()
            lettersGuessed.append(inputletter)
    else:
        print('You Failed')
        print('The word is', secretWord,'\n','-'*10)
        hangman(secretWord)
    '''以上為輸入條件判斷'''
    
    temp_letterGuessed = secretWord[:]
    for letter in lettersGuessed:
        while letter in temp_letterGuessed:
            temp_letterGuessed.remove(letter)
    print("You've guessed" , lettersGuessed)
    print("You've got ", getGuessedWord(secretWord, lettersGuessed))
    print("letters available:", getAvailableLetters(lettersGuessed))
    print("-"*10)
    while len(temp_letterGuessed) < 1:
        return True
    else:
        return False
        
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    i = 0
    temp= secretWord[:]
    
    while int(i) < len(temp):
        if temp[i] in lettersGuessed:
            Guessedword[i] =temp[i]
        i+=1
    return str(Guessedword)
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphalist = [chr(i) for i in range(97,123)]
    for letter in lettersGuessed:
        if letter in alphalist:
            alphalist.remove(letter)
    
    return "".join(alphalist)
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...    
    global timeguessed
    global lettersGuessed
    global Guessedword
    timeguessed = 0
    lettersGuessed = []
    Guessedword = list("_"*len(secretWord))
    print("Number of letters=", len(secretWord))
    while timeguessed<len(secretWord)+5:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('Yes!, you got it', "It's", "'",secretWord, "'")
            wordlist = loadWords()
            secretWord = list(chooseWord(wordlist))
            hangman(secretWord)
        else:
            isWordGuessed(secretWord, lettersGuessed)
wordlist = loadWords()
secretWord = list(chooseWord(wordlist))
Guessedword = list("_"*len(secretWord))
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
