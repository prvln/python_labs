import random

class BST:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def print(self):
        for x in self:
            print(x)

    def add(self,value):
        if value<self.data:
            
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.add(value)

        elif value == self.data:

            raise ValueError(f'Такой узел уже существует {value}')
        elif value>self.data:
            
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.add(value)
    
    def __iter__(self):
        
        if self.left:
            yield from self.left
        
        yield self.data

        if self.right:
            yield from self.right


t = BST(8)
for i in range(0,30):
    print(f"Пытаемся добавить узел {i} в дерево")
    i = random.randint(0,10)
    t.add(i)

t.print()
