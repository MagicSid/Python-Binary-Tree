class BinaryTree():
    """
    A class to implement a binary tree node and by extension a full binary tree

    Attributes
    ----------
    left - the child node to the left of the current node - data is less than parent
    right - the child node to the right of the current node - data is greater than parent
    data - the value of the current node

    Methods
    -------
    findMax - finds max value in the tree
    findVal - finds a value in the tree and returns true/false based on result
    binarySearch - performs a binary search to look for a value - same purpose as findVal
    printAll - prints all values in the binary tree using a breadth first method
    insert - inserts a new data point into the tree as a new node.
    inOrder - returns an array with the tree in inorder
    preOrder - same as inorder except array is in preorder
    postOrder - same as inorder except array is in postorder
    """

    def __init__(self,data,left,right):
        self.left = left
        self.right = right
        dataPoints = [data]
        leftExists = False
        if left != None:
            leftExists = True
            dataPoints.append(left.data)
        if right != None:
            dataPoints.append(right.data)
        dataPoints.sort()
        if len(dataPoints) not in [1,2,3]:
            raise Exception("Missing Parameter")
        elif len(dataPoints) == 1:
            self.data = data
        elif len(dataPoints) == 2:
            if leftExists:
                self.left.data = dataPoints[0]
                self.data = dataPoints[1]
            else:
                self.data = dataPoints[0]
                self.right.data = datapoints[1]
        else:
            self.left.data = dataPoints[0]
            self.data = dataPoints[1]
            self.right.data = dataPoints[2]

    def findMax(self):
        currentMax = 0
        if self.left != None:
            val = self.left.findMax()
            if val > currentMax:
                currentMax = val
        if self.right != None:
            val = self.right.findMax()
            if val > currentMax:
                currentMax = val
        if self.data > currentMax:
            return self.data
        else:
            return currentMax

    def findVal(self,val):
        if self.data == val:
            return True
        if self.left != None:
            if self.left.findVal(val):
                return True
        if self.right != None:
            if self.right.findVal(val):
                return True
        return False

    def binarySearch(self,val):
        if val == self.data:
            return True
        elif val < self.data and self.left != None:
            return self.left.binarySearch(val)
        elif val > self.data and self.right != None:
            return self.right.binarySearch(val)
        else:
            return False

    def printAll(self):
        nodes = [self]
        while len(nodes) > 0:
            print(nodes[0].data)
            if nodes[0].left != None:
                nodes.append(nodes[0].left)
            if nodes[0].right != None:
                nodes.append(nodes[0].right)
            del nodes[0]
                
        
    def insert(self, item):
        if item > self.data:
            if self.right != None:
                self.right.insert(item)
            else:
                self.right = BinaryTree(item,None,None)
        else:
            if self.left != None:
                self.left.insert(item)
            else:
                self.left = BinaryTree(item,None,None)

    def inOrder(self):
        nodes = [self]
        count = 0
        while len(nodes) > count:
            if isinstance(nodes[count],int):
                count += 1
            else:
                toAdd = []
                current = nodes[count]
                if current.left != None:
                    toAdd.insert(0,current.left)
                toAdd.insert(0,current.data)
                if current.right != None:
                    toAdd.insert(0,current.right)
                
                for item in toAdd:
                    nodes.insert(count,item)
                del nodes[count+len(toAdd)]
            
        return nodes

    def preOrder(self):
        nodes = [self]
        count = 0
        while len(nodes) > count:
            if isinstance(nodes[count],int):
                count += 1
            else:
                toAdd = []
                current = nodes[count]
                toAdd.insert(0,current.data)
                if current.left != None:
                    toAdd.insert(0,current.left)
                if current.right != None:
                    toAdd.insert(0,current.right)
                
                for item in toAdd:
                    nodes.insert(count,item)
                del nodes[count+len(toAdd)]
            
        return nodes

    def postOrder(self):
        nodes = [self]
        count = 0
        while len(nodes) > count:
            if isinstance(nodes[count],int):
                count += 1
            else:
                toAdd = []
                current = nodes[count]
                if current.left != None:
                    toAdd.insert(0,current.left)
                if current.right != None:
                    toAdd.insert(0,current.right)
                toAdd.insert(0,current.data)
                
                for item in toAdd:
                    nodes.insert(count,item)
                del nodes[count+len(toAdd)]
            
        return nodes
    

leafOne = BinaryTree(2,None,None)
leafTwo = BinaryTree(4,None,None)
leafThree = BinaryTree(6,None,None)
leafFour = BinaryTree(8,None,None)
middleOne = BinaryTree(10,leafOne,leafTwo)
middleTwo = BinaryTree(12,leafThree,leafFour)
root = BinaryTree(14,middleOne,middleTwo)

root.printAll()
print("")
print(root.postOrder())
