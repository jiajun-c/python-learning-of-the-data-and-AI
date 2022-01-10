import re
string = "the background of the book and 2the linux the11"
string_list = string.split()
# 使用 compile 的目的是编译我们的pattern使得其变为正则表达式的形式，从而参与后面的match , search 等方式
pattern = re.compile(r"the", re.I)
count = 0
for word in string_list:
    if pattern.search(word):
        count += 1
        print(pattern.search(word).span())
print(count)
