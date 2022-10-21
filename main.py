def min_numb (number_s):
    min_n = number_s[0]
    for i in range(1, len(number_s)):
        if number_s[i] < min_n:
            min_n = number_s[i]
    return min_n
def max_numb (number_s):
    max_n = number_s[0]
    for i in range(1, len(number_s)):
        if number_s[i] > max_n:
            max_n = number_s[i]
    return max_n
def even (number):
    if (number % 2) == 0:
        return True
def change_numbers(number_s, min_n, max_n):
    for i in range(0,len(number_s)):
        if even(i):
            number_s[i] *= min_n
        else: number_s[i] *= max_n
numbers = [1234,3321,-421,23,44,19,40,18,-21,23,87]
print("Список чисел: " + str(numbers) + "\n")
min_n = min_numb(numbers)
max_n = max_numb(numbers)
print("Минимальное число: " + str(min_n) +"\n" )
print("Максимальное число: " + str(max_n) +"\n" )
change_numbers(numbers, min_n, max_n)
print("Изменённый список чисел: " + str(numbers))