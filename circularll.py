#circular linked list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLL:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            newnode.next=self.head
            return
        temp=self.head
        while temp.next!=self.head:
            temp=temp.next
        temp.next=newnode
        newnode.next=self.head
    def traverse(self, start):
        temp=temp.next
        while temp.data!= start:
            temp=temp.next
            if temp==self.head:
                print('Node not found')
                return
        first=temp
        while True:
            print(temp.data, end='->')
            temp=temp.next
            if temp==first:
                break
            print('(Back to starting node)')
cll=CLL()
n=int(input("Enter no.of nodes:"))
for i in range(n):
    cll.insert(int(input('Enter value:')))
start=int(input('Enter starting point:'))
cll.traverse(start)