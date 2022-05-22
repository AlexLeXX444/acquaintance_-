# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
nums = list(map(int, input().split(", ")))
max = None
for i in range (len(nums)):
    if nums[i] > nums[i-1]:
        max = nums[i]
print(max)