student = {"name":"Ravi", "age" : "A"}

print(student["name"])   #Ravi
student["age"]=21        #update
student["course"]="cs"   # add new
print(student)


student2={
    "name":"john",
    "age":20,
    "course":"cs"

}

print(student2["name"])  #john
print(student2.get("age")) #20
print(student2.keys())   # dict_keys(['name','age',course])
print(student2.values()) #dict_values(['john',20,'cs'])