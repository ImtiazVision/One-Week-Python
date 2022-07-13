# count() method
# The count() method returns the number of times a value occurs in a list. If the value is not in the list, it returns '0'

import numbers


language = ['C#', 'C#','C','PHP', 'Python', 'Java', 'JavaScript']

print(language.count('C#'))

# reverse() method reverses a list in-place that is it doesn't make a new copy of the list but rather rearrange the list in reverse order in the same container/list/data structure

nums = [1,2,3,4,5,6,7,8]

nums.reverse()
print(nums)


# sort() method arrange list elements in an ascending (least to greatest) order

numbers = [8, -2, 4, -9, 3, 1, -4, 5, 4]

numbers.sort()  # [-9, -4, -2, 1, 3, 4, 4, 5, 8]

print(numbers)

numbers.sort(reverse=True) 
print(numbers)  # [8, 5, 4, 4, 3, 1, -2, -4, -9]

# lists are mutable

nums1 = [1,2,3]
nums2 = nums1
# here both 'nums1' and 'nums2' are pointing to the same list/container in memory (think about lists as pill container)
print(nums1)
print(nums2)