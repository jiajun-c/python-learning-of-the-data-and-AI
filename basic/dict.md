# The dictionary
The dictionary in the python is similar to the map in the c++, like hash
It has a key - value pair
## 1.create a dict
```python
my_dict = {"jack": 3, "cjj": 2}
```

## 2.get the value
If you wants to get the value , you must know the key
```python
print(dict[<key>])
print(dict.get(<key>))
```

## 3.use the in and the not
you can use the in and the not in to judge whether a 
key is in the dict
```python
if "rose" not in dict:
    print("ERROR")

if "cjj" in dict:
    print("OK")
```

## 4. sort the dict
You should pass in the items, otherwise you can only get the sorted key
```python
a = sorted(my_dict.items(), key=lambda it: it[0])
```


