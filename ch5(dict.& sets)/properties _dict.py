#properties:
#1.                            it is unordered
# 2.                           it is mutable like list 
# 3.                           it is indexed
# 4.                           can't contained duplicate keys 


# methods:
#1.    dict.keys()

dic={
    "name":"Navjot",
    "class":"3rd",
    "Roll no.": 1,
    "std. ID":78

}

print(dic.keys())
print(dic.values())
print(dic.items())

# dic.get()

print(dic.get("name"))
print(dic.get("std. ID",900))                 # by 'dict.get(key,default)' if we want to give default value t pre-existing value not valid
print(dic.get("Section"))               # print : None
print(dic.get("Section","c"))           #          by 'dict.get(key,default)'

#dic.update({other_dict.})
dic.update({"Father Name ":"XYZ"})
print(dic)

#dict.pop(key)
dic.pop("Roll no.")
print(dic)

#dict.popitem()  = remove last pair
dic.popitem()
print(dic)

#dict.clear()   = remove all elements
# dic.clear()
# print(dic)


#dict.copy()
new_dic=dic.copy()
print(new_dic)

#dic.fromkeys()
keys = ["a","b","c"]
d=dict.fromkeys(keys,0)
print(d)

subject = ["maths","english","science"]
marks=dict.fromkeys(subject,33)
print(marks)

