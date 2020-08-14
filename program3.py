list1=[1,2,3,4,5,"a","b","Apple"]
list2=["MyCaptain","AI","Workshop"]
print("Lists: \n")
print("before:")
print(list1)
print(list2)

#1.Assigning elements to different lists:
list1.append(12)
n=len(list2)
list2[n-1]="Captain"
list2.insert(n,"Aviral")

print("After list manipulation:")
print(list1)
print(list2)

#2.Accessing elements from a tuple
print("\n\n")
print("Accesing Tuples:-")
tuple1=(1,2,3,4,5,6)
print(tuple1)
print(tuple1[0])
for i in tuple1:
    print(i, end="  ")

#3.Deleting different elements in a dictionary
print("\n\n")
print("Dictionary:")
dict1={1:"a",2:"b","Ram":43,"dict":{"a":1,"b":2},"list":[1,2,3,4]}
print("The dictionary is: ",dict1)
del dict1[1]
dict1.pop("list")
print("After  different deletion operations,\n",dict1)










































