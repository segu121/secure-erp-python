import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):

    letters_lower = random.choices(string.ascii_lowercase, k = number_of_small_letters)
    letters_upper = random.choices(string.ascii_uppercase, k = number_of_capital_letters)
    numbers = random.choices(string.digits, k = number_of_digits)
    special_char = random.choices(allowed_special_chars, k = number_of_special_chars)

    id_generator = letters_lower+letters_upper+numbers+special_char
    random.shuffle(id_generator)
    Id="".join(id_generator)
    return Id
 

                
     
