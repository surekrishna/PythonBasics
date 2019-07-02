# predefined methods in List -> append(value), insert(index, value), extend(another_list), index(item)
# remove(item), pop(), pop(index), sort(), reverse(), sorted(list)
# How to create a List and access
companies = ['mindtree', 'vit', 'amazon']
print('Getting first item : ' + companies[0])
print('Getting second item : ' + companies[1])
print('Getting third item : ' + companies[2])
print('-----------------------------------------')
# Two dimentional List
companies1 = [['mindtree', 'vit'], ['amazon', 'sap']]
print(companies1)
print('-----------------------------------------')
# Adding element to the existing List will be added at end
companies.append('google')
print(companies)
companies.append('facebook')
print(companies)
print('-----------------------------------------')
# Adding element to the existing List with specified index
companies.insert(1, 'TCS')
print(companies)
print(companies[1])
print('-----------------------------------------------------')
# Extending List
companies2 = ['Wipro', 'Infosys']
companies.extend(companies2)
print(companies)
print('-------------------------------------------------------------------')
# Get index of item from list
print(companies.index('Wipro'))
print('------------------------------------------------------------')
# Remove item from the list
companies.remove('google')
print(companies)
print('---------------------------------------------')
# popping the item from the List, Item will be removed from last and will return the item 
numbers = [1,2,3,4,5]
print(numbers)
print(numbers.pop())
numbers.pop()
print(numbers)
print('---------------------------------------------')
# popping the item from the list with specified index
numbers.pop(1)
print(numbers)
print('---------------------------------------------')
# sorting the items from the list
numbers1 = [19,4,23,1,52]
numbers1.sort()
print(numbers1)
print('---------------------------------------------')
# sorting the items from the list
numbers2 = [19,4,23,1,52]
numbers2.reverse()
print(numbers2)
print('---------------------------------------------')
# Similar to the sort method, you can also use the sorted function which also sorts the list. 
# The difference is that it returns the sorted list, while the sort method sorts the list in place. 
# So this function can be used when you want to preserve the original list as well.
numbers3 = [1,5,3,7,2,4]
print(numbers3)
print(sorted(numbers3))
print(numbers3)


