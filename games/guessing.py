import random

def play():
  print('*********************************')
  print('Bem vindo ao jogo de Adivinhação!')
  print('*********************************')

  number_secret = random.randrange(1, 101)
  total_attempts = 5
  round = 1
  scored = 1000

  print("Qual nível de dificuldade?")
  print("(1) Fácil (2) Médio (3) Díficil")

  level = int(input("Define o nível: "))

  if(level == 1):
    total_attempts = 20
  elif(level == 2):
    total_attempts = 10

  while(round <= total_attempts):
    print("Tentativa {} de {}".format(round, total_attempts))
    kick_str = input("Digite um número entre 1 e 100: ")
    kick = int(kick_str)

    if(kick < 1 or kick > 100):
      print("Você deve digitar um número entre 1 e 100!")
      continue

    print("Você digitou ", kick)

    if(number_secret == kick):
      print("Você acertou e fez {} pontos!".format(scored))
      break
    else:
      if(kick > number_secret):
        print("Você errou! O seu chute foi maior do que o número secreto.")
      else:
        print("Você errou! O seu chute foi menor do que o número secreto.")

      lost_points = abs(number_secret - kick)
      scored = scored - lost_points

    round += 1
  print("Fim de jogo")

if(__name__ == "__main__"):
  play()