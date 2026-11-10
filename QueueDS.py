#insert operation in a queue
'''import queue
q=queue.Queue()
n=int(input("Enter number of elements:"))
for i in range(n):
    value=int(input("Enter value:"))
    q.put(value)
print("Queue:", list(q.queue))
'''

#insert operation in a queue delete operation
'''import queue
q=queue.Queue()
n=int(input("Enter number of elements:"))
for i in range(n):
    value=int(input("Enter value:"))
    q.put(value)
print("Queue:", list(q.queue))
if not q.empty():
    print("Deleted element:", q.get())
else:
    print("Queue Empty")
print("Queue:",list(q.queue))
print("Element ready to be deleted",q.queue[0])
'''

#queue overflow
'''
import queue
size=int(input("Enter size of queue:"))
q=queue.Queue(maxsize=size)
n=int(input("Enter number of elements:"))
for i in range(n):
    val=int(input("Enter a value:"))
    if not q.full():
        q.put(val)
    else:
        print("queue overflow")
print("Queue:",list(q.queue))
'''

'''
import queue
q=queue.Queue()
n=int(input("Enter number of elements:"))
for i in range(n):
    value=int(input("Enter value:"))
    q.put(value)
print("Queue:", list(q.queue))
if not q.empty():
    print("Front:",q.queue[0])
    print("Rear:",q.queue[-1])
else:
    print("Queue is Empty")
'''

import queue
q=queue.Queue()
n=int(input("Enter number of elements:"))
for i in range(n):
    value=int(input("Enter value:"))
    q.put(value)
oc=int(input("Enter element:"))
count=list(q.queue).count(oc)
print("Count is:",count)