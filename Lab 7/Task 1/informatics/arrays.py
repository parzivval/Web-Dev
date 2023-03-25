# n=int(input())
# arr=input().split(' ')
# for i in range(0, n, 2):
#     print(arr[i], end = ' ')

# n=int(input())
# arr=input().split(' ')
# for i in range(0, n):
#     if int(arr[i])%2==0:
#         print(arr[i], end = ' ')

# n=int(input())
# count=0
# arr=input().split(' ')
# for i in range(0, n):
#     if int(arr[i])>0:
#         count+=1
# print(count)

# n=int(input())
# count=0
# arr=input().split(' ')
# for i in range(0, n):
#     if int(arr[i])>int(arr[i-1]):
#         count+=1
# print(count)

# n=int(input())
# arr=input().split(' ')
# count=0
# for i in range(1, n):
#     if (int(arr[i])>0 and int(arr[i-1])>0) or (int(arr[i])<0 and int(arr[i-1])<0):
#         count+=1
# print("YES") if count>0 else print("NO")

# n=int(input())
# arr=input().split(' ')
# count=0
# for i in range(1,n-1):
#     if (arr[i] > arr[i-1]) & (arr[i] > arr[i+1]):
#         count+=1
# print(count)

n=int(input())
arr=input().split(' ')
arr.reverse()
print(*arr, sep=' ')