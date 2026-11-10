#insert at end in a doubly linked
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Doublylinkedlist:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end='<->')
            temp=temp.next
        print('Tail')
dll=Doublylinkedlist()
n=int(input('Enter no.of nodes:'))
for i in range(n):
    value =int(input('Enter value:'))
    dll.insert_end(value)
print('DLL:')
dll.display()
