class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def delete(self):
        cur_node = self.head
        last_node = cur_node
        while cur_node.next != None:
            last_node = cur_node
            cur_node = cur_node.next
        last_node.next = None

    def delete_index_node(self, index):
        if linked_list.length(self) <= index:
            print("the index is bigger than list")
        cur = self.head
        last_node = cur
        indx = 0
        while cur.next != None:
            last_node = cur
            cur = cur.next
            if indx == index:
                last_node.next = cur.next
            indx += 1

    def insert_index_node(self, index, data):
        if linked_list.length(self) <= index:
            print("your index is bigger than list")
        new_node = Node(data)
        indx = 0
        cur = self.head
        while cur.next != None:
            cur = cur.next
            if indx == index:
                new_node.next = cur.next
                cur.next = new_node
            indx += 1

    def __str__(self):
        elements = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        print(elements)


option = None

while option is None:
    choose = input("Do you want to start? yes/no")
    if choose[0].lower() == "y":
        option = True
    elif choose[0].lower() == "n":
        option = False
        print("Goodbye")
    else:
        print("please try again")

while option:
    l = linked_list()
    func = input(
        "Which function do you want to use? \n1.append 2.delete 3.delete from index 4.insert data from index 5.result"
    )
    if func == "1":
        data = input("enter a number")
        l.append(data)
        print("success")
    else:
        print("ooopps, not a value there")

    if func == "2":
        if l.length() <= 0:
            print("hey no object in the list")
        else:
            l.delete()
            print("success")
