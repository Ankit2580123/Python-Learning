student = ["Karan", 85, "Delhi"] #student[0], student[1]..

student[0] = "Arjun" #allowed in python


print(len(student)) #returns length
##list slicing
list=[12,45,65,14,78,62,78,22,44]
# print(arr[1:5])
# print(arr[5:])
# print(arr[-5:-1])
# print(arr[-6:])
# list.append(100)
# print(list)
# list.sort()  #ascending order sort
# print(list)
# list.sort(reverse=True)  #descending order
# print(list)
# list.insert(2,500) 
# print(list)
# list.reverse()
# print(list)
# list.pop()  ##remove alements form last
# print(list)
# list.remove(78)
# print(list)
# list2=list.index(500)
# print("This is List2:",list2)

##TUPLES
tup=(41,25,15,85,32,17,49)
tup2=(1,)
print(type(tup2))

##Exercise1 take input from the users of three favourates movies
# favMovies=[]
# movi1=input("Enter Your First Favourites Movie : ")
# movi2=input("Enter Your Second Favourites Movie Names: ")
# movi3=input("Enter Your Third Favourites Movie Names: ")
# favMovies.append(movi1)
# favMovies.append(movi2)
# favMovies.append(movi3)
# print(favMovies)
 
#Exercise2 palindrome list or not

list1=[1,2,1]
list2=[1.2,3,4,5]
copy1=list1.copy()
copy2=list2.copy()
copy1.reverse()
copy2.reverse()

if copy2==list1:
                    print("Yes it is Palindrome")
else:
                    print("No it is not Palindrome")

