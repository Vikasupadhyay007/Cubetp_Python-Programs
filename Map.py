def calculateSquare(n):
    return n*n

number = (5, 2, 3, 1, 6)
result = map(calculateSquare, number)
print(result)

numbersSquare = set(result)
print(numbersSquare)