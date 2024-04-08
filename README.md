# midterm-programming-design-2024

Midterm: Programming Design 2024.

## 01. Define a function `range_fizz_buzz()` which returns the FizzBuzz numbers within certain range $a \le b$ in a `list`.

Source: <https://en.wikipedia.org/wiki/Fizz_buzz>

```python
def range_fizz_buzz(a: int, b: int) -> list:
    """
    >>> range_fizz_buzz(1, 5)
    [1, 2, 'Fizz', 4, 'Buzz']
    >>> range_fizz_buzz(6, 10)
    ['Fizz', 7, 8, 'Fizz', 'Buzz']
    >>> range_fizz_buzz(11, 15)
    [11, 'Fizz', 13, 14, 'Fizz Buzz']
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 02. Define a function `cumulative_sum()` which returns cumulative sum given `*args` of numbers.

```python
def cumulative_sum(*args) -> list:
    """
    >>> cumulative_sum(1, 2, 3)
    [1, 3, 6]
    >>> cumulative_sum(2, 3, 5)
    [2, 5, 10]
    >>> cumulative_sum(2, 3, 5, 7, 11)
    [2, 5, 10, 17, 28]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 03. Define a function `return_days_abbreviation_from_int()` which returns weekday/weekend abbreviations given its order.

```python
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
```

```python
def return_days_abbreviation_from_int(x: int) -> tuple:
    """
    >>> return_days_abbreviation_from_int(0)
    ('Sunday', 'Sun.')
    >>> return_days_abbreviation_from_int(1)
    ('Monday', 'Mon.')
    >>> return_days_abbreviation_from_int(2)
    ('Tuesday', 'Tue.')
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 04. Define a function `median_args()` which returns the median of `*args`.

```python
def median_args(*args):
    """
    >>> median_args("January", "February", "March")
    "February"
    >>> median_args("January", "February", "March", "April")
    ("February", "March")
    >>> median_args(5, 2, 3)
    3
    >>> median_args(5, 7, 2, 3)
    4.0
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 05. Define a function `square_negatives()` which returns positive ones given a `list`.

```python
def square_negatives(x: list) -> list:
    """
    >>> square_negatives([-3, -2, -1, 0, 1, 2, 3])
    [9, 4, 1]
    >>> square_negatives([-3, -2, -1, 0, 1, 2, 3, '4', '5'])
    [9, 4, 1]
    >>> square_negatives([-3, -2, -1, False, True, 2, 3, '4', '5'])
    [9, 4, 1]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 06. Define a function `filter_non_negatives()` which returns non-negative ones given a `list`.

```python
def filter_non_negatives(x: list) -> list:
    """
    >>> filter_non_negatives([-3, -2, -1, 0, 1, 2, 3])
    [0, 1, 2, 3]
    >>> filter_non_negatives([-3, -2, -1, 0, 1, 2, 3, '4', '5'])
    [0, 1, 2, 3]
    >>> filter_non_negatives([-3, -2, -1, False, True, 2, 3, '4', '5'])
    [False, True, 2, 3]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 07. Define a function `find_min_max()` which finds the minimum and maximum values given a `list`.

```python
def find_min_max(x: list) -> dict:
    """
    >>> find_min_max([2, 3, 5, 7, 11])
    {'min': 2, 'max': 11}
    >>> find_min_max([13, 17, 19, 23, 29, 31])
    {'min': 13, 'max': 31}
    >>> find_min_max([10, 9, 8, 6, 4, 1])
    {'min': 1, 'max': 10}
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 08. Define a function `find_idxmin_idxmax()` which finds the indices of minimum and maximum values, respectively given a `list`.

```python
def find_idxmin_idxmax(x: list) -> dict:
    """
    >>> find_idxmin_idxmax([2, 3, 5, 7, 11])
    {'idxmin': [0], 'idxmax': [4]}
    >>> find_idxmin_idxmax([2, 3, 5, 7, 11, 11, 7, 5, 3, 2])
    {'idxmin': [0, 9], 'idxmax': [4, 5]}
    >>> find_idxmin_idxmax([10, 9, 8, 6, 4, 1])
    {'idxmin': [5], 'idxmax': [0]}
    >>> find_idxmin_idxmax([10, 9, 8, 6, 4, 1, 1, 4, 6, 8, 9, 10])
    {'idxmin': [5, 6], 'idxmax': [0, 11]}
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 09. Define a function `pig_latin()` which plays the Pig Latin language game with function inputs.

- For words that begin with consonant sounds, all letters before the initial vowel are placed at the end of the word sequence. Then, "ay" is added. e.g. "pig" -> "igpay". When words begin with consonant clusters (multiple consonants that form one sound), the whole sound is added to the end. e.g. "smile" -> "ilesmay"
- For words that begin with vowel sounds, the vowel is left alone, and "yay" is added to the end. e.g. "eat" -> "eatyay"

Source: <https://en.wikipedia.org/wiki/Pig_Latin>

```python
def pig_latin(x: str) -> str:
    """
    >>> pig_latin("pig")
    'igpay'
    >>> pig_latin("smile")
    'ilesmay'
    >>> pig_latin("eat")
    'eatyay'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 10. Define a function `fibonacci()` which returns the famous Fibonacci sequence in a `list` given `a`, `b` ($a \le b$) and `length` as parameters.

Source: <https://en.wikipedia.org/wiki/Fibonacci_sequence>

```python
def fibonacci(a: int, b: int, length: int) -> list:
    """
    >>> fibonacci(0, 1, 5)
    [0, 1, 1, 2, 3]
    >>> fibonacci(0, 1, 7)
    [0, 1, 1, 2, 3, 5, 8]
    >>> fibonacci(0, 1, 11)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```