#Recursion : It is a programming technique where a function calls itself in order to solve a problem.
#Recursion is often used to solve problems that can be broken down into smaller, similar subproblems.
#two cases: base and iterative cases
#Types: Direct Recursion, Indirect Recursion, Head Recursion , Tail recursion, Tree Recursion, Nested Recursion

#1. Direct Recursion
#print n numbers
'''
def numbers(n):
    if n==0:
        return
    print(n,end=' ')
    numbers(n-1)
n=int(input('Enter the value:'))
numbers(n)
'''

#print factorial of a number
'''
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
n=int(input('Enter the value:'))
print(factorial(n))
'''

#2. Indirect Recursion
#print n numbers
'''
def fun1(n):
    if n>0:
        print(n,end=' ')
        fun2(n-1)
def fun2(n):
    if n>0:
        print(n,end=' ')
        fun1(n-1)
n=int(input('Enter the value:'))
fun1(n)
'''

#given num is even/odd
'''
def even(n):
    if n==0:
        return True
    return odd(n-1)
def odd(n):
    if n==0:
        return False
    return even(n-1)
n=int(input('Enter the value:'))
if even(n):
    print('Even')
else:
    print('Odd')
'''

#3.Tree Recursion
'''
def tree(n):
    if n==-1:
        return
    print(n,end=' ')
    tree(n-1)
    tree(n-1)
n=int(input('Enter the value:'))
tree(n)
'''

#fibonacci series
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input('Enter the value:'))
print(fib(n))
