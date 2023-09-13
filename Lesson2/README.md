
#
# 分支语句
## if ... else
if 关键字用于创建条件语句（if 语句），并且仅当条件为 True 时，才允许您执行代码块。使用 else 关键字在条件为 False 执行代码。

### 实例
如果 x 大于 9 则打印 "YES"，否则打印 "NO"：
```Python
x = 5
if x > 9:
  print("YES")
else:
  print("NO")
```

## elif
elif 关键字用在条件语句（if 语句）中，它是 else if 的简写。

### 实例
如果变量 i 是争执，则打印 "YES"，如果 i 是 0 则打印 "WHATEVER"，否则打印 "NO"：
```Python
for i in range(-5, 5):
  if i > 0:
    print("YES")
  elif i == 0:
    print("WHATEVER")
  else:
    print("NO")
```

# 循环语句
Python 提供了两种循环语句 `for` 和 `while`

## while 循环
如果使用 while 循环，只要条件为真，我们就可以执行一组语句。

### 实例
只要 i 小于 7，打印 i：
```Python
i = 1
while i < 7:
  print(i)
  i += 1
```
## for 循环


## break 语句
如果使用 break 语句，即使 while 条件为真，我们也可以停止循环：

### 实例
在 i 等于 3 时退出循环：
```Python
i = 1
while i < 7:
  print(i)
  if i == 3:
    break
  i += 1
```

## continue 语句
continue 关键字用于在 for 循环（或 while 循环）中结束当前迭代，然后继续下一个迭代。

### 实例
如果变量 i 为 5，则跳过迭代，但继续进行下一个迭代：
```Python
for i in range(9):
  if i == 5:
    continue
  print(i)
运行实例
```
在 while 循环中使用 continue 关键字：
```Python
i = 0
while i < 9:
  i += 1
  if i == 5:
    continue
  print(i)
```
