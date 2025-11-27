class Node:
    def __init__(self,x):
        self.data=x
        self.parent=None
        self.left=None
        self.right=None
    
class Tree:
    def __init__(self):
        self.root=None

    def insere_palavra(self,x): #1 QUESTÃO OK com printa fora da funcao
        newNode=Node(x)
        if(self.root is None):
            self.root=newNode
            return f"Palavra inserida: {x}"
        currentNode = self.root
        while(currentNode):
            parentTrackNode = currentNode
            if( x < parentTrackNode.data):
                currentNode = currentNode.left
                if(currentNode is None):
                    parentTrackNode.left = newNode
                    newNode.parent=parentTrackNode
                    return f"Palavra inserida {x}"
                    
            else:
                currentNode = currentNode.right 
                if(currentNode is None):
                    parentTrackNode.right = newNode
                    newNode.parent=parentTrackNode
                    return f"Palavra inserida {x}"
                    
                
    def consulta(self,x):#2 QUESTÃO OK com print fora da funcao
        trackNode = self.root
        while(trackNode):
            parentTrackNode = trackNode
            if (x < parentTrackNode.data):
                trackNode = trackNode.left
            elif(x>parentTrackNode.data):
                trackNode = trackNode.right
            else:
                return "Palavra existente"

        return f"Palavra Inexistente {x}"
    
    def ocorrencia(self,x): #3 QUESTÃO OK com print fora da funcao
        trackNode = self.root
        counter = 0
        while(trackNode):
            parentTrackNode = trackNode
            if (x<parentTrackNode.data):
                trackNode = trackNode.left
            elif (x>=parentTrackNode.data):
                if (x == trackNode.data):
                    counter +=1
                trackNode = trackNode.right
        if (counter==0):
            return f"Palavra inexistente: {x}"
        else:
            return f"Palavra existente: {x} {counter}"
        
#------------------------------------------------------------
    def ordemAlfabetica(self,l1,l2): #4 QUESTÃO OK com print dentro da funcao
        noAtual=self.root
        if (noAtual):
            self.ordenada(noAtual) 
            print('------------------------------')
            self.ordenadaMargem(noAtual,l1,l2)
        else:
            print('lista vazia')

    def ordenada(self,noAtual): #Função auxiliar 4
        if(noAtual):
            self.ordenada(noAtual.left)
            print(noAtual.data)
            self.ordenada(noAtual.right)
    
    def ordenadaMargem(self,noAtual,l1,l2): #Função auxiliar 4 
        if (noAtual is None):
            return 

        self.ordenadaMargem(noAtual.left,l1,l2)
        if(noAtual.data[0]>=l1 and noAtual.data[0]<=l2):
            print(noAtual.data)
        self.ordenadaMargem(noAtual.right,l1,l2)
         
#------------------------------------------------------------

    def contarNivel(self,No,NivelAtual,NivelMeta): #QUESTÃO 6 OK PRINT FORA
        if No is None:
            return 0
        if (NivelAtual == NivelMeta):
            return 1
        qtdEsquerda = self.contarNivel(No.left, NivelAtual + 1, NivelMeta)
        qtdDireita = self.contarNivel(No.right, NivelAtual + 1, NivelMeta)

        return qtdEsquerda + qtdDireita
    
    def imprimePalavrasPorNivel(self,No, NivelAtual, NivelMeta): #QUESTÃO 6 OK COM PRINT DENTRO
        if No is None:
            return
        if (NivelAtual == NivelMeta):
            print(No.data)
        esquerda = self.imprimePalavrasPorNivel(No.left, NivelAtual + 1, NivelMeta)
        direita = self.imprimePalavrasPorNivel(No.right, NivelAtual + 1, NivelMeta)

#---------------------------------------------------------------

    def palavrasNoCaminho(self,No): # QUESTÃO 7 OK PRINT NA FUNCAO

        currentNode = self.root
        while(currentNode):
            parentNode = currentNode
            if(No.data < parentNode.data):
                currentNode = currentNode.left
            elif(No.data>parentNode.data):
                currentNode = currentNode.right
            else:
                print('palavras no caminho:')
                currentNode = self.root
                while(currentNode):
                    parentNode = currentNode
                    print(parentNode.data)
                    if(No.data < parentNode.data):
                        currentNode = currentNode.left
                    elif (No.data > parentNode.data):
                        currentNode = currentNode.right
                    else:
                        return

        return print(f"palavra inexistente: {No.data}")      
      
#----------------------------------------------------------------

    def alturaDaArvore(self): # QUESTÃO 8 OK PRINT FORA DA FUNCAO
        
        if self.root is None:
            return 0

        esquerda=self.alturaDaArvore(self.root.left)
        direita=self.alturaDaArvore(self.root.right)
            
        if (esquerda > direita):
            return 1 + esquerda
        else:
            return 1 + direita
        
#------------------------------------------------------------------

    def imprimeArvore(self,No): #QUESTÃO 9 OK PRINT DENTRO
        if (No is None):
            if (No == self.root):
                print("arvore vazia")
            return
        
        if (No.left):
            palavraEsquerda = No.left.data
        else:
            palavraEsquerda = "nil"
        if (No.right):
            palavraDireita = No.right.data
        else:
            palavraDireita = "nil"

        print(f'palavra {No.data} fesq: {palavraEsquerda} fdir: {palavraDireita}')

        self.imprimeArvore(No.left)
        self.imprimeArvore(No.right)
        
        
arvore = Tree()

# array=['b','a','c','d','a','a']
# for i in array:
#     print(arvore.insere_palavra(i))
# print('------------------------------')

# # print(arvore.consulta("2"))
# # print('------------------------------')

# # print(arvore.ocorrencia("carlos"))
# # print('------------------------------')
# # arvore.ordemAlfabetica('b','c')
# # print("------------------------------")
# novoNo= Node("c")
# NoRaiz = arvore.root
# arvore.palavrasNoCaminho(novoNo)
# print(arvore.alturaDaArvore(arvore.root))
# arvore.imprimeArvore(NoRaiz)

while True:
    comando = input("Digite um comando: ")
    if (comando=='i'):
        palavraInserida = input("Palavra a ser inserida: ")
        print(arvore.insere_palavra(palavraInserida))
    if (comando=='c'):
        consultaPalavra = input("Consulte uma palavra: ")
        print(arvore.consulta(consultaPalavra))
    if (comando=='v'):
        ocorrenciaPalavra = input("ocorrencia da palavra: ")
        print(arvore.ocorrencia(ocorrenciaPalavra))
    if (comando=='o'):
        l1=input("letra 1")
        l2=input('letra 2')
        arvore.ordemAlfabetica(l1,l2)
    if (comando=='n'):
        nivelMeta = int(input("escolha um nivel"))
        No = arvore.root
        print(f'palavras no nivel: {arvore.contarNivel(No,1,nivelMeta)}')
        arvore.imprimePalavrasPorNivel(No,1, nivelMeta)
    if (comando=='h'):
        print(arvore.alturaDaArvore())
        

        