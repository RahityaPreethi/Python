import pdb
def add(a,b):
    ans = a*b
    return ans

pdb.set_trace()
#breakpoint()
x = int(input("enter the value:"))
y = int(input('enter the value:'))
sum = add(x,y)
print(sum)