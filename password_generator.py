import random
import string


# function for generating the random password for the give length of string
def generate_password(length):
    characters = string.ascii_letters + string.digits  # taking letters, digits
    password = ""  # initializing password with empty
    
    # creating password with for loop under the specified length
    for index in range(length):
        password = password + random.choice(characters)

    return password


# for the length of the password from the user
password_length = int(input("Enter the length of the password: "))
random_password = generate_password(password_length)
print("Random Password:",random_password)


