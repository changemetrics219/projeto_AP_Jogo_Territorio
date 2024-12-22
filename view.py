#from controller import *
from jogadores import *

def main():
  print("********************* BEM-VINDO *********************")
  inicio()
    

def inicio():
  opcao = input("c - cadastrar jogador\ni - iniciar jogo\nx - sair\n>")
  match opcao:
    case "c":
      for i in range(4):
        nome = input("Nome do jogador: ")
        criar_jogador(nome)
      
    case "i":
      print("Boa sorte!")
    case "x":
      return False
    case _:
      print("opcao invalida")