tuple1=("apple",1,3,4,5, "banna",True,6,7,8.3)
tuple2=(12,13,"orange")

tuple5 = () #empaty tuple
tuple4 = tuple() #Empaty tuple using tuple()
tuple6 = tuple([1,2,3]) # convert to list to tuple
print("tuple5 :", tuple5)


print("tuple[0] :",tuple[0])  #first element
print("tuple[-1]:",tuple[-1])  #last element

print("tuple1[:4]",tuple1[:4])  #first 4 elements
print("tuple1[2:]:",tuple1[2:])  #from index 2till end
print("tuple1[2:5]:",tuple1[2:5]) #from index2to 4
print("tuple1[::-1]:",tuple1[::-1]) #reverse list

#concateenation
print("tuple1+tuple2:",tuple1+tuple2)

#no reassignment
print("After reassignment:",tuple1)
