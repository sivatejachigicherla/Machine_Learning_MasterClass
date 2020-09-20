l = [1,2,3,'hi',[4,5,6]]
print('Contents of the list : ' , l)
print(l[4])
l.append('teja')
print('Appended list :' , l)
l.remove(3)
print(l)
l.insert(0,'tez')
print(l)
l.reverse()
print(l)
print('The last element is ' , l[-1])
l.clear()
print(l)
numList = [4,8,2,0,1,7,3]
print("contents of numList :" , numList)
numList.sort()
print('Sorted List : ',numList)
for num in numList:
    print(num)

print(numList[::2])
problems = 'nerdy,pale,intel'
por = problems.split(',')
print(por)
print(por[2])

numList = [1,1,5,9,6,7,7,5,8,5,5]
print(numList)
noDuplicates = set(numList)
print(noDuplicates)
numList = list(noDuplicates)
numList.sort()
print(numList)
