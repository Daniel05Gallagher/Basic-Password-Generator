import string, secrets

# Password generate function
def password_generate(length: int, uppercase: bool, symbols: bool):
    combination = string.ascii_lowercase + string.digits
    
    # If statements to determine if uppercase and symbol characters are to be included
    if uppercase == True:
        combination += string.ascii_uppercase
    if symbols == True:
        combination += string.punctuation
        
    password = " "
    combination_length = len(combination)
    
    # for loop to generate the password
    for _ in range(length):
        password += combination[secrets.randbelow(combination_length)]     
    
    return password

print("--- Welcome to the password generation tool ---")
print()
lengthIn = int(input("How many characters long do you want your password?: "))
uppercaseIn = input("Do you wish uppercase characters to be included? [True] or [False]: ").lower()
symbolsIn = input("Do you wish symbols characters to be included? [True] or [False]: ").lower()
passwordQauntity = int(input("How many passwords do you want generated?: "))
print()

# If statement to deterime if uppercase characters are to be included or not
uppercaseInBool = False
if uppercaseIn == "true":
    uppercaseInBool = True
if uppercaseIn == "false":
    uppercaseInBool = False

# If statement to deterime if symbols are to be included or not
symbolsInBool = False
if symbolsIn == "true":
    symbolsInBool = True
if symbolsIn == "false":
    symbolsInBool = False

i=1
# While loop to print the correct number of passwords specified by the user
while i <= passwordQauntity:
    print(password_generate(lengthIn, uppercaseInBool, symbolsInBool))
    i = i+1