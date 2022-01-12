# create the dict
my_dict = {"jack": 3, "cjj": 2}

# print the dict
print("Out{}".format(my_dict))

# print the dict according to the key
print(my_dict["jack"])

if "rose" not in my_dict:
    print("ERROR")

if "cjj" in my_dict:
    print("OK")

print(my_dict.get("cjj"))

a = sorted(my_dict.items(), key=lambda it: it[0])
print(a)

keys = []
for elem in my_dict.keys():
    keys.append(elem)
print(keys)
