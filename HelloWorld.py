print("Hello, World!")
print('Hello, World!')
list_ex = [1,5,9,3,7,8,2,25,2]
#max in list
max = list_ex[0]
for item in list_ex:
    if(item > max) :
        max = item 
print(max)
#removing the duplicates
nodup = list(set(list_ex))
list_ex.sort()
print(list_ex)
print(nodup)
#unpacking the list
list_ex1 = [1,2]
x,y= list_ex1
print(x)
def talk():
    print('Import Success')