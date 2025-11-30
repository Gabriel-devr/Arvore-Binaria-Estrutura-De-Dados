class Node:
    def __init__(self,x):
        self.data=x
        self.parent=None
        self.left=None
        self.right=None
    
class Tree:
    def __init__(self):
        self.root=None
#========================================================================    
    #1) Primeiramente passei uma string como argumento do método, com ela fiz a instância do objeto usando esse argumento. Após inserir o primeiro nó na raiz, as variáveis auxiliares percorrem a arvore conforme as condicionais até então poder inserir o novo nó.
    def insertWord(self,word): #1 
        newNode=Node(word)
        if(self.root is None):
            self.root=newNode
            return f"palavra inserida: {word}"
        currentNode = self.root
        while(currentNode):
            parentTrackNode = currentNode
            if( word < parentTrackNode.data):
                currentNode = currentNode.left
                if(currentNode is None):
                    parentTrackNode.left = newNode
                    newNode.parent=parentTrackNode
                    return f"palavra inserida: {word}"   
            else:
                currentNode = currentNode.right 
                if(currentNode is None):
                    parentTrackNode.right = newNode
                    newNode.parent=parentTrackNode
                    return f"palavra inserida: {word}"
#========================================================================    
    #2) Ao criar variáveis que nos permitem verificar se existe ou não determinado dado, podemos então retornar essa mensagem no terminal.
    def consult(self,word):#2 
        trackNode = self.root
        while(trackNode):
            parentTrackNode = trackNode
            if (word < parentTrackNode.data):
                trackNode = trackNode.left
            elif(word>parentTrackNode.data):
                trackNode = trackNode.right
            else:
                return f"palavra existente: {word}"

        return f"palavra inexistente: {word}"
#========================================================================    
    #3) Aqui fazemos uma consulta, mas dessa vez ao percorrer contamos a quantidaade de vezes que determinado dado aparece na nossa árvore.
    def occurrence(self,word):#3
        trackNode = self.root
        counter = 0
        while(trackNode):
            parentTrackNode = trackNode
            if (word<parentTrackNode.data):
                trackNode = trackNode.left
            elif (word>=parentTrackNode.data):
                if (word == trackNode.data):
                    counter +=1
                trackNode = trackNode.right
        if (counter==0):
            print(f"palavra inexistente: {word}")
        else:
            print(f"palavra existente: {word} {counter}")
#========================================================================    
    #4) Para imprimir a nossa árvore com delimitadores e em ordem alfabetica optei por usar um método recursivo, assim me poupando linhas de código por meio de uma lógica baseada em stacks.
    def alphabeticalOrder(self,l1,l2):
        if (self.hasWords(self.root,l1,l2)):
            print(f'palavras em ordem:')
            self.orderedMargin(self.root,l1,l2)
        else:
            print('lista vazia')

    def hasWords(self, node, l1,l2):
        if (node is None):
            return False
        if (node.data[0] >= l1 and node.data[0] <=l2):
            return True
        return self.hasWords(node.left,l1,l2) or self.hasWords(node.right, l1,l2)
    
    def orderedMargin(self,currentNode,l1,l2): #Função auxiliar 4 
        if (currentNode is None):
            return 

        self.orderedMargin(currentNode.left,l1,l2)
        if(currentNode.data[0]>=l1 and currentNode.data[0]<=l2):
            print(currentNode.data)
        self.orderedMargin(currentNode.right,l1,l2)
