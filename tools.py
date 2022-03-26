import utils
import random


# Have functions that run password gen


def password_gen_loop(amount_of_chars, type_of_chars):
    '''
    This function makes the random sequences
    :param amount_of_chars: how many characters need to be generated
    :param type_of_chars: the type of characters
    :return:
    '''

    password = []
    for character in range(amount_of_chars):
        password.append(random.choice(type_of_chars))

    return password



def gen_password(total_password_len, symbol_len, number_len):

    '''
    This function will generate the password and return it as a string
    :param total_password_len: What the total length of password should be
    :param symbol_len: how many symbols in password
    :param number_len: how many numbers in password
    :return:
    '''


    # Get the total amount of letters needed in password
    random_letter_len = total_password_len - (symbol_len + number_len)

    # create lists of all the passwords
    letters = password_gen_loop(random_letter_len, utils.letters)
    symbol = password_gen_loop(symbol_len, utils.symbols)
    numbers = password_gen_loop(number_len, utils.numbers)

    # add all the lists togather
    new_password = letters + symbol + numbers

    # Randomize the list
    random.shuffle(new_password)

    return "".join(new_password)