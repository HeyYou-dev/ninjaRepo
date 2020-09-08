import random

class MinStack:
    def __init__(self):
        """ instanciating data structure here """
        self.stack = []

    def to_push(self, item: int) -> None:
        self.stack.append(item)

    def from_pop(self) -> int:
        if self.stack:
            return self.stack.pop()

    def get_top(self) -> int:
        if self.stack:
            return self.stack.pop(-1)

    def get_min(self) -> int:
        if self.stack:
            return min(self.stack)
        else:
            return 'stack is empty'

    def GetStack(self):
        return self.stack


# Object creation will be here
minstack = MinStack()
for i in range(5):
    minstack.to_push(random.randint(1, 10))

print(minstack.GetStack())
minstack.to_push(12)
print(minstack.GetStack())
print(minstack.get_top())
print(minstack.get_min())
print(minstack.from_pop())

a = None

if a  in ("a","b"):
    print ("you are wroing ")
else:
    print(" you are correct")