#========================================================================
    #5) Bom seguindo a linha de raciocinio de remoção utilizando transplante. Primeiro precisamos verificar se o nó que queremos remover está dentro da arvore e a quantidade de filhos que ele tem. Temos 3 casos possíveis de remoção: o nó que queremos eliminar com nenhum, 1 ou 2 filhos. O caso mais complicado é o de 2 filhos onde temos que realizar o transplante do sucessor com o seu filho a direita e então acertar os ponteiros do sucessor e do seu filho conforme os ponteiros do no a ser eliminado.
    def search(self,x):
        trackNode = self.root
        while(trackNode):
            parentNode = trackNode
            if(x < parentNode.data):
                trackNode = trackNode.left
            elif(x > parentNode.data):
                trackNode = trackNode.right
            else:
                return trackNode

    def minimum(self,node):
        while(node.left):
            node = node.left
        return node

    def transplant(self,u,v):
        p = u.parent
        if(p is None):
            self.root = v
        elif (u==p.left):
            p.left = v
        else:
            p.right = v
        if (v is not None):
            v.parent = p
    
    def delete(self,z):
        node = self.search(z)
        if (node):
            if(node.left is None):
                self.transplant(node,node.right)
            elif (node.right is None):
                self.transplant(node,node.left)
            else:
                y = self.minimum(node.right)
                if(y != node.right):
                    self.transplant(y, y.right)
                    y.right = node.right
                    y.right.parent = y
                self.transplant(node, y)
                y.left = node.left
                y.left.parent = y
            print(f'palavra removida: {z}')
        else:
            print(f"palavra inexistente: {z}")
#========================================================================  
    #6) Optei por utilizar uma função recursiva para poder caminhar por toda a arvore, ou até o nível que foi escolhido, e ao final me retornar a soma recursiva dos lados, a quantidade de nos que está naquele nível. Além disso, preferi separar em 2 funções para melhor entendimento e para separar funções.   
    def countLevel(self,node,currentNode,meta): 
        if node is None:
            return 0
        if (currentNode == meta):
            return 1
        qtdEsquerda = self.countLevel(node.left, currentNode + 1, meta)
        qtdDireita = self.countLevel(node.right, currentNode + 1, meta)

        return qtdEsquerda + qtdDireita
    
    def printWordByLevel(self,node, currentNode, meta): 
        if node is None:
            return
        if (currentNode == meta):
            print(node.data)
        esquerda = self.printWordByLevel(node.left, currentNode + 1, meta)
        direita = self.printWordByLevel(node.right, currentNode + 1, meta)

#========================================================================    
    #7) A lógica foi dividida em duas partes para garantir a ordenação correta. Primeiro, eu verifico se a palavra existe na árvore. Se existir, imprimo o cabeçalho e chamo a função recursiva printPathSorted. Se o destino está à esquerda, eu visito a esquerda primeiro e só imprimo o nó atual na volta e faço o inverso caso contrário.
    def wordsOnTheWay(self,word):
        if not (self.search(word)):
            print(f'palavra inexistente: {word}')
            return
        print('palavras no caminho:')
        self.printPathSorted(self.root,word)
    
    def printPathSorted(self,node,meta):
        if not node:
            return
        if (meta<node.data):
            self.printPathSorted(node.left,meta)
            print(node.data)
        elif (meta>node.data):
            print(node.data)
            self.printPathSorted(node.right, meta)
        else:
            print(node.data)
#========================================================================    
    #8) Optei novamente por um método recursivo que irá iterar 1 a cada nível e ao final me retornar a altura exata da arvore
    def treeHeight(self,node):
        
        if node is None:
            return 0

        esquerda=self.treeHeight(node.left)
        direita=self.treeHeight(node.right)
            
        if (esquerda > direita):
            return 1 + esquerda
        else:
            return 1 + direita
#========================================================================    
    #9) Conforme foi proposto no item 9, foi necessário usar uma ordem de visita em pré-ordem, onde primeiro imprimo, visito recursivamente a esquerda e por último visito recursivamente a direita.
    def printTree(self,node): 
        if (node is None):
            if (node == self.root):
                print("arvore vazia")
            return
        
        if (node.left):
            palavraEsquerda = node.left.data
        else:
            palavraEsquerda = "nil"
        if (node.right):
            palavraDireita = node.right.data
        else:
            palavraDireita = "nil"

        print(f'palavra: {node.data} fesq: {palavraEsquerda} fdir: {palavraDireita}')

        self.printTree(node.left)
        self.printTree(node.right)