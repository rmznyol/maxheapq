class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heappush(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self,index):
        value = self.heap[index]
        l = len(self.heap)
        max_index = index
        while index < l :
            left_index = self._left_child(index)
            right_index = left_index + 1
            if left_index < l and self.heap[left_index] > value:
                max_index = left_index
            if right_index < l and self.heap[right_index] > value:
                max_index = right_index
            if index != max_index:
                self._swap(max_index,index)
                index = max_index
            else:
                return 
            
                   
    def heappop(self):
        match len(self.heap):
            case 0:
                return None
            case 1:
                return self.heap.pop()
            case _:
                self._swap(0,len(self.heap)-1)
                to_be_returned = self.heap.pop()
                self._sink_down(0)
                return to_be_returned
