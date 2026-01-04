#for i in range(6):
#  print(i)

# for i in range(1,6):
#     print(i)

# for i in range(1,10,2):
#     print(i)

# for i in range(10,0,-1):
#     print(i)

# sum of 1 to n numbers
#n = int(input("Enter the number:"))
#sum = 0
#for i in range(1,n+1):
    #sum += i
#print(f"sum={sum}")


#list1=[10,20,30,40]
#print(list1[0])
#print(list1[1])
#print(list1[2])
#print(list1[3])

#for i in list1:
    #print(i)

    #for index,value in enumerate(list1):
       #print(index,value)

# #str1="dilna"
# for char in str1:
#     print(char)
# fruits=["apple","orange","banna"]
# for index,fruit in enumerate(fruits,start=1):
#     print(index,fruit)


#sum of number in an list
# marks=[30,50,60,34,45]
# total_mark=0
# for mark in marks:
#     total_mark+=mark
# print(f"total mark={total_mark}")

# marks=[30,50,29,40,60]
# largest=marks[0]
# for mark in marks:
#     if mark>largest:
#         largest=mark
# print(f"largest:{largest}")

# marks=[30,50,29,40,60]
# smallest=marks[0]
# for mark in marks:
#     if mark<smallest:
#         smallest=mark
# print(f"smallest:{smallest}")

#for loop in dictonary

#student = {"name":"Rahual","age":20,"grade":"A"}
# for i in student:
#     print(i,student[i])


#     for i in "banna":
#         print(i)
    
# student = {"name":"Rahual","age":20,"grade":"A"}

# for key, value in student.items():
#     print(key,value)

# student = {"name":"Rahual","age":20,"grade":"A"}

# for i in student.values():
#     print(i)

    
# reverse a string

# word="hello"
# reverse=''
# for char in word:
#     reverse=char+reverse
# print(f"reverse:{reverse}")    


#check given sting palndrom

# word=input("enter a word:")
# revese=""
# for char in word:
#     revese=char+revese
# print(f"reverse:{revese}")

# if word==revese: #word[::-1]
#     print(f"{word} is palindrom")
# else:
#     print(f"{word} is not a palindrom")

# nested for loop


# for i in range(4):
#     print("*",end="")


# for i in range(5):
#     for j in range(5):
#         print(" * ",end=" ")
#     print()    


# for i in range(5):
#     for j in range(i+1):
#         print(" * ",end=" ")
#     print()    

# for i in range(5):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()    

n=5
for i in range(1,n+1):
    for j in range(i):
        print(j+1,end=" ")
    print()