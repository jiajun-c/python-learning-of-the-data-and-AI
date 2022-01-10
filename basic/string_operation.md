# 正则表达式与模式匹配
在正则表达式中， 我们可以使用re库进行操作

##step one

compile the code
```python
re.compile(r"the", re.I)
```
r表示的是可以忽略文章中的转义字符

`re.I` means ingore the upper and the lower, `re.A` means it is limited to the
ASCII match...

[the further learning of the re](https://docs.python.org/3/library/re.html#module-contents)

## step two
find the matched string, we will mainly use the 
function search, match ,fullmatch to find our string

`search`: 在字符串中查找第一个和我们的模式相匹配的位置

`match` : 从字符串的开头进行匹配

`fullmatch:` 这个要求全部的字符串相互匹配