def main(): #main accepts no arguements
    #main should call all other functions to build the entire program
    pass

def get_shift():
    #accepts no arguements
    #get_shift should prompt the user for the shift value and return the value as a string
    #Validate for integers 1-25, inclusive.
    again = 'y'
    while again == 'y':
        try:
            shift = int(input('Enter a number 1-25 for your shift: '))
            if shift > 25 or shift < 1:
                print('Please enter a digit from 1-25\n')
                again = 'y'
            else:
                again = 'n'
        except:
            again = 'y'
            print('Please enter a digit from 1-25\n')
    return shift
def choose_option(): #choose option accepts no arguements
    #choose_option should prompt the user to choose to encode or decode.
    #It should return True if the user chooses encode and False
    #if the user chooses decode.
    #Validate to only accept the appropriate prompts for encode and decode.
    pass

def get_message():
    #get_message accepts no arguements
    #get_message should prompt the user to enter a message to encode or decode.
    #It should return that message
    print('Please input a message to encode or decode:')
    message = input()
    return message
def create_key(shift):
    #accepts 1 arguement of a shift dictionary
    #create_key should accept the shift value from get_shift.
    #It should create the caesar cipher according to the shift value
    #and store the key in a dictionary and return the dictionary as the key
    pass

def encode(message, key): #accepts message as a string and key as a dictionary
    #it should encode the message using the key and return the encoded message as a string
    pass

def decode(message, key):
    #decode accepts message as a string and key as a dictionary
    #it should decode the message using the key and return the decoded message as a string
    pass
