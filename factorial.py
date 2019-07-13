
inputnumber = int(input('Please input your number: '))

numbers = [inputnumber]
if inputnumber == 0:
    print(1)

while inputnumber > 1:
    numbers.append(inputnumber - 1)
    inputnumber = inputnumber - 1
result = 1
# time = len(numbers) - 1
# for number in numbers:
#     result = numbers[time] * result
#     time = time - 1

for i in numbers:
    result = numbers[i - 1] * result
    print(result)
print('numbers length', len(numbers))
print(result, numbers)
