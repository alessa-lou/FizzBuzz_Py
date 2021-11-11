def fizzbuzz(n):
    if not isinstance(n, int):
        raise TypeError("Enter a number, fool")

    if n == 3:
        return "Fizz"
    elif n == 15:
        return "FizzBuzz"
    elif n == 5:
        return "Buzz"
    else:
        return n