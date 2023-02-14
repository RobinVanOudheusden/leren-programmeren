def fibonacci(getal):
    a, b = 0, 1
    resultaat = []
    for i in range(getal):
        resultaat.append(a)
        a, b = b, a + b
    return resultaat
    
print(fibonacci(20))