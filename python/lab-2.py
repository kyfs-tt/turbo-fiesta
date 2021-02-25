# Q2: Write a function that takes the last element in a list and moves it to
# the front of the list
def last_to_first(list):
    list.insert(0, list.pop())


# Q3: Write a function that takes a list and a variable number of indices.
# The function should return a tuple of the values at those indices
def get_values_at_indices(list, *args):
    return (list[i] for i in args)


# Q4: Write a function that takes named parameters
# and returns the parameters as a Dictionary of parameter name -> value
def create_programmer(name="", position="", years_of_xp=0, languages=[]):
    return {
      "name": name,
      "position": position,
      "years_of_xp": years_of_xp,
      "languages": languages
    }


print(
  create_programmer(name="Smart", position="Junior Seftware Engineer",
                    years_of_xp=0, languages=["C++", "Python", "Java"])
)


# Q5: Write a function that take an initial value and a tuple of
# ints and accumulates into the initial value
def acc(initial_value=0, numbers=()):
    sum = initial_value
    for i in numbers:
        sum += i
    return sum


print(acc(1, (1, 3, 5)))


# Q6: Rewrite your Fibonacci exercise from earlier to
# use a function that takes an argument for how many numbers are required
def fib(max_element=20):
    F0 = 0
    F1 = 1
    Fn1 = 0
    Fn2 = 0
    for i in range(max_element):
        if i == 0:
            print(F0)
        elif i == 1:
            print(F1)
        else:
            print(Fn1 + Fn2)
            Fn1 = Fn
        
    pass
