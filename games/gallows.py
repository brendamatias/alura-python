import random

def play():
  prints_aperture()
  secret_word = get_secret_word()
  correct_letters = initializes_correct_letters(secret_word)
  print(correct_letters)

  hanged = False
  win = False
  attempts = 0

  while(not hanged and not win):
    kick = input("Qual letra?")
    kick = kick.strip().upper()
    index = 0

    if(kick in secret_word):
      for word in secret_word:
        if(kick == word):
          correct_letters[index] = word
        index += 1
    else:
      attempts += 1
      draw_fork(attempts)
    
    hanged = attempts == 7
    win = "_" not in correct_letters
    print(correct_letters)

  if(win):
    prints_winner_message()
  else:
    prints_loser_message(secret_word)

def prints_aperture():
  print('*********************************')
  print('***Bem vindo ao jogo de Forca!***')
  print('*********************************')

def get_secret_word():
  archive = open("words.txt", "r")
  words = []

  for row in archive:
    row = row.strip()
    words.append(row)

  archive.close()

  number = random.randrange(0, len(words))
  secret_word = words[number].upper()

  return secret_word

def initializes_correct_letters(secret_word):
  return ["_" for word in secret_word]

def prints_winner_message():
  print("Parabéns, você ganhou!")
  print("       ___________      ")
  print("      '._==_==_=_.'     ")
  print("      .-\\:      /-.    ")
  print("     | (|:.     |) |    ")
  print("      '-|:.     |-'     ")
  print("        \\::.    /      ")
  print("         '::. .'        ")
  print("           ) (          ")
  print("         _.' '._        ")
  print("        '-------'       ")

def prints_loser_message(secret_word):
  print("Puxa, você foi enforcado!")
  print("A palavra era {}".format(secret_word))
  print("    _______________         ")
  print("   /               \       ")
  print("  /                 \      ")
  print("//                   \/\  ")
  print("\|   XXXX     XXXX   | /   ")
  print(" |   XXXX     XXXX   |/     ")
  print(" |   XXX       XXX   |      ")
  print(" |                   |      ")
  print(" \__      XXX      __/     ")
  print("   |\     XXX     /|       ")
  print("   | |           | |        ")
  print("   | I I I I I I I |        ")
  print("   |  I I I I I I  |        ")
  print("   \_             _/       ")
  print("     \_         _/         ")
  print("       \_______/           ")

def draw_fork(errors):
  print("  _______     ")
  print(" |/      |    ")

  if(errors == 1):
      print(" |      (_)   ")
      print(" |            ")
      print(" |            ")
      print(" |            ")

  if(errors == 2):
      print(" |      (_)   ")
      print(" |      \     ")
      print(" |            ")
      print(" |            ")

  if(errors == 3):
      print(" |      (_)   ")
      print(" |      \|    ")
      print(" |            ")
      print(" |            ")

  if(errors == 4):
      print(" |      (_)   ")
      print(" |      \|/   ")
      print(" |            ")
      print(" |            ")

  if(errors == 5):
      print(" |      (_)   ")
      print(" |      \|/   ")
      print(" |       |    ")
      print(" |            ")

  if(errors == 6):
      print(" |      (_)   ")
      print(" |      \|/   ")
      print(" |       |    ")
      print(" |      /     ")

  if (errors == 7):
      print(" |      (_)   ")
      print(" |      \|/   ")
      print(" |       |    ")
      print(" |      / \   ")

  print(" |            ")
  print("_|___         ")
  print()

if(__name__ == "__main__"):
  play()