import jogo_da_forca
import Alura_Python
print("Escolha o seu jogo")
print("********************")
print('jogo de adivinhação (Item A)')
print('jogo da Forca(Item B)')
escolha= input('digite A ou B:')
item_a= 'A'
item_b= 'B'

if escolha == item_a:
    print("Jogando jogo de advinhação")
    Alura_Python.jogar()
elif escolha == item_b:
    print("Jogando jogo da forca")
    jogo_da_forca.jogar()