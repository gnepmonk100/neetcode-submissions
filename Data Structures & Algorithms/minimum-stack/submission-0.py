class MinStack:

    def __init__(self):
        self.items = []
        

    def push(self, val: int) -> None:
        self.items.append(val)

    def pop(self) -> None:
        self.items.pop()

    def top(self) -> int:
        top_element = self.items[-1]
        return top_element

    def getMin(self) -> int:
        return min(self.items)
        
