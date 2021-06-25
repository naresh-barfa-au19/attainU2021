class Node:
    def __init__(self,data):
        self.data = data
        self.link = None
node1 = Node(10)
print("node1 ",node1,node1.data,node1.link)

class Linkedlist:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if(self.head is None):
            print("Linkedlist is empty :( ")
        else:
            while(self.head is not None):
                print(self.head.data,"---->",end=" ")
                self.head = self.head.link

    
if __name__ == '__main__':
    LList = Linkedlist()
    LList.head = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    LList.head.link = node2
    node2.link = node3

    LList.print_LL()