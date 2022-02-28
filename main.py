import random
import timeit
class sortSystem:
    def __init__(self):
        self.sortList = []
        self.length = 0
    def genList(self, length):
        self.sortList = list(range(0, length))
        for i in range(length):
            rand = random.randint(0, length-1)
            self.sortList[i], self.sortList[rand] = self.sortList[rand], self.sortList[i]
        self.length = len(self.sortList)
        print("finished")
    def selSort(self):
        list = self.sortList.copy()
        for i in range(self.length):
            holder = list[i]
            hPos = i
            for x in range(i+1, self.length):
                if holder > list[x]:
                    holder = list[x]
                    hPos = x
            list[hPos], list[i] = list[i], list[hPos]
        return list
    def inSort(self):
        list = self.sortList.copy()
        for i in range(1, self.length):
            holder = list[i]
            for x in range(0, i):
                if list[x] > holder:
                    list[i], list[x] = list[x], list[i]
                    break
        return list
    def bubSort(self):
        measure = 0
        list = self.sortList.copy()

        while measure < self.length-1:
           measure = 0
           for i in range(self.length-1):
               if list[i] > list[i+1]:
                   list[i], list[i+1] = list[i+1], list[i]
               else:
                   measure = measure + 1
        return list
class MergSort:
    def __init__(self):
        self.list = []
    def genList(self, length):
        List = list(range(0, length))
        for i in range(length):
            rand = random.randint(0, length-1)
            List[i], List[rand] = List[rand], List[i]
        self.list = List
        return List
    def MergSortFunc(self):
        self.splitFunction(self.list)
    def splitFunction(self, list):
        leftBranch = []
        rightBranch = []
        ComBran = []
        for i in range(int(len(list)/2)):
            leftBranch.append(list[i])
        for i in range(int(len(list)/2), len(list)):
            rightBranch.append(list[i])
        if len(leftBranch) == 1 and len(rightBranch) == 1:
            if leftBranch[0] < rightBranch[0]:
                leftBranch.append(rightBranch[0])
                return leftBranch
            else:
                rightBranch.append(leftBranch[0])
                return rightBranch
        elif len(leftBranch) == 1:
            rightBranch = self.splitFunction(rightBranch)
        elif len(rightBranch) == 1:
            leftBranch = self.splitFunction(leftBranch)
        else:
            rightBranch = self.splitFunction(rightBranch)
            leftBranch = self.splitFunction(leftBranch)
        rInt = 0
        lInt = 0
        while len(ComBran) != (len(rightBranch)+len(leftBranch)):
            if rInt != len(rightBranch) and lInt != len(leftBranch):
                if rightBranch[rInt] <= leftBranch[lInt]:
                    ComBran.append(rightBranch[rInt])
                    if rInt < len(rightBranch):
                        rInt = rInt + 1
                elif leftBranch[lInt] < rightBranch[rInt]:
                    ComBran.append(leftBranch[lInt])
                    if lInt < len(leftBranch):
                        lInt = lInt + 1
            elif lInt != len(leftBranch):
                ComBran.append(leftBranch[lInt])
                if lInt < len(leftBranch):
                    lInt = lInt + 1
            elif rInt != len(rightBranch):
                ComBran.append(rightBranch[rInt])
                if rInt < len(rightBranch):
                    rInt = rInt + 1
        return ComBran
class MHNode:
    def __init__(self, integer):
        self.list = []
        self.height = 0
        self.layerN = 0
        self.nodeVal = integer
        self.LNode = None
        self.RNode = None
    def makeTree(self, list):
        self.list = self.fillNodeTree(1, 1, list)
        self.height = self.findTopLayer()
        self.permHeap()
    def fillNodeTree(self, i, num, list):
        self.nodeVal = list[i]
        self.layerN = num
        newList = list
        newList[i] = self
        if (2*i) < len(list):
            node1 = list[(2*i)]
            self.LNode = MHNode(node1)
            newList = self.LNode.fillNodeTree(2*i, num+1, newList)
        if ((2*i)+1) < len(list):
            node2 = list[(2*i)+1]
            self.RNode = MHNode(node2)
            newList = self.RNode.fillNodeTree((2*i)+1, num+1, list)
        return newList
    def findTopLayer(self):
        if self.LNode == None:
            return self.layerN
        else:
            found = self.LNode.findTopLayer()
        return found
    def insert(self, newVal):
        nNode = MHNode(newVal)
        self.list.append(nNode)
        nodePos = int((len(self.list)-1)/2)
        if self.list[nodePos].LNode == None:
            self.list[nodePos].LNode = nNode
        elif self.list[nodePos].RNode == None:
            self.list[nodePos].RNode = nNode
        nNode.layerN = self.list[nodePos].layerN + 1
        self.height = self.findTopLayer()
        self.heapify(len(self.list))
    def heapify(self, num):
        if self.list[num - 1] != None and self.list[int((num - 1) / 2)] != None:
            if self.list[num-1].nodeVal < self.list[int((num-1)/2)].nodeVal:
                self.list[num - 1].nodeVal, self.list[int((num-1)/2)].nodeVal = self.list[int((num-1)/2)].nodeVal, self.list[num - 1].nodeVal
                self.heapify(int((num-1)/2)+1)
    def permHeap(self):
        for i in range(1, len(self.list)+1):
            self.heapify(i)
    def MiniSort1(self):
        value = self.nodeVal
        newVal = None
        if self.LNode != None and self.RNode != None:
            if self.LNode.nodeVal <= self.RNode.nodeVal:
                if self.LNode.nodeVal != self.nodeVal and self.nodeVal < self.LNode.nodeVal:
                    newVal = self.LNode.MiniSort1()
                else:
                    newVal = self.RNode.MiniSort1()
            elif self.RNode.nodeVal < self.LNode.nodeVal:
                if self.RNode.nodeVal != self.nodeVal and self.nodeVal < self.RNode.nodeVal:
                    newVal = self.RNode.MiniSort1()
                else: #:
                    newVal = self.LNode.MiniSort1()
        elif self.RNode != None and self.LNode == None:
            newVal = self.RNode.MiniSort1()
        elif self.LNode != None and self.RNode == None:
            newVal = self.LNode.MiniSort1()
        if newVal != None:
            self.nodeVal = newVal
        return value
    #@profile
    def MiniSort(self):
        list = self.genList(10000)
        self.makeTree(list)
        sorted = []
        for i in range(1, len(self.list)):
            integer = self.MiniSort1()
            sorted.append(integer)
        #return sorted
    def genList(self, length):
        lister = list(range(0, length))
        for i in range(length):
            rand = random.randint(0, length-1)
            lister[i], lister[rand] = lister[rand], lister[i]
        lister.insert(0, None)
        return lister
hello = MHNode(None)
print(timeit.timeit(hello.MiniSort, number=1))
print("MiniHeap")
hello2 = sortSystem()
hello2.genList(10000)

print(timeit.timeit(hello2.inSort, number=1))
print("insert")
print(timeit.timeit(hello2.selSort, number=1))
print("select")
print(timeit.timeit(hello2.bubSort, number=1))
print("Buble")
hello = MergSort()
lister = hello.genList(10000)
    #[38,27,43,3,9,82,10]
print(timeit.timeit(hello.MergSortFunc, number=1))
print("MergSort")
