# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.



# Part 1

def total_cost(state, price, tax=5):
    """Returns the price of an item with tax.""" 
    tax_in_decimal = float(tax) / 100
    tax_on_item = tax_in_decimal * price
    total_price = price + tax_on_item
    print "In the state of" + " " + state + " " + "the item costs" + " $" + str(total_price)

# Part 2

# 1.

def is_berry(fruit):
    """Determines if the fruit inputted is equal to specified fruits."""
    if fruit == "strawberry" or fruit == "cherry" or fruit == "blackberry":
        return True
    else:
        return False


def shipping_cost(fruit):
   """Returns a value dependent on the response from is_berry function.""" 
    if is_berry(fruit) is True:
        return 0
    elif is_berry(fruit) is False:
        return 5

# 2.

def is_hometown(town):
    """Compares inputted hometown to Oakland."""
    if town.lower() == "Oakland":
        return True
    else:
        return False


def full_name(first, last):
    """Concatenates first name and last name."""
    return first + " " + last


def hometown_greeting(town, first, last):
    """Prints a statement dependent on if hometown is equal to or different from Oakland."""
    if is_hometown(town) is True:
        print "Hi" + " " + full_name(first, last) + ", " + "we're from the same place!"
    elif is_hometown(town) is False:
        print "Hi" + " " + full_name(first, last) + ", " + "where are you from?"

# Part 3

# 1.

def increment(x = 1):
    def add(y):
        """Returns the sum of two numbers."""
        return x + y
    return add

# 2.

addfive = increment(5)

print addfive(5)
print addfive(20)

# 3.

def adding_numbers(number, list_numbers):
    """Add a number to the end of a list."""
    list_numbers.append(number)
    return list_numbers





#####################################################################