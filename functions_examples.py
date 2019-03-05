
# define a say hello function that accepts a name, greeting and
# punctuation

# practice calling the unction with both positional an keyword arguments


def sayhello(name='Dd', greeting='Whattup', punctuation='?'):
    print(greeting+', '+name+punctuation)


sayhello('dude', 'Yo', '!')
sayhello(greeting='Cowabunga', punctuation='!!!', name='peeps')
sayhello('dog', punctuation='?!', greeting='What\'s happening')


def sayhello2(name, greeting, punctuation):
    print(greeting+', '+name+punctuation)

# ERROR MANIA

# SyntaxError: positional argument follows keyword argument
# sayhello('world', punctuation='?!', 'Hello')

# SyntaxError: invalid syntax
# sayhello(,,,)

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# sayhello('Joe', 2123)

# TypeError: int() argument must be a string, a bytes-like object
# or a number, not 'NoneType'
# int(sayhello())

# TypeError: sayhello2() missing 3 required positional
# arguments: 'name', 'greeting', and 'punctuation'
# sayhello2()
