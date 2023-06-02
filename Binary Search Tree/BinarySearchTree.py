class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None #smaller
        self.right_child = None #greater
        self.parent = None # pointer to parent node in tree

class Binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        #判斷tree是否為空
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
                cur_node.left_child.parent = cur_node #set parent
            else:
                self._insert(value, cur_node.left_child)

        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
                cur_node.right_child.parent = cur_node #set parent
            else:
                self._insert(value, cur_node.right_child)

        # value == cur_node.value
        else:
            print("This value has existed")

    def print_tree(self):
        if self.root!=None:
        	self._print_tree(self.root)

    def _print_tree(self,cur_node):
    	if cur_node!=None:
        	self._print_tree(cur_node.left_child)
        	print(str(cur_node.value))
        	self._print_tree(cur_node.right_child)



    def height(self):
        if self.root != None:
            return self._height(self.root,0)
        else:
            return

    # 我們要在每一次遞迴呼叫時傳入cur_height，如果沒有像parameter
    # 樣傳入或儲存成global variable會造成 無法儲存cur_height
    def _height(self, cur_node, cur_height):
        if cur_node == None:
            return cur_height #0
        # 找一個最高的子樹
        left_height = self._height(cur_node.left_child,cur_height+1)
        right_height = self._height(cur_node.right_child,cur_height+1)

        return max(left_height, right_height)

    # returns the node with specified input value
    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child != None:
            return self._find(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._find(value, cur_node.right_child)

    def delete_value(self, value):
        return self.delete_node(self.find(value))


    def delete_node(self, node):
        #returns the node with min value in tree rooted at input Node
        #we will pass the single node to treat as the root of a binary search fill_tree
        def min_value_node(n):
            current = n
            # traverse down to the left of the tree until it finds the smallest element returning this value
            while current.left_child != None:
                current = current.left_child
            return current

            #returns the number of children for the specified node
            # return the number of the children and attach the input node either 0,1 or two
        def num_children(n):
            num_children = 0
            if n.left_child != None:
                num_children +=1
            if n.right_child != None:
                num_children += 1
            return num_children



        #create variable to hold both the parent of the node to delete as well as
        #the number of children get the parent of the node to be deleted
        node_parent = node.parent

        #get the number of children of the node to be deleted
        node_children = num_children(node)

        #break operation into different cases based on the
        #structure of the tree & node to be delete

        #CASE 1 (node has no children)
        if node_children == 0:
            #remove reference to the node from the node_parent
            if node_parent.left_child == node:
                node_parent.left_child = None
            else:
                node_parent.right_child = None

        #CASE 2 (node has a single child)
        if node_children == 1:

            # get the single child node
            if node.left_child != None:
                child = node.left_child
            else:
                child = node.right_child

            #replace the node to be deleted with its child
            if node_parent.left_child == node:
                node_parent.left_child = child
            else:
                node_parent.right_child = child

            #correct the parent pointer in node
            child.parent = node_parent

        #CASE 3 (node has two children)
        if node_children == 2:

            # get the inorder successor of the deleted node
            successor = min_value_node(node.right_child)

            #copy the inorder successor's value to the node formerly
            #holding the value we wished th delete
            node.value = successor.min_value_node

            #delete the inorder successor now that it's value was
            #copied into the other node
            self.delete_node(successor)
    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child != None:
            return self._search(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._search(value, cur_node.right_child)
        else:
            return False

def fill_tree(tree, num_elems=10, max_int=50):
    from random import randint
    for _ in range(num_elems): #10個 value
        cur_elem = randint(0, max_int) #隨機0~50(不含50)的值
        tree.insert(cur_elem)
    return tree

#============================================================

#建立1~9的樹
tree = Binary_search_tree()
for num in range(10):
    tree.insert(num)


#delete node 5
tree.delete_value(5)
tree.delete_value(4)
tree.delete_value(1)
#印出樹
tree.print_tree()
