#Recursive Function:
#def-Function which calls itself repetedly till stopping condition occurs.

#sum of n integers using recursive function.

def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
r=sum(6)
print('result=',r)
