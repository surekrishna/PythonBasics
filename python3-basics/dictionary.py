# Creating a dictionary
person_dictionary = {'name' : 'krish', 'gender' : 'Male', 'city' : 'Bangalore'}
print(person_dictionary)
print(person_dictionary['name'])
alphabets = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e'}
# accessing with key
print(alphabets.get(1))
#accessing with key if key is not present display None
print(alphabets.get(27, 'None'))
print(alphabets.has_key(1))
print(alphabets.has_key(27))
print('----------------------------------------------------------------')
# Looping over dictionary
for k, v in person_dictionary.items():
    print('Key :: %s ' % k)
    print('Value :: %s ' % v)
    print('=================')
print('----------------------------------------------------------------')
# Adding elements to dictionary
person1_dictionary = {}
person1_dictionary['name'] = 'king'
person1_dictionary['gender'] = 'Male'
person1_dictionary['city'] = 'Heaven'
print(person1_dictionary)
print('----------------------------------------------------------------')
# Combining two dictionaries
person2_dictionary = {'name' : 'queen'}
person22_dictionary = {'gender' : 'Female', 'city' : 'Heaven'}
person2_dictionary.update(person22_dictionary)
print(person2_dictionary)
print('----------------------------------------------------------------')
# Popping key/value pair from dictionary
person2_dictionary.pop('city', None)
print(person2_dictionary.pop('email', None))
print(person2_dictionary)