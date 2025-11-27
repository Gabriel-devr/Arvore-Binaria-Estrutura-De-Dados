class Node:
    def __init__(self,x):
        self.data=x
        self.parent=None
        self.left=None
        self.right=None
    
class Tree:
    def __init__(self):
        self.root=None

    def insere_palavra(self): #1 QUESTÃO OK com printa fora da funcao
        word = input()
        newNode=Node(word)
        if(self.root is None):
            self.root=newNode
            return f"Palavra inserida: {word}"
        currentNode = self.root
        while(currentNode):
            parentTrackNode = currentNode
            if( word < parentTrackNode.data):
                currentNode = currentNode.left
                if(currentNode is None):
                    parentTrackNode.left = newNode
                    newNode.parent=parentTrackNode
                    return f"Palavra inserida {word}"
                    
            else:
                currentNode = currentNode.right 
                if(currentNode is None):
                    parentTrackNode.right = newNode
                    newNode.parent=parentTrackNode
                    return f"Palavra inserida {word}"
    
    def consulta(self):#2 QUESTÃO OK com print fora da funcao
        word = input()
        trackNode = self.root
        while(trackNode):
            parentTrackNode = trackNode
            if (word < parentTrackNode.data):
                trackNode = trackNode.left
            elif(word>parentTrackNode.data):
                trackNode = trackNode.right
            else:
                return "Palavra existente"

        return f"Palavra Inexistente {word}"