
inputnumber = int(input('Please input your number: '))

numbers = []
if inputnumber == 0:
    print(1)

while inputnumber:
    numbers.append(inputnumber)
    inputnumber = inputnumber - 1

result = 1
for i in numbers:
    result = numbers[i - 1] * result
    print(result)
print('numbers length', len(numbers))
print(result, numbers)
