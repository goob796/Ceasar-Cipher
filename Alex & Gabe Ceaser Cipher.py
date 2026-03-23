QUIT = 3
import string

def main(): #main accepts no arguements
    #it prompts the user with the menu
    # and calls the function based on the input
    
    #intilize choice, key as a dictionary, and message as a string
    choice = 0
    shift = 0
    message = ""
        
    while choice != QUIT:
        #get the shift number, message, and create the dicitonary for the shift
        shift = get_shift()
        message = get_message()
        create_key(shift)
        choice = choose_option()
        
        if choice == 1:
            print(encode(message, shift))
        elif choice == 2:
            print(decode(message, shift))
        elif choice == 3:
            break
        else:
            print("Invalid Menu Option Selected.")
        
        #ask user if they want to return to the menu
        again = input("Enter 'q' to quit or any other key to return to menu: ")
        
        if again.lower() == 'q':
            break  # exit loop
            
    print()
    print("Thank you for using the Menu")

def get_shift():
    #accepts no arguements
    #get_shift should prompt the user for the shift value and return the value as a string
    #Validate for integers 1-25, inclusive.
    
    #initlize again
    again = 'y'
    
    #loop for getting the number in the shift and validate input
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
    #Validate to only accept the appropriate prompts for encode and decode.
    
    choice = 0
    
    #get input from the user for the menu choice
    try:
        #validate input
        while choice < 1 or choice > 3: 
            print()
            choice = int(input("Enter 1 to encode, 2 to decode, 3 to quit: "))
            
    except Exception as err:
        print(f"\nError: Only enter number 1-3.")
    return choice
    

def get_message():
    #get_message accepts no arguements
    #get_message should prompt the user to enter a message to encode or decode.
    #it should return that message
    print('Please input a message to encode or decode:')
    message = input()
    return message


def create_key(shift):
    #accepts 1 arguement of a shift dictionary
    #create_key should accept the shift value from get_shift.
    #It should create the caesar cipher according to the shift value
    #and store the key in a dictionary and return the dictionary as the key
    
    alphabet = string.ascii_uppercase #initlize alphabet
    
    #create the key based on the shift
    key = alphabet[shift+1:]+alphabet[:shift+1]
    
    return key


def encode(message, shift): #accepts message as a string and shift as a number
    #it should encode the message using the shift and return the encoded message as a string
    result = ''
    
    for char in message:
        if char.isalpha(): #only shift letters
            
            #convert the letter to num
            num = ord(char)
            
            #add the shift to move the letter forward
            num = num + shift
            
            #if its an uppercase letter and goes past Z
            if char.isupper() and num > ord('Z'):
                #wrap it around the alphabet
                num = num - 26
                
            #if its a lowercase letter and goes past 'z'
            elif char.islower() and num > ord('z'):
                num = num - 26
                
            #convert the number back to a letter
            new_char = chr(num)
            result += new_char
            
        else:
            #if it's not a letter keep the same
            result += char
        
    #return the message
    return result
        

def decode(message, shift):
    #decode accepts message as a string and shift as a number
    #it should decode the message using the shift and return the decoded message as a string
    
    #reuse encode but a negative shift
    return encode(message, -shift)


