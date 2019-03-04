# Problem 1: Print an average of 3 numbers
a, b, c = 50, 60, 70
average = (a + b + c) / 3
print(average)

# Problem 2: Print an average of a list
scores = [50, 60, 70]
average = sum(scores) / len(scores)
print(average)

# Problem 3: Print a median of a list
five_numbers = [50, 60, 70, 65, 80]
four_numbers = [50, 60, 70, 65]


def median(numbers):
    length = len(numbers)
    half = length // 2 - int(length % 2 == 0)
    middle = sorted(numbers)[half:-half]
    median = sum(middle) / len(middle)
    return median


print(median(five_numbers))
print(median(four_numbers))