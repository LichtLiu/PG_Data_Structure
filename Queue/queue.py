from collections.abc import Iterable

class Queue:
    """docstring for Queue."""

    def __init__(self, initial_data):
        self.queue = []
        self.initial_data = initial_data

        if isinstance(initial_data, Iterable):
            self.queue = initial_data
        else:
            raise NotImplementedError('Initial was not iterable data')
    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return "queue{}".format(self.queue)

    def __getitem__(self, i):
        return self.queue[i]


    @property
    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def is_empty(self):
        return self.queue.__len__() == 0




def main():
    myqueue = Queue([])
    print(myqueue.is_empty())

if __name__ == '__main__':
    main()
