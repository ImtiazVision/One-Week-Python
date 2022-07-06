# 'append' adds a single value to the end of a list

list1 = [1,2,3,4]
list1.append(5)
print(list1) # output: list1 = [1,2,3,4,5]

# 'extend()' accepts an iterable and appends each item from that iterable to the end of the list

nums = [1,2,3]
nums.extend('abc')
print(nums)