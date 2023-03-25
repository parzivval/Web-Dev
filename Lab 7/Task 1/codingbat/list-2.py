def count_evens(nums):
  count = 0
  for element in nums:
    if element % 2 == 0:
      count += 1
  return count

def big_diff(nums):
  return max(nums) - min(nums)

def centered_average(nums):
  sum = 0
  for element in nums:
    sum += element
  return (sum - min(nums) - max(nums)) / (len(nums)-2)


def sum13(nums):
    if len(nums) == 0:
        return 0
    for i in range(0, len(nums)):
        if nums[i] == 13:
            nums[i] = 0
            if i + 1 < len(nums):
                nums[i + 1] = 0
    return sum(nums)

def sum67(nums):
  for i in range(0, len(nums)):
    if nums[i] == 6:
      nums[i] = 0
      for j in range(i+1, len(nums)):
        temp = nums[j]
        nums[j] = 0
        if temp == 7:
          i = j + 1
          break
  return sum(nums)

def has22(nums):
  for i in range(0, len(nums)-1):
    if nums[i:i+2] == [2,2]:
      return True
  return False