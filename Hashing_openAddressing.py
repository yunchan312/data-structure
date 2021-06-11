class Dictionary:
    def __init__(self, size):
        self.M = size
        self.keyList = [None]*size
        self.valueList = [None]*size
    def hashFunc(self,key):
        return key%self.M
    def put_LinearProbing(self, key, value): #Linear Probing
        initialPos = self.hashFunc(key)
        i = initialPos
        while True:
            if self.keyList[i] == None:
                self.keyList[i] = key
                self.valueList[i] = value
                return
            if self.keyList[i] == key:
                self.valueList[i] = value

            i = (i+1)%self.M
            if i == initialPos:
                return
    def get_LinearProbing(self,key):
        initialPos = self.hashFunc(key)
        i = initialPos
        while self.keyList[i] != None:
            if self.keyList[i] == key
                return self.valueList[i]
            i = (i+1)%self.M
            if i == initialPos:
                return
    def put_QuadraticProbing(self, key, value):
        initialPos = self.hashFunc(key)
        i = initialPos
        j = 0
        while True:
            if self.keyList[i] == None:
                self.keyList[i] = key
                self.valueList[i] = value
                return
            if self.keyList[i] == key:
                self.valueList[i] = value
            j += 1
            i = (initialPos + j*j)%self.M
            if self.N>self.M:
                return
    def get_QuadraticProbing(self, key):
        initialPos = self.hashFunc(key)
        i = initialPos
        j = 0
        while self.keyList[i] != None:
            if self.keyList[i] == key:
                return self.valueList[i]
            j += 1
            i = (initialPos + j*j)%self.M
        return

