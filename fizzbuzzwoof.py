number = range(1,101)

for num in number:
    fizzCount = 0
    buzzCount = 0
    woofCount = 0

    # If number CONTAINS 3, 5 or 7, add the word once
    for n in str(num):
        if n == '3':
            fizzCount = fizzCount + 1
        elif n == '5':
            buzzCount = buzzCount + 1
        elif n == '7':
            woofCount = woofCount + 1

    # If number is DIVISIBLE by 3, 5 or 7, add the word once
    if num % 3 == 0:
        fizzCount = fizzCount + 1
    if num % 5 == 0:
        buzzCount = buzzCount + 1
    if num % 7 == 0:
        woofCount = woofCount + 1

    # Arrange words (if more than one occur) in the order given in the title
    print (str(num) + ': ' + ("Fizz " * fizzCount) + ("Buzz " * buzzCount) + ("Woof " * woofCount))