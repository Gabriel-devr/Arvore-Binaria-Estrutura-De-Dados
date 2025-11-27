from metodos.py import Node, Tree

while True:
    comando = input("Digite um comando: ")
    if (comando=='i'):
        palavraInserida = input("Palavra a ser inserida: ")
        print(arvore.insere_palavra(palavraInserida))