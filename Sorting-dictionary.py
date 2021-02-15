dict = {'a':1,'b':2,'c':3}
min = min(dict, key=dict.get)
print(min)

max = max(dict, key=dict.get)
print(max)