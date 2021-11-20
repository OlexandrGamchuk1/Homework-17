def summa(numbers, function):
    summa = 0
    for i in numbers:
        i = function(i)
        summa += i
    return summa

def my_function(number):
    return number * 2

numbers = [3, 124, 244, 4512, 123]
print(summa(numbers, my_function))