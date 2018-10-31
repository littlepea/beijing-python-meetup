autoscale: true
build-lists: true
theme: Top20Talent
footer: © Evgeny Demchenko, 2018.

![inline](https://i.gyazo.com/846955abfb8b4d99421e1a56d1132222.png)

# **PYTHON TIPS & TRICKS**

-

## **By** Evgeny Demchenko

## **CTO** at Top20Talent

[.background-color: #000000]
[.header: #FFFFFF]
[.header-strong: #FFFFFF]

---

## [fit] **TALK** _OVERVIEW_

* Boolean expression
* Loops
  * List and Dictionary comprehensions
* Useful data structures
* Functional tools

---

# [fit] **BOOLEAN** _EXPRESSIONS_

---

# [fit] **TRUTHFUL** _CONDITIONS_

```python
if x is not False \
        and x != None \
        and x != [] \
        and x != '' \
        and x != 0:
    print('Bad')
```

---

# [fit] **TRUTHFUL** _CONDITIONS_

```python
if x:
    print('Good')
```


---

# [fit] **USEFUL** _ONE-LINERS_

```python
def yes_or_no(x):
    if x > 10 and x <= 20:
        return 'yes'
    else:
        return 'no'
```
---

# [fit] **USEFUL** _ONE-LINERS_

```python
def yes_or_no(x):
    return 'yes' if 10 < x <= 20 else 'no'
```

---

# [fit] **all** & _any_

```python
def true_or_false(x, y):
    if isinstance(x, int) and x > 10 and x <=20 and x != y:
        return True
    return False
```

---

# [fit] **all** & _any_

```python
def true_or_false(x, y):
    return all([
        isinstance(x, int),
        10 < x <=20,
        x != y
    ])
```
---

# [fit] **LOOPS**

---

# [fit] **ENUMERATE**

```python
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

i = 0
for f in fib:
    print(f'Fibonacci of {i} is {f}')
    i += 1
```

---

# [fit] **ENUMERATE**

```python
for i, f in enumerate(fib):
    print(f'Fibonacci of {i} is {f}')


for i, f in zip(range(11), fib):
    print(f'Fibonacci of {i} is {f}')
```

---

# [fit] **FILTERING** _LISTS_

```python
odds = []
for n in fib:
    if n % 2 != 0:
        odds.append(n)
```

---

# [fit] **FILTERING** _LISTS_

```python
odds = list(filter(lambda n: n % 2 !=0, fib))


odds = [
    n
    for n in fib
    if n % 2 != 0
]
```

---

# [fit] **LIST** _COMPREHENSIONS_

```python
sum_of_squares = 0
for n in fib:
    sum_of_squares += n**2
```

---

# [fit] **LIST** _COMPREHENSIONS_

```python
sum_of_squares = sum(n**2 for n in fib)
```

---

# [fit] **DICTIONARY** _COMPREHENSIONS_

```python
fib_mapping = {}
for i, n in enumerate(fib):
    fib_mapping[i] = n
```

---

# [fit] **DICTIONARY** _COMPREHENSIONS_

```python
fib_mapping = {
    i: n
    for i, n in enumerate(fib)
}
```

---

# [fit] **DICTIONARY** _ITEMS_

```python
for key, value in fib_mapping.items():
    print(f'Fibonacci of {key} is {value}')
```

---

# [fit] **USEFUL** _DATA STRUCTURES_

---

# [fit] **collections**._defaultdict_

```python
numbers = [1,1,2,3,4,4,5]

number_counts = {}
for number in numbers:
    if number not in number_counts:
        number_counts[number] = 0
    number_counts[number] += 1
```

---

# [fit] **collections**._defaultdict_

```python
from collections import defaultdict

number_counts = defaultdict(int)
for number in numbers:
    number_counts[number] += 1
```

---

# [fit] **collections**._Counter_

```python
from collections import Counter

number_counts = Counter(numbers)
```

---

# [fit] **FUNCTIONAL** _TOOLS_

---

# [fit] **NAIVE** _FizzBuzz_

```python
def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    if number % 3 == 0:
        return 'Fizz'
    if number % 5 == 0:
        return 'Buzz'
    return str(number)
```

---

# [fit] **READABLE** _FizzBuzz_

```python
def divisible_by(div, number):
    return number % div == 0

def fizzbuzz(number):
    if divisible_by(3, number) and divisible_by(5, number):
        return 'FizzBuzz'
    if divisible_by(3, number):
        return 'Fizz'
    if divisible_by(5, number):
        return 'Buzz'
    return str(number)
```
---

# [fit] **functools**._partial_

```python
from functools import partial


divisible_by_3 = partial(divisible_by, 3)
divisible_by_5 = partial(divisible_by, 5)
```
---

# [fit] **MORE READABLE** _FizzBuzz_

```python
def fizzbuzz(number):
    if divisible_by_3(number) and divisible_by_5(number):
        return 'FizzBuzz'

    if divisible_by_3(number):
        return 'Fizz'

    if divisible_by_5(number):
        return 'Buzz'

    return str(number)
```

---

![inline 90%](https://www.top20talent.com/wp-content/uploads/2017/09/logotype-1.png)

# Q&A
