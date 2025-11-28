from metodos import Tree

tree = Tree()
while True:
    command = input()
    if (command=='i'):
        word = input()
        print(tree.insertWord(word))
    if (command=='c'):
        word = input()
        print(tree.consult(word))
    if (command=='v'):
        word = input()
        tree.occurrence(word)
    if (command=='o'):
        l1=input()
        l2=input()
        tree.alphabeticalOrder(l1,l2)
    if (command=='r'):
        word = input()
        tree.delete(word)
    if (command=='n'):
        node = tree.root
        level = 1
        meta = int(input())
        count = tree.countLevel(node,level,meta)
        if (count>0):
            print(f'palavras no nivel: {meta}')
            tree.printWordByLevel(node,level,meta)
        else: 
            print(f'nao ha nos com nivel: {meta}')
    if(command=='t'):
        word = input()
        tree.wordsOnTheWay(word)
    if(command=='h'):
        node=tree.root
        print(f'altura da arvore: {tree.treeHeight(node)}')
    if(command=='p'):
        node=tree.root
        tree.printTree(node)
    if(command=='e'):
        break

