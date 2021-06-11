class MasHeap:
    def __init__(self):
        self.heap = []
    def print(self):
        print(self.heap)
    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1
        while (i != 0 and value > self.heap[(i-1)//2]):
            self.heap[i] = self.heap[(i-1)//2]
            i = (i-1)//2
        self.heap[i] = value
    def delete1(self):
        n = len(self.heap)
        if n == 0:
            return None
        current = 0
        maxValue = self.heap[0]
        value = self.heap[n-1]
        self.heap.pop()
        n = n-1
        while (2*current +1 < n):
            largerChild = 2*current+1
            if (largerChild + 1 < n) and (self.heap[largerChild+1] > self.heap[largerChild]):
                largerChild += 1

            if value < self.heap[largerChild]:
                self.heap[current] = self.heap[largerChild]
                current = largerChild
            else:
                break

        self.heap[current] = value
        return maxValue
    def delete2(self):
        n = len(self.heap)
        if n == 0:
            return 0
        current = 0
        maxValue = self.heap[0]
        value = self.heap[n-1]
        self.heap.pop()
        n = n-1
        while 2*current+1 < n:
            leftChild = 2*current+1
            rightChild = leftChild +1
            if rightChild < n and self.heap[rightChild] > self.heap[leftChild]:
                largerChild = rightChild
            else:
                largerChild = leftChild

            if value < self.heap[largerChild]:
                self.heap[current] = self.heap[largerChild]
                current = largerChild
            else:
                break

        self.heap[current] = value
        return maxValue
    
