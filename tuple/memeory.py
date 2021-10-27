

# sample
# store in contrineusly --- next to each other
# tuples are imutables and


# access element

a = tuple("abcde")
print(a[1])


# you cannot overwirte tuple
try:
    a[1] = 'c'
except TypeError:
    print("not working because tuple cannot assing to new valus")

print(a[1])
