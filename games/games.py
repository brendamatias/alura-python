import gallows
import guessing

def choose_game():
  print("*********************************")
  print("*******Escolha o seu jogo!*******")
  print("*********************************")

  print("(1) Forca (2) Adivinhação")

  game = int(input("Qual jogo? "))

  if (game == 1):
    print("Jogando forca")
    gallows.play()
  elif (game == 2):
    print("Jogando adivinhação")
    guessing.play()

if (__name__ == "__main__"):
  choose_game()