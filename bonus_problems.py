# 1. Write a function named `add`. It should accept two arguments and return the result of adding the two arguments together.
def add(x, y):
    return x + y

# 2. Write a function named `subtract`. It should accept two arugments and return the result of subtracting the first from the second.


def substract(x, y):
    return y - x


# 3. Write a function named `multiply`. It should accept two numbers and return the result of multiplying them together.
def multiply(x, y):
    return x * y


# Bonus: don't use the `*` operator in your `multiply` function
def multiply_no_splat(x, y):
    i = 0
    for i in range(y + 1):
        i + i
    return i


def multiply_no_splat_no_loop(base, multiplier, i=0, product=0):
    i += 1
    product += base
    if i == multiplier + 1:
        return product - base
    else:
        print('i: '+str(i)+' product: '+str(product))
    return multiply_no_splat_no_loop(base, multiplier, i, product)


print('PRODUCT: '+str(multiply_no_splat_no_loop(2, 3,)))
