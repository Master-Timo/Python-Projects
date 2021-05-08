import string


def check_valid(user_pass, pass_length):

    if pass_length < 5:
        print("INVALID!! Password Too Short")

    elif pass_length > 20:
        print("INVALID!! Password Too Long. Enter a password between 6-20 characters")

    else:
        while user_pass:
            if user_pass[i] in string.printable:
                return True


# chars = string.digits + string.ascii_letters
# special_chars = "" .join(sp_char for sp_char in string.printable if sp_char not in chars)


special_chars = string.punctuation

# Taking a password from user to check its strength
user_input = input("Enter the Password to check strength of: ")
length = len(user_input)


# Declaring Flags
hasLower = False
hasUpper = False
hasDigit = False
hasSpecialChar = False


# for character in range(0, 256):
#     if chr(character) not in chars:
#         special_chars = special_chars+chr(character)

# print(chars)
# print(special_chars)

# print (string.printable)


for i in range(length):
    if user_input[i].islower():
        hasLower = True
    if user_input[i].isupper():
        hasUpper = True
    if user_input[i].isdigit():
        hasDigit = True
    if user_input[i] in special_chars:
        hasSpecialChar = True


check = check_valid(user_input, length)
print("Valid Password" if check == True else "Invalid")

# Strength of password
print("Strength of password:- ", end="")
if hasLower and hasUpper and hasDigit and hasSpecialChar and length >= 8:
    print("Strong")

elif (hasLower or hasUpper) and (hasSpecialChar and hasDigit) and length >= 6:
    print("Moderate")

else:
    print("Weak")


