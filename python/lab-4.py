import timeit

print(timeit.timeit(setup='myArray = range(1000)',
                    stmt='[x ** 2 for x in myArray]', number=1000))


# # import ms.version
# import numpy as np

# # ms.version.addpkg('numpy', 1, 13, 3)
# otherArray = np.arange(1000)
