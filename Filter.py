ages = (23, 34, 45, 64, 5, 32)

def myFunc(x):
    if x > 18:
        return False
    else:
        return True

adults = filter(myFunc, ages)

for x in adults:
    print(x)