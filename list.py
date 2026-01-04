list1=["apple",1,3,4,5, "banna",True,6,7,8.3]
list2=[12,13,"orange"]

list5 = []  #empaty list
list4 = list() #Empaty list using list()
list6 = list((1,2,3)) # convert to tuble to list
print("list5 :", list5)



print("list1[0] :",list1[0])  #first element
print("list1[-1]:",list1[-1])  #last element

print("list1[:4]",list1[:4])  #first 4 elements
print("list1[2:]:",list1[2:])  #from index 2till end
print("list[2:5]:",list1[2:5]) #from index2to 4
print("list1[::-1]:",list1[::-1]) #reverse list

#concateenation
list1[1]= "watermeloen"
print("After reassignment:",list1)
