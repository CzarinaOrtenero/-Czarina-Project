#EXERCISE 9 BINARY TREE
#CZARINA J. ORTENERO

class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid

    def getLeftStudent(self):
        return self.left
    def getRightStudent(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.left = self.left
            self.left = tree


    def printTree(tree):
        if tree != None:
            printTree(tree.getLeftStudent())
            print(tree.getNodeValue())
            printTree(tree.getRightStudent())


        if _name_ == "_main_":
            myTree = BinaryTree("YNA")
            myTree.insertLeft("SHIELA")
            myTree.insertRight("MADEL")
            myTree.insertRight("AUBREY")
            myTree.insertLeft("PAOLO")
            myTree.insertLeft("JUAN")
            myTree.insertLeft("MAE")
            myTree.setNodeValue("MIG")
    

            print myTree.getNodeValue()
            print Tree(myTree)
