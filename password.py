import random
import string
def password_generator(numbers, symbols, lenght):

    characters = string.ascii_letters

    if numbers:
        characters = characters + string.digits


    if symbols:
        characters = characters + string.punctuation

    generator = random.choices(characters, k = lenght)

    generator = ''.join(generator)

    return generator
