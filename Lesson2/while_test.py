
i = 1
while (i < 7):
    print(i)
    i += 1
print("End")


i = 1
while i < 10000:
  if i == 3:
     i += 1
     continue
  print(i)
  if i == 7:
    break
  i += 1
print("End")

i = 1
while i < 5:
    j = 1
    while j <4:
       if i == 3:
          break
       print(i,j)
       j += 1
    i += 1