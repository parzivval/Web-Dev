# def min(a, b, c, d):
#     n=[a,b,c,d]
#     n.sort()
#     return n[0]
# arr=input().split(' ')
# print(min(arr[0], arr[1], arr[2], arr[3]))

# def power(a, n):
#     return a**n
# arr=input().split(' ')
# a=int(arr[0])
# n=int(arr[1])
# print(power(a, n))

def xor(x, y):
    if x!=y:
        print(1)
    else:
        print(0)
arr=input().split(' ')
x=arr[0]
y=arr[1]
xor(x, y)
