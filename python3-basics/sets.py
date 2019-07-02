# Creating empty set
set_test = set()
print(set_test)
print('---------------------------------------------------')
# Create set with string
name = 'krishnasure'
set_name = set(name)
print(set_name)
print('---------------------------------------------------')
# Create a set with list
set_list = set(['Java', 'python', 'dot net'])
print(set_list)
print('---------------------------------------------------')
# Creating set with number including duplicates
set_numbers = set([1,2,3,2,4,5,5,6,2,5])
print(set_numbers)
print('---------------------------------------------------')
# adding elements to set
set_numbers1 = set([1,2,3,4,5,3,6,4])
print(set_numbers1)
set_numbers1.add(7)
print(set_numbers1)
#adding tuple (8,10)
set_numbers1.add((8,10))
print(set_numbers1)
#adding multiple numbers
set_numbers1.update([11,14])
print(set_numbers1)
set_numbers1.update([16,20], {17,25})
print(set_numbers1)
print('---------------------------------------------------')
# Both discard and remove take a single argument, the element to be deleted from the set. 
# If the value is not present, discard() does not do anything. Whereas, remove will raise a KeyError exception.
set_remove_discard = set([1,2,3,4,5,6,7])
print(set_remove_discard)
set_remove_discard.discard(2)
print(set_remove_discard)
set_remove_discard.remove(4)
print(set_remove_discard)
print('---------------------------------------------------')
# Creating shallow copy using copy() method
set_shallow = set([1,2,3,4])
set_shallow_copy = set_shallow.copy()
print(set_shallow_copy)
# Clearing the set using clear() method
set_shallow_copy.clear()
print(set_shallow_copy)
# poping a set
# pop raises a KeyError exception if the set is empty
set_shallow.pop()
print(set_shallow)
print('---------------------------------------------------')
set1 = set([1,2,3,4,5])
set2 = set([4,5,6,7,8])
# print a new set with the values present in both set1 and set2
print(set1 & set2)
# above operation and using method name intersection shows same results
print(set1.intersection(set2))
# print a new set with values present in set1 but not in set2
print(set1.difference(set2))
# print a new set with values present in set2 but not in set1
print(set2.difference(set1))
# returns false as both have common elements
print(set1.isdisjoint(set2))
# update set1 by removing elements present in set2 from set1
set1.difference_update(set2)
print(set1)
# check if set1 is a subset of set2
print(set1.issubset(set2))
# check if set2 is a subset of set1
print(set2.issubset(set1))
# remove few items to make set1 a subset of set2
set1.remove(1)
set1.remove(2)
set1.remove(3)
print(set1.issubset(set2))
# check if set2 is super set of set1
print(set2.issuperset(set1))