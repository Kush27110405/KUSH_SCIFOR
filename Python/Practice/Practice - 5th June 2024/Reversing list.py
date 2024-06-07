def func(list1):
  l = []
  for i in range(len(list1) - 1,-1,-1):
    l.append(list1[i])
  return l

list1 = [1,2,3,4,5]
print(func(list1))
