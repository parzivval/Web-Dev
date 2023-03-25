# n=int(input())
# i=1
# while i*i<=n:
#    print(i*i, ' ')
#    i=i+1

# n=int(input())
# i=1
# while i<=n:
#     i=i+1
#     if n%i==0:
#         print(i)
#         if i!=0:
#             break

# n=int(input())
# m=1
# while m<n:
#     print(m, end=' ')
#     m=m*2

# a=int(input())
# i=1
# while i<a:
#     i*=2
# if i==a:
#     print('YES')
# else:
#     print('NO')

n=int(input())
k=0
while 2**k<n:
    k+=1
print(k)