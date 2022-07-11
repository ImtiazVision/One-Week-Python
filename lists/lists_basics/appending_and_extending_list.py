# 'append' adds a single value to the end of a list

list1 = [1,2,3,4]
list1.append(5)
print(list1) # output: list1 = [1,2,3,4,5]

# 'extend()' accepts an iterable and appends each item from that iterable to the end of the list

nums = [1,2,3]
nums.extend('abc')
print(nums)

# list1.append(nums) # appends just add the entire 2nd list to the end of the first list
# print(list1)

# extend offers iterable and go through each element of the 2nd list that we are extending upon and add elements from the 2nd list the to first list one by one. It add each element from the 2nd list to the end of the 1st list.
list1.extend(nums)
print(list1)
