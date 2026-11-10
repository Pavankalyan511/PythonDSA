#inorder to preorder conversion using stack
'''exp= input("Enter the expression: ")
stack = []
result = []
priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
rev=exp[::-1]
for ch in rev:
    if ch.isalnum():
        result.append(ch)
    elif ch == ')':
        stack.append(ch)
    elif ch == '(':
        while stack and stack[-1] != ')' and priority.get(stack[-1], 0) >= priority.get(ch, 0):
            result.append(stack.pop())
        stack.append(ch)
while stack:
    result.append(stack.pop())
prefix =' '.join(result[::-1])
print(prefix)'''

#prefix -> postfix
'''exp=input('Enter the expression:')
stack=[]
for ch in exp[::-1]:
    if ch.isalnum():
        stack.append(ch)
    else:
        a=stack.pop()
        b=stack.pop()
        result=a+b+ch
        stack.append(result)
print(stack[-1])'''

#postfix->prefix
'''exp=input('Enter the expression:')
stack=[]
for ch in exp[::-1]:
    if ch.isalnum():
        stack.append(ch)
    else:
        b=stack.pop()
        a=stack.pop()
        result=ch+a+b
        stack.append(result)
print(stack[-1])'''