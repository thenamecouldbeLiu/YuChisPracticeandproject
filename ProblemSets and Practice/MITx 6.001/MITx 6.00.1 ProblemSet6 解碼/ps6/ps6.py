import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        lowerkey = list(string.ascii_lowercase)   
        upperkey = list(string.ascii_uppercase)
        lowervalue = list(string.ascii_lowercase)
        uppervalue = list(string.ascii_uppercase)
        l = lowerkey[:]
        u = upperkey[:]
        shift= shift % 26
        if shift <0:
            shift = shift +26
        i = 0
        while i<26:
            if i + shift<26:
                lowervalue[i] = l[i+shift]
                uppervalue[i] = u[i+ shift]
                i+=1
            else:
                lowervalue[i] = l[i+shift-26]
                uppervalue[i] = u[i+ shift-26]
                i+=1
        shifted_dict =dict( dict(zip(lowerkey,lowervalue)),**dict(zip(upperkey,uppervalue)))
        return shifted_dict
    
    def apply_shift(self, shift):
        shifted = Message.build_shift_dict(self,shift)
        copymsg = self.message_text[:]
        copymsg= list(copymsg)
        index = 0
        while index< len(copymsg):
            if copymsg[index].isalpha():
                copymsg[index] = shifted[copymsg[index]]
                index +=1
            else:
                index +=1
                continue
        return "".join(copymsg)
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        Message.__init__(self, text)
        self.shift= shift
        self.encrypting_dict = PlaintextMessage.build_shift_dict(self, self.shift)
        self.message_text_encrypted = PlaintextMessage.apply_shift(self, self.shift)
        

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        self.encrypted_dict_copy = (Message.build_shift_dict(self, self.shift)).copy()
        
        return self.encrypted_dict_copy

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        new_texttext_encrypted = PlaintextMessage.apply_shift(self, self.shift)
        return new_texttext_encrypted

    def change_shift(self, changed_shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        changed_shift = changed_shift%26
        
        self.shift = changed_shift


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):

        self.decrypted_list = []
        best_Value =0
        best_word = None
        best_counter = 0
        index = 0
        for shift in range(26):    
            self.decrypted_list.append(self.apply_shift(shift))
        while index< len(self.decrypted_list):
            self.decrypted_list[index] = (self.decrypted_list[index].split(" "))
            index+=1
        for s in self.decrypted_list:
            counter = 0
            for i in s:
                if is_word(load_words('words.txt'), i):
                    counter =counter+1
            if counter>best_counter:
                best_counter = counter
                best_word = s
                best_Value = self.decrypted_list.index(s)
        return (best_Value, " ".join(best_word))
    
#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage(get_story_string())
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())
