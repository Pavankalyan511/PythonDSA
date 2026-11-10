#valid paranthesis
'''s=input("enter parenthesis:")
stack=[]
for ch in s:
    if ch=='(':
        stack.append(ch)
    elif ch==')':
        if len(stack)==0:
            print('not balanced')
            break
        stack.pop()
else:
    if len(stack)==0:
        print('balanced')
    else:
        print('unbalanced')
'''

'''
s=input("enter parenthesis:")
stack=[]
for ch in s:
    if ch=='(':
        stack.append(ch)
    elif ch==')':
        if stack:
            stack.pop()
        else:
            continue
result=s+(')'*len(stack))
print(result)
'''

#delete if not balanced
'''
s=input("enter parenthesis:")
stack=[]
result=[]
for ch in s:
    if ch=='(':
        stack.append(len(result))
        result.append(ch)
    elif ch==')':
        if stack:
            stack.pop()
            result.append(ch)
        else:
            continue
for i in reversed(stack):
    result.pop(i)
print(''.join(result))
'''

s=input("enter parenthesis:")
stack=[]
for ch in s:
    if ch=='(' or ch=='[' or ch=='{':
        stack.append(ch)
    elif ch==')' or ch==']' or ch=='}':
        if not stack:
            print('not balanced')
            break
        top=stack.pop()
if len(stack)==0:
    print('balanced')
else:
    print('not balanced')