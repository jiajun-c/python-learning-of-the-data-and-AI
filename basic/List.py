a = [1, 2, 3, 4]

print(a[-1])

print(a[1:3])
print(a[2:])
print(a[:4])

b = a
print(b)

# the in and the not function in the list
if 1 in a:
    print("1 is in the a")

# the use of add or delete the elem in the list
a.append(7)
print(a)
a.remove(7)
print(a)
a.pop()
print(a)


def cmp(b):
    return b


k = [3, 4, 1, 3]
k = sorted(k)
# the default is decrease
print(k)

k = sorted(k, reverse=True)
print(k)

sorted(a, key=cmp)
print(a)
