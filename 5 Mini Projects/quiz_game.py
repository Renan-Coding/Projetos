print("Seja bem vindo ao meu quiz sobre computadores!")

playing = input("Você gostaria de jogar? ")

if playing.lower() != "sim":
    quit()

print("Ok! Vamos jogar! :)")
score = 0

answer = input("O que significa CPU? ").lower()
if answer == "unidade central de processamento":
    print("Correto! :) ")
    score += 1
else: 
    print("Errado! :( ")

answer = input("O que significa GPU? ").lower()
if answer == "unidade de processamento gráfico":
    print("Correto! :) ")
    score += 1
else: 
    print("Errado! :( ")

answer = input("O que significa RAM? ").lower()
if answer == "memória de acesso aleatório":
    print("Correto! :) ")
    score += 1
else: 
    print("Errado! :( ")

print("Você acertou " + str(score) + " questões!")