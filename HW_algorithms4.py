# 1. Even First
# Your input is a list of integers, and you have to reorder its entries so that the even entries appear first.
# You are required to solve it without allocating additional storage (operate with the input list).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

def even_odd(arr):
    next_even = 0
    next_odd = len(arr) - 1

    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            if arr[next_odd] % 2 == 0:
                arr[next_odd], arr[next_even] = arr[next_even], arr[next_odd]
                next_even += 1
                next_odd -= 1
            else:
                next_odd -= 1
    return arr


print(even_odd([1, 5, 2, 0, 3, 4, 5, 7, 8, 1, 10]))


# 2. Increment a Number
# Write a program that takes as input a list of digits encoding a nonnegative decimal integer D and
# updates the list to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].

def plus_one(nums):

   i = len(nums) - 1

   while i >= 0:
      if nums[i] + 1 <= 9:
         nums[i] = nums[i] + 1
         break
      else:
         nums[i] = 0
      i -= 1
   if i < 0:
      nums.insert(0, 1)
   return nums


print(plus_one([1, 2, 9]))