import string
import random

def generador_contraseñas(caracteres):
    characters = list(string.ascii_letters)
    numbers = list(string.digits)
    special_characters=list("!@#$%^&*_-=&/?¡¿}+´¨{[~^+()")
    characters_lower_count=1
    characters_capitalize_count=1
    numbers_count=1
    special_characters_count=1
    password = []
    contraseña=""
    for a in range(caracteres):
        
        for x in range(characters_lower_count):
            password +=random.choice(characters).lower()
        for a in range(characters_capitalize_count):
            password +=random.choice(characters).capitalize()
        for y in range(numbers_count):
            password +=random.choice(numbers)
        for z in range(special_characters_count):
            password +=random.choice(special_characters)
        for i in range(caracteres):
            password +=(random.choice(random.choice(characters).lower()+
            random.choice(characters).capitalize() + 
            random.choice(numbers) +
            random.choice(special_characters)))
        random.shuffle(password)
        contraseña = ("".join(password))
        return contraseña

if __name__ == '__main__':
    caracteres=int(input("Elija la cantidad de caracteres para su contraseña (minimo 4): "))-4
    print(generador_contraseñas(caracteres))

