# key,value pairs.
my_dict = {'Dave':'001','Ava':'002','Joe':'003'}
print(my_dict)
print(type(my_dict))
print('\n'
      ,'\n')
#make a dictionary dict() consructor
my_dict = dict()
print(my_dict)
print(type(my_dict))
print('\n'
      ,'\n')
#Use dict 
my_dict = dict(name = 'john' , age = 36, country= 'Norway')
print(my_dict)
print('\n'
      ,'\n')
# accessing items
my_dict = dict(name = 'john', age = 36 , country = 'Norway')
print(my_dict)
x = my_dict['country']
print(x)
my_dict = dict(name = 'john', age = 36 , country = 'Norway')
print(my_dict)
x = my_dict.get('country')
print(x)
my_dict = dict(name = 'john', age = 36 , country = 'Norway')
print(my_dict)
x = my_dict.keys()
print(x)
my_dict = dict(name = "John", age = 36, country = "Norway")
print(my_dict)
x = my_dict.keys()
print(x) #before the change
my_dict["color-like"] = "white"
print(my_dict)
print(x) #after the change
print('\n')
#check if Key Exists
my_dict = dict(name = "John", age = 36, country = "Norway")
print(my_dict)

if "country" in my_dict:
 print("Yes, 'country' is one of the keys in the my_dict dictionary")
print('\n')
print("Change Values")
my_dict = dict(name = "John", age = 36, country = "Norway")
print(my_dict)

my_dict["name"] = "Ford"
my_dict["color-like"] = "Blue"
print(my_dict)

my_dict = dict(name = "John", age = 36, country = "Norway")
print('Print all values in the dictionary by using values() method:')
for x in my_dict.values():
      print(x)
print('Print all key names in the dictionary by using keys() method:')
for x in my_dict.keys():
      print(x)
print('Loop through both keys and values, by using the items() method:')
for x, y in my_dict.items():
      print(x, y)
