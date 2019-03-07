# # 1 --- Read the contents of your last exercise file into a variable.

# # 1i.   Print out every line in the file
# with open('4.5_import_exercises.py') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line)

# # 1ii.  Print out every line in the file, but add a line numbers
# with open('4.5_import_exercises.py') as f:
#     lines = f.readlines()
#     i = 0
#     for line in lines:
#         i += 1
#         print(f'{i} \t' + line)


# 2 --- Write some python code to create a grocery list.

# 2i.   Create a variable named grocery_list. It should be a list, and
# the elements in the list should be a least 3 things that you need to
# buy from the grocery store.

grocery_list = ['oranges', 'snack', 'meat']

# 2ii.  Create a function named make_grocery_list. When run, this
# function should write the contents of the grocery_list variable
# to a file named my_grocery_list.txt.


def make_grocery_list(groceries):
    with open('my_grocery_list.txt', 'w') as f:
        for item in groceries:
            f.write(item + ',')


# 2iii. Create a function named show_grocery_list. When run, it should
# show each item on the grocery list.


def show_grocery_list():
    with open('my_grocery_list.txt') as f:
        lines = f.readlines()
        for line in lines:
            print(line)


# 2iv.  Create a function named buy_item. It should accept the name of
# an item on the grocery list, and remove that item from the list.

def buy_item(item):
    new_list = []
    print('Item is "' + item + '."')
    with open('my_grocery_list.txt') as f:
        contents = f.read()
        lines = contents.split(',')
        for line in lines:
            if line == item:
                continue
            else:
                new_list.append(line)
    make_grocery_list(new_list)


make_grocery_list(grocery_list)
show_grocery_list()
buy_item(input('What item to buy? '))
show_grocery_list()