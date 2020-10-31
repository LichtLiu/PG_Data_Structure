
from collections.abc import Iterable
#class ClassName(object):
#>>> when you inherit from "object", this class is a "new style"
#>>> In Python 3.x all classes are new style - no need to set the metaclass.

#class Stack(object):
class Stack:
    def __init__(self, initial_data):
        self.stack = []
        self.initial_data = initial_data
        
        if isinstance(initial_data, Iterable):
            self.stack = list(initial_data)

        else:
            raise NotImplementedError('Initial was not iterable data')

    def __repr__(self):
        #直接輸入變數，輸出則為__repr__返回的字串
        return "Stack(initial_data={!r})".format(self.initial_data)

    def __str__(self):
        return "stack({})".format(self.stack)

    #return: int
    def __len__(self):
        return len(self.stack)

    def __getitem__(self, i):
        return self.stack[i]

    @property
    def is_empty(self):
        return len(self.stack) == 0

    #return
    def push(self, data):
        self.stack.append(data)

    #return: data that pop out
    def pop(self):
        if not self.is_empty:
            return self.stack.pop()

    # return: top element in stack
    def peek(self):
        return self.stack[-1]


def main():
    list1 = []
    stack = Stack(list1)
    print(stack)

    stack.push(1)
    print(stack)

    stack.pop()
    print(stack)

    stack.push(3)
    print(stack)

    stack.push(4)
    print(stack)

    print(stack.peek())



if __name__ == '__main__':
    main()
