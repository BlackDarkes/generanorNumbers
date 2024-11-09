def generateNumbers(count):
    numbers = [];
    
    for i in range(1, count + 1):
        numbers.append(i);
        
    return numbers;

print(generateNumbers(5));