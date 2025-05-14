values = [1, 2, "amber", 4, 5]
# list is a data type that allows multiple values and can be different data types

print(values[0]) #1

print(values[3]) #4

print(values[-1]) #5

print(values[1:3]) #2 'amber'

values.insert(3, "zach") #1, 2, 'amber', 'zach', 4, 5

print(values)

values.append("End") #1, 2, 'amber', 'zach', 4, 5, 'End'

print(values)

values[2] = "AMBER" #Updating

del values[0] #deleting #2, 'AMBER', 'zach', 4, 5, 'End'

print(values)

# Tuple

val = (1, 2, "amber")

print(type(val)) #class 'tuple'

print(val[1]) # 2

# Dictionary

dic = {"a":10, 2:20, 3:"hi"}

print(type(dic)) #class 'dict'

print(dic) #{'a': 10, 2: 20, 3: 'hi'}

print(dic[2]) #20

print(dic[3]) #hi

print(dic["a"]) #10

# keys

dict = {}

dict["firstname"] = "Amber"
dict["lastname"] = "Zach"
dict["gender"] = "female"

print(dict) #{'firstname': 'Amber', 'lastname': 'Zach', 'gender': 'female'}

print(dict["firstname"]) #Amber