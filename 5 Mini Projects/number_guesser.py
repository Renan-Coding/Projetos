import random

top_of_range = input("Digite um número: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Por favor digite um número maior que 0.")
        quit()
else:
    print("Por favor digite um número.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Adivinhe: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Por favor digite um número.")
        continue

    if user_guess == random_number:
        print("Você acertou!")
        break
    elif user_guess > random_number:
        print("Você ficou acima do número!")
    else:
        print("Você ficou abaixo do número!")

print("Você acertou em", guesses, "tentativas") 